from flask import Response, request
from database.models import Movie
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, UpdatingMovieError, DeletingMovieError, MovieNotExistsError
from pymongo.errors import DuplicateKeyError
import logging



logger = logging.getLogger(__name__)


class MoviesApi(Resource):
    @jwt_required
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            movie = Movie(**body).save()
            id = movie.id
            logger.info('MoviesApi -- Movie saved successfully')
            return {'id': str(id)}, 200
        except NotUniqueError:
            logger.error('MoviesApi -- Movie error occured.')
            return {
                "message": "Movie with given name already exists",
                "status": 400
            }


class MovieApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return '', 200

    @jwt_required
    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)
