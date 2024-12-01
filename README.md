# Casting Agency Capstone Project

This is my final capstone project for Udacity's FullStack Web Developer Nanodegree.
Web app can be accessed at [here](https://flaskcasting.herokuapp.com)

##### Project Dependencies
* __Flask__ - Slim python web library.
* __SQLAlchemy__ - Python ORM library
* __Heroku__ - PaaS platform for easy hosting of web apps
* __Postman__ - API testing tool

### Installation instructions
* Clone project to directory of your choice.
* Create a virtualenv in project directory
* run ```pip install -r requirements.txt``` to install project dependencies
* add ```DATABASE_URL``` to environment variables of your system. 
On Unix systems, use ```export DATABASE_URL={username}:{password}@{host}:{port}/{database_name}```
* run ```export FLASK_APP=app.py```
* type ```flask run``` in terminal

###Endpoints:
* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/

### Roles
* Casting Assistant
    * GET /actors and /movies

* Casting Director
    * GET /actors and /movies
    * ADD /actors and DELETE /actors
    * PATCH /actors and /movies
    
* Executive Producer
    * GET /actors and /movies
    * ADD /actors and DELETE /actors
    * PATCH /actors and /movies
    * ADD /movies and DELETE /movies


## API Endpoints

In the next few subsections, we'll cover how the API works and what you can expect back in the results.

### Default Path

#### GET /
Verifies that application is up and running on Heroku.

Sample response:
```
{
    "description": "App is running.",
    "success": true
}
```

### GET Endpoints

#### GET /movies
Displays all movies listed in the database.

Sample response:
```
{
    "movies": [
        {
            "id": 3,
            "release_year": 2008,
            "title": "Movie 3"
        },
        {
            "id": 4,
            "release_year": 1973,
            "title": "Movie 4"
        },
    ],
    "success": true
}
```

#### GET /actors
Displays all actors / actresses listed in the database.

Sample response:
```
{
    "actors": [
        {
            "age": 34,
            "gender": "female",
            "id": 3,
            "movie_id": 2,
            "name": "Actor 3"
        },
        {
            "age": 34,
            "gender": "male",
            "id": 4,
            "movie_id": 3,
            "name": "Actor 4"
        },
    ],
    "success": true
}
```

### POST Endpoints

#### POST /movies/
Creates a new movie entry in the database.

Sample response:
```
{
    "movie_id": 8,
    "success": true
}
```

#### POST /actors/
Creates a new actor / actress entry in the database.

Sample response:
```
{
    "actor_id": 7,
    "success": true
}
```

### PATCH Endpoints

#### PATCH /movies/<id>
Updates movie information given a movie_id and newly updated attribute info.

Sample response:
```
{
    "movie_id": 2,
    "success": true
}
```

#### PATCH /actors/<id>
Updates actor information given a actor_id and newly updated attribute info.

Sample response:
```
{
    "actor_id": 2,
    "success": true
}
```

### DELETE Endpoints

#### DELETE /movies/<id>
Deletes a movie entry from the database given the inputted movie_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/<id>
Deletes an actor / actress entry from the database given the inputted actor_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```
