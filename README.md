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
  * ` curl http://127.0.0.1:5000/movies ` Sample:
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
  * ` curl http://127.0.0.1:5000/actors ` Sample:
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
  * ` curl http://127.0.0.1:5000/movies/5 -X DELETE ` Sample:
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

DELETE /actors (Require EXECUTIVE or DIRECTED ROLE)
* General:
  * Takes an actor id and remove it from the database, returns a list of actors object, number of actors, delete actor id and success value
  * ` curl http://127.0.0.1:5000/actors/5 -X DELETE `
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
  * inserts a movie into the database 
  * ` curl http://127.0.0.1:5000/categories/4/questions '
```bash
{
  "current_category": null,
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```
POST /quizzes
* General:
  * Takes a quiz category and previous questions list and returns a success value and random question object that's not in the list
  * ` curl http:127.0.0.1:5000/quizzes -X POST -H "Content-Type:application/json" -d '{"quiz_category":{"type":"art","id":2},"previous_questions":[]}' `
```bash
{
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    },
```
## Deployment N/A
## Authors
Saud Almutawa
## Acknowledgements
Udacity team and ME (:
