import os
from flask import Flask, jsonify, abort, request
from auth import AuthError, requires_auth
from models import Actor, Movie, setup_db
from flask_cors import CORS


def create_app(test_config=None):

    app = Flask(__name__)
    CORS(app)
    setup_db(app)
    

    @app.after_request
    def after_request(response):
        """After_request decorator to set Access-Control-Allow"""
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, True')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, DELETE, PATCH, OPTIONS')
        return response

    @app.route('/movies', methods=['GET'])
    @requires_auth('view:movies')
    def get_movies(payload):
        """
        Fetches all movies from the database and returns them as a JSON response.
        """
        movies = Movie.query.all()

        if not movies:
            abort(404, "No movies found.")

        movies_data = [movie.format() for movie in movies]
        return jsonify({
            "success": True,
            "movies": movies_data
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        """
        create a new movie to the database.
        """
        try:
            data = request.get_json()
            movie_title = data.get('title')
            release_year = data.get('release_year')

            if not (movie_title and isinstance(release_year, int)):
                abort(422, "Missing or invalid movie data.")

            movie = Movie(title=movie_title, release_year=release_year)
            movie.insert()

            return jsonify({
                'success': True,
                'movie_id': movie.id
            })
        except Exception as e:
            abort(500, f"Internal Server Error: {str(e)}")

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        """Deletes a movie by its ID.
        """
        movie = Movie.query.filter(Movie.id == id).one_or_none()

        if movie:
            try:
                movie.delete()
                return jsonify({'success': True, 'deleted': id})
            except Exception as err:
                abort(422, f"Failed to delete movie: {str(err)}")
        else:
            abort(404, 'Movie not found')

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(payload, id):
        """Updates a movie by its ID.
        """
        movie = Movie.query.get(id)

        if movie:
            try:
                data = request.get_json()
                if data is None:
                    abort(400, "Missing request body")

                title = data.get('title')
                if title:
                    movie.title = title

                release_year = data.get('release_year')
                if release_year:
                    movie.release_year = release_year

                movie.update()

                return jsonify({'success': True, 'movie_id': movie.id})
            except Exception as err:
                abort(422, f"Failed to update movie: {str(err)}")
        else:
            abort(404, 'Movie not found')

    @app.route('/actors', methods=['GET'])
    @requires_auth('view:actors')
    def get_actors(payload):
        """Retrieves a list of all actors.
        """

        actors = Actor.query.all()

        if not actors:
            abort(404, 'No actors found')

        formatted_actors = [actor.format() for actor in actors]

        return jsonify({'success': True, 'actors': formatted_actors})

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        """
        Creates a new actor.
        """

        try:
            body = request.get_json()

            if not body:
                abort(400, 'Request body is missing')

            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')
            movie_id = body.get('movie_id')

            if not name or not age or not gender or not movie_id:
                abort(400, 'Name, age, gender, and movie_id are required fields')

            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
            actor.insert()

            return jsonify({"success": True}), 201
        except Exception as err:
            # Log the error for debugging
            app.logger.error(f"Error creating actor: {str(err)}")
            abort(400, 'An error occurred while creating the actor.')

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, id):
        """
        Deletes an existing actor.
        """

        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if not actor:
                abort(404)

            actor.delete()

            return jsonify({
                "success": True,
                "deleted": id
            }), 200
        except Exception as e:
            # Log the error for debugging
            app.logger.error(f"Error deleting actor: {str(e)}")
            abort(400, 'An error occurred while deleting the actor.')

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(jwt, id):
        """
        Updates an existing actor.
        """

        try:
            actor = Actor.query.get(id)

            if not actor:
                abort(404)

            body = request.get_json()

            # Update actor properties only if provided in the request body
            if body:
                actor.name = body.get('name', actor.name)
                actor.age = body.get('age', actor.age)
                actor.gender = body.get('gender', actor.actor.gender)
                actor.movie_id = body.get('movie_id', actor.movie_id)

            actor.update()

            return jsonify({
                "success": True,
                "actor_id": actor.id
            }), 200
        except Exception as e:
            # Log the error for debugging
            app.logger.error(f"Error updating actor: {str(e)}")
            abort(400, 'An error occurred while updating the actor.')

    # Error Handler (422) Unprocessable
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    # Error Handler (404) Not Found
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    # Error Handler (400) Bad request
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    # Error Handler (401) Unauthorized
    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error,
        }), 401
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
