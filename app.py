import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS

from auth import AuthError, requires_auth
from models import setup_db, Movies, Actors


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return jsonify({
            "success": "TEST"
        })

    @app.route('/movies')
    def get_movies():
        try:
            movies = Movies.query.order_by(Movies.id).all()
            movies_list = []

            if not movies:
                abort(404)

            for movie2 in movies:
                # appending movies in good format in a list of movies (instead of using __repr__ method)
                movies_list.append(movie2.format())

            return jsonify({
                "success": True,
                "Movies": movies_list,
                "movies_count": len(movies)
            })
        except:
            abort(404)

    @app.route('/actors')
    def get_actors():

        actors = Actors.query.order_by(Actors.id).all()

        if not actors:
            abort(404)

        actors_list = []
        for actor2 in actors:
            actors_list.append(actor2.format())

        return jsonify({
            'success': True,
            'Actors': actors_list,
            'actors_count': len(actors)
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):
        try:
            body = request.get_json()
            new_title = body.get('title', None)
            new_genres = body.get('genres', None)

            if not new_title:
                abort(400)

            if not new_genres:
                abort(400)

            movie = Movies(title=new_title, genres=new_genres)
            movie.insert()
            movies = Movies.query.order_by(Movies.id).all()
            movies_list = []

            for movie2 in movies:
                movies_list.append(movie2.format())

            return jsonify({
                'success': True,
                'Movies': movies_list,
                'movie_added_id': movie.id,
                'movies_count': len(movies)
            })
        except:
            abort(400)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(payload):
        try:
            body = request.get_json()
            new_fullname = body.get('fullname', None)
            new_age = body.get('age', None)
            if not new_fullname:
                abort(400)

            if new_age is None:
                abort(400)

            actor = Actors(fullname=new_fullname, age=new_age)
            actor.insert()
            actors = Actors.query.order_by(Actors.id).all()
            actors_list = []

            for actor2 in actors:
                actors_list.append(actor2.format())

            return jsonify({
                'success': True,
                'Actors': actors_list,
                'actor_added_id': actor.id,
                'actors_count': len(actors)
            })
        except:
            abort(400)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movies(payload, id):
        try:

            movie = Movies.query.filter(Movies.id == id).one_or_none()

            if movie is None:
                abort(404)

            body = request.get_json()
            new_title = body.get('title', None)
            new_genres = body.get('genres', None)

            if not new_title:
                abort(400)

            if not new_genres:
                abort(400)

            movie.title = new_title
            movie.genres = new_genres
            movie.update()

            movies = Movies.query.order_by(Movies.id).all()
            movies_list = []

            for movie2 in movies:
                movies_list.append(movie2.format())

            return jsonify({
                'success': True,
                'Movies': movies_list,
                'updated_movie_id': movie.id,
                'movies_count': len(movies)
            })
        except:
            abort(422)

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actors(payload, id):
        try:
            body = request.get_json()
            actor = Actors.query.filter(Actors.id == id).one_or_none()

            if actor is None:
                abort(404)

            new_fullname = body.get('fullname', None)
            new_age = body.get('age', None)

            if not new_fullname:
                abort(400)

            if new_age is None:
                abort(400)

            actor.fullname = new_fullname
            actor.age = new_age
            actor.update()

            actors = Actors.query.order_by(Actors.id).all()
            actors_list = []

            for actor2 in actors:
                actors_list.append(actor2.format())

            return jsonify({
                'success': True,
                'Actors': actors_list,
                'updated_actor_id': actor.id,
                'actors_count': len(actors)
            })
        except:
            abort(422)

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movies.query.filter(Movies.id == id).one_or_none()

            if not movie:
                abort(404)

            movie.delete()
            movies = Movies.query.order_by(Movies.id).all()
            movies_list = []

            for movie2 in movies:
                movies_list.append(movie2.format())
            return jsonify({
                'success': True,
                'Movies': movies_list,
                'deleted_movie_id': movie.id,
                'movies_count': len(movies)
            })
        except:
            abort(400)

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            actor = Actors.query.filter(Actors.id == id).one_or_none()

            if not actor:
                abort(404)

            actor.delete()
            actors = Actors.query.order_by(Actors.id).all()
            actors_list = []

            for actor2 in actors:
                actors_list.append(actor2.format())

            return jsonify({
                'success': True,
                'Actors': actors_list,
                'deleted_actor_id': actor.id,
                'actors_count': len(actors)
            })
        except:
            abort(404)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "unprocessable"
        }), 422

    @app.errorhandler(AuthError)
    def authError(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code

    return app


app = create_app()
if __name__ == '__main__':
    app.run()
