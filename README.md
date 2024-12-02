# Capstone Project for Udacity's Full Stack Developer Nanodegree

This is my final capstone project for Udacity's FullStack Web Developer Nanodegree.
Web app can be accessed at [here](https://baotcn-capstone-e1c5b8baa700herokuapp.com/)

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


### Roles
* Casting Assistant
	* Can view actors and movies
    * has view:actors, view:movies permissions
* Casting Director
	* All permissions a Casting Assistant has and…
	* Add or delete an actor from the database
	* Modify actors or movies
    * has view:actors, view:movies, delete:actors, post:actors, update:actors, update:movies permissions
* Executive Producer
	* All permissions a Casting Director has and…
	* Add or delete a movie from the database
    * has view:actors, view:movies, delete:actors, post:actors, update:actors, update:movies, post:movies, delete:movies

### Permissions
* `view:actors`
* `view:movies`
* `delete:actors`
* `post:actors`
* `update:actors`
* `update:movies`
* `post:movies`
* `delete:movies`

### Set JWT Tokens
Use the following link to create users and sign them in

```
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```

YOUR_DOMAIN = dev-akuhtykoddz2bf0k.us.auth0.com
API_IDENTIFIER = capstone
YOUR_CLIENT_ID = 063PqMh9ABrOVEfD4Ux9gss6Gs6ElXxL
YOUR_CALLBACK_URI = https://baotcn-capstone-e1c5b8baa700herokuapp.com/

###API Reference:
Base URL: This application can be run locally. The hosted version is at (https://baotcn-capstone-e1c5b8baa700.herokuapp.com/)

### JWT Tokens for each role:
* Casting Assistant - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImYwelk3NVN6YXE2OExNTTNtVzVmXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ha3VodHlrb2RkejJiZjBrLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzRjMWU2ODg5NWYyMTZhNzk5NmY0NDIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczMzE2MTIyMSwiZXhwIjoxNzMzMTY4NDIxLCJzY29wZSI6IiIsImF6cCI6IjA2M1BxTWg5QUJyT1ZFZkQ0VXg5Z3NzNkdzNkVsWHhMIiwicGVybWlzc2lvbnMiOlsidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.M-9zYHZ9ReLEPkcZowgek4a0_5R6ZpgMn42IRj2coqcBFeBXliyvXWkT7RpUUMBIBcfM1V1iq0MpAFsB6t1-gf9benhTJcDMh7Ev_CivyF7mJjv53yKQLj2fR_aEwOvQ7tdY59htunosbeROUnfiA0tKttdnz5F-AV4SauQSvABHY8qhwJHcjl0Vr9RqvXE9Ov9TDaeMcoJSA4uvAnJ3BSblnqe-aMD82C9Pz9YcDVitdyn2i8mpy-foDzB4XlABmS3UJHMGdeOPybj6bWQwoLLgY4gJDN-RJeyEx2KyN7NK-en-23gXEFAq51kcEdhGJahH238I86BB7S1TWp0pcg```

* Casting Director- ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImYwelk3NVN6YXE2OExNTTNtVzVmXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ha3VodHlrb2RkejJiZjBrLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzRjNTMyOTY3MzBhN2EwYjM4MmZjMzUiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczMzA2OTU1NiwiZXhwIjoxNzMzMDc2NzU2LCJzY29wZSI6IiIsImF6cCI6ImllUzFxdldRbXVJVllEeEhEckthdFBReWI2U3JpT0g5IiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.Y0YT-YWNMiNrEmRcOmdV98i6jp4Y3GwRxGPUHMDUzRgQ0T6Y8FQad4hjd7czyRkBhnImWnpyNrUTsAic6MYaxtGrM8RVYEzAYwxwzbLomJlUhIDbqB3Jl-auUQTvtYNU8fkixRarxLiP8rVr7_JKpntIsPjiCmXH6flR-oJwcjHhNXUM26GFzkQ45350FIGXHRlXOsjCdi5b8q_9QKyxtHgTI7IztxcfXBWZyu-AdAKPCIqnZwqUeSRauIjvfauQh2GVmg9JO-4uky1lT81C86TJfdwaZY94qcs3VqupyfZyQgusUzhupdvk0d9f2MlR0xRV6XeH1g-g_oGXjwjP6g```

* Executive Producer - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImYwelk3NVN6YXE2OExNTTNtVzVmXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ha3VodHlrb2RkejJiZjBrLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzRjMTVjMDg5NWYyMTZhNzk5NmYwNWIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczMzA2OTQzNCwiZXhwIjoxNzMzMDc2NjM0LCJzY29wZSI6IiIsImF6cCI6ImllUzFxdldRbXVJVllEeEhEckthdFBReWI2U3JpT0g5IiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.U23wUHpiLRwS7PUuiaKRAnsGY735ezAF02Boum27NvVRh-nydz0KyH3XnNAdaiW0abllUaoCz7qo88cv9w75PH0F1rseDolu0LC5xy1vhkoMPMf8JjVPNbQe1yfjxLgQcvpRF_jCllJ8f27a-t0mX0nrec8e2Uub3a_JLulUfzAz9CPhBwRE9vJNxONg0SQLWhN2RkeUgTAGuilFk3AlyzmzsZBx_aTLOp8sbHbFSq0-3s1ooUQEWYpxbtv-BFHQLqQxjLfKn06NPOnipED3BtkUbaOzx3GU0vj_YIOFIBqaVrYfYZ_-6Fx4BHwcgNSdKjxorTSxPOcASMNFjaDCkA```

### Default Path

#### GET /
Verifies that application is up and running on Heroku.

Sample response:
```
{'health': 'Running!!'}
```

* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/

### Roles-API-Using
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
