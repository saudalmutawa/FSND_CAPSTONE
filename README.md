# CAPSTONE Project 

## Celebrities API Final Project
The Celebrities API project is a project where you can add, delete, update and view actors and movies.
There are 2 user roles who can manipulate movies and actors.

* DIRECTED ROLE: GET movies and actors, DELETE actors, UPDATE movies and actors, POST actors.
* EXECUTIVE ROLE: GET movies and actors, DELETE movies and actors, update movies and actors, POST movies and actors (DOES IT ALL).

## Local Development

### Installing Dependencies
1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

### Running the server

To run the server, execute:

```bash
flask run --reload
```
### Unittesting the application
To test the application locally run the following command

```bash
python test_app.py
```

##Hosting Instructions
First, we need to create an account with Heroku here and then we need to download the Heroku CLI (Command Line Interface) in order to run commands from the terminal that enable us to create a Heroku application and manage it.
After you create your account, install Heroku with Homebrew by running:
` brew tap heroku/brew && brew install heroku `

If you need alternate instructions for the download they can be found here. You can verify the download by typing
` which heroku `
Once you have the Heroku CLI you can start to run Heroku commands! Enter ` heroku login `and then provide your authentication information. Now you can start running Heroku commands for your account and applications.

### Create Heroku app
In order to create the Heroku app run ` heroku create name_of_your_app ` The output will include a git url for your Heroku application. Copy this as, we'll use it in a moment.

### Add git remote for Heroku to local repository
Using the git url obtained from the last step, in terminal run:
` git remote add heroku heroku_git_url `.
Run ` heroku config --app name_of_your_application ` in order to check your configuration variables in Heroku. You will see DATABASE_URL and the URL of the database you just created. That's excellent, but there were a lot more environment variables our apps use.

### push local repo into heroku 
`git push heroku master`
### Run migrations
Once your app is deployed, run migrations by running:
` heroku run python manage.py db upgrade --app name_of_your_application `
## API Reference
ALL API endpoints can be accessed via https://moviecapstonefsnd.herokuapp.com/.

Auth0 authentication require some information can be found in setup.sh.


### Error Handling
Errors are returned as JSON objects in the following format:
```bash
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

```
The API will return three error types when requests fail:
* 400: Bad Request
* 404: Resource Not Found
* 422: Not Processable

### Endpoints
GET /movies
* General :
  * returns a a list of movies objects, number of movies and a success value (It does not require any authentications)
  * Sample:
```bash
{
    "Movies": [
        {
            "genres": "WZUP2",
            "id": 5,
            "title": "WZUPMM2"
        },
        {
            "genres": "WZUP2",
            "id": 8,
            "title": "WZUPMldmsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 9,
            "title": "WZUPMldmddsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 10,
            "title": "WZUPMldmddxxsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 11,
            "title": "zzz"
        }
    ],
    "movies_count": 5,
    "success": true
}
```

GET /actors
* General: 
  * returns a list of actors object, number of actors, success value.
  * Sample:
```bash
{
    "Actors": [
        {
            "age": 3,
            "fullname": "KALID",
            "id": 3
        },
        {
            "age": 10,
            "fullname": "A222LI",
            "id": 4
        },
        {
            "age": 30,
            "fullname": "Nssossuf",
            "id": 5
        },
        {
            "age": 30,
            "fullname": "Nssozzssuf",
            "id": 6
        }
    ],
    "actors_count": 4,
    "success": true
}
```
DELETE /movies/{movie_id} (Requires Executive ROLE)
* General:
  * Takes a movie id and remove it from the database, returns a list of movies object, number of movies, delete movie id and success value.
  * Sample:
```bash
{
    "Movies": [
        {
            "genres": "WZUP2",
            "id": 8,
            "title": "WZUPMldmsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 9,
            "title": "WZUPMldmddsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 10,
            "title": "WZUPMldmddxxsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 11,
            "title": "zzz"
        }
    ],
    "deleted_movie_id": 5,
    "movies_count": 4,
    "success": true
}
```

DELETE /actors/{actor_id} (Requires EXECUTIVE or DIRECTED ROLE)
* General:
  * Takes an actor id and remove it from the database, returns a list of actors object, number of actors, delete actor id and success value
  * Sample: 
```bash
{
    "Actors": [
        {
            "age": 3,
            "fullname": "KALID",
            "id": 3
        },
        {
            "age": 10,
            "fullname": "A222LI",
            "id": 4
        },
        {
            "age": 30,
            "fullname": "Nssozzssuf",
            "id": 6
        }
    ],
    "actors_count": 3,
    "deleted_actor_id": 5,
    "success": true
}
```
POST /movies (Requires EXECUTIVE ROLE)
* General: 
  * inserts a movie into the database and returns a list of movies objects, movie_added_id, number of movies and success value.
  * Sample:
```bash
{
    "Movies": [
        {
            "genres": "WZUP2",
            "id": 5,
            "title": "WZUPMM2"
        },
        {
            "genres": "WZUP2",
            "id": 8,
            "title": "WZUPMldmsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 9,
            "title": "WZUPMldmddsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 10,
            "title": "WZUPMldmddxxsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 11,
            "title": "zzz"
        }
    ],
    "movie_added_id": 11,
    "movies_count": 5,
    "success": true
}
```
POST /actors (Requires EXECUTIVE or DIRECTED ROLE)
* General: 
  * inserts an actor into the database and returns a list of actors objects, actors_added_id, number of actors and success value.
  * Sample:
```bash
{
    "Actors": [
        {
            "age": 3,
            "fullname": "KALID",
            "id": 3
        },
        {
            "age": 10,
            "fullname": "A222LI",
            "id": 4
        },
        {
            "age": 30,
            "fullname": "Nssozzssuf",
            "id": 6
        },
        {
            "age": 10,
            "fullname": "A222zLI",
            "id": 7
        }
    ],
    "actor_added_id": 7,
    "actors_count": 4,
    "success": true
}
```
PATCH /movies/{movie_id} (Requires EXECUTIVE or DIRECTED ROLE)
* General: 
  * takes a movie id and update it with the give data and returns a list of movies objects, updated_movie_id, number of movies and success value.
  * Sample:
```bash
{
    "Movies": [
        {
            "genres": "comedy",
            "id": 8,
            "title": "TEzST"
        },
        {
            "genres": "WZUP2",
            "id": 9,
            "title": "WZUPMldmddsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 10,
            "title": "WZUPMldmddxxsldsssM2"
        },
        {
            "genres": "WZUP2",
            "id": 11,
            "title": "zzz"
        }
    ],
    "movies_count": 4,
    "success": true,
    "updated_movie_id": 8
}
```
PATCH /actors/{actor_id} (Requires EXECUTIVE or DIRECTED ROLE)
* General: 
  * takes an actor id and update it with the give data and returns a list of actors objects, updated_actor_id, number of actors and success value.
  * Sample:
```bash
{
    "Actors": [
        {
            "age": 3,
            "fullname": "KALID",
            "id": 3
        },
        {
            "age": 15,
            "fullname": "khzalid",
            "id": 4
        },
        {
            "age": 30,
            "fullname": "Nssozzssuf",
            "id": 6
        },
        {
            "age": 10,
            "fullname": "A222zLI",
            "id": 7
        }
    ],
    "actors_count": 4,
    "success": true,
    "updated_actor_id": 4
}
```
## Motivation
My motivation to build this project is to allow all users to view actors and movies withing a webpage, also allowing directors and executive to add, update and delete actors and movies.

## Authors
Saud Almutawa
