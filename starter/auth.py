import json
from urllib.request import urlopen
from flask import abort, request
from functools import wraps
from jose import jwt
from starter.config import Variables


AUTH0_DOMAIN = Variables.AUTH0_DOMAIN
ALGORITHMS = Variables.ALGORITHMS
API_AUDIENCE = Variables.API_AUDIENCE

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header
'''
    it should attempt to get the header from the request
        it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
        it should raise an AuthError if the header is malformed
    return the token part of the header
'''


def get_token_auth_header():
    """Get token from header"""
    auth_header = request.headers.get("Authorization", None)
    if not auth_header:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization header is missing"
        }, 401)

    spl_auth = auth_header.split()

    if spl_auth[0].lower() != "bearer":
        raise AuthError({
            "code": "invalid_token",
            "description": "The authorization header is missing"
        }, 401)
    elif len(spl_auth) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found'
        }, 401)
    elif len(spl_auth) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    token = spl_auth[1]

    return token


'''
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission string is not in the payload permissions array
    return true otherwise
'''


def check_permissions(permission, payload):
    """Used to check permissions"""
    if "permissions" not in payload:
        raise AuthError({
            "code": "invalid_claims",
            "description": "Permissions not found in JWT payload"
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not allowed.'
        }, 403)

    return True


'''
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload

    !!NOTE urlopen has a common certificate error described here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
'''


def verify_decode_jwt(token):
    """Used to verify token"""
    url = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(url.read())
    unverified_header = jwt.get_unverified_header(token=token)

    if "kid" not in unverified_header:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization malformed"
        }, 401)

    rsa_key = next(
        (key for key in jwks["keys"] if key["kid"] == unverified_header["kid"]), None)
    if rsa_key:
        rsa_key = {
            "kty": rsa_key["kty"],
            "kid": rsa_key["kid"],
            "use": rsa_key["use"],
            "n": rsa_key["n"],
            "e": rsa_key["e"]
        }

        try:
            payload = jwt.decode(
                token=token,
                key=rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://{}/'.format(AUTH0_DOMAIN)
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 400)


'''
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
'''


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = get_token_auth_header()
                payload = verify_decode_jwt(token)
                check_permissions(permission, payload)
            except AuthError as err:
                print(err.error)
                abort(err.status_code)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
