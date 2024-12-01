import os
from dotenv import load_dotenv

load_dotenv()

class Variables:
    # Database variables config   
    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_DB_TEST = os.environ["POSTGRES_DB_TEST"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    DATABASE_PATH = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    DATABASE_TEST_PATH = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_TEST}'
    
    # Auth variables config   
    AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
    ALGORITHMS = [os.environ["ALGORITHMS"]]
    API_AUDIENCE = os.environ["API_AUDIENCE"]

    # Token config
    Casting_Assistant_Token = os.environ["Casting_Assistant_Token"]
    Casting_Director_Token = os.environ["Casting_Director_Token"]
    Executive_Producer_Token = os.environ["Executive_Producer_Token"]