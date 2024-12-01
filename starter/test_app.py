import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor
from config import Variables


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):

        self.casting_assistant = Variables.Casting_Assistant_Token
        self.casting_director = Variables.Casting_Director_Token
        self.producer = Variables.Executive_Producer_Token

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = Variables.DATABASE_PATH
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.movie = {
            'title': "The Killer",
            'release_year': 2024
        }

        self.actor = {
            "name": "Camavinga",
            "age": 45,
            "gender": 'M',
            "movie_id": 2
        }
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    def test_get_movies_200(self):
        """Test get movies - 200
        """
        header_obj = {
            'Authorization': "Bearer {}".format(self.casting_assistant)
        }
        res = self.client().get('/movies', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)
        self.assertEqual(type(data["movies"]), type([]))

    def test_get_movies_404(self):
        """Test get movies - 404
        """
        header_obj = {
            'Authorization': "Bearer {}".format(self.casting_assistant)
        }
        res = self.client().get('/movies', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_actors_200(self):
        header_obj = {
            'Authorization': "Bearer {}".format(self.casting_assistant)
        }
        res = self.client().get('/actors', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["actors"]), type([]))

    def test_get_actors_by_director_200(self):
        header_obj = {
            'Authorization': "Bearer {}".format(self.producer)
        }
        res = self.client().get('/actors', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["actors"]), type([]))

    def test_get_actor_fail_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(type(data["message"]), type(""))

    def test_create_movies(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.producer)
        }
        res = self.client().post(f'/movies',
                                 json=self.movie, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_movies_fail_400(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.producer)
        }
        movie_fail = {"title": "Movie"}
        res = self.client().post(f'/movies',
                                 json=movie_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], "Missing field for Movie")

    def test_create_movies_fail_403(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        movie_fail = {"title": "Movie"}
        res = self.client().post(f'/movies',
                                 json=movie_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_create_actors(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        res = self.client().post(f'/actors',
                                 json=self.actor, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_actors_fail_400(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        actor_fail = {"name": "Actor"}
        res = self.client().post(f'/actors',
                                 json=actor_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], "Bad request")


    def test_delete_movie(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.producer)
        }
        delete_id_movie = 1
        res = self.client().delete(
            f'/movies/{delete_id_movie}',
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], delete_id_movie)

        res = self.client().get('/movies', headers=header_obj)
        m_data = json.loads(res.data)

        found_deleted = False

        for m in m_data["movies"]:
            if m["id"] == delete_id_movie:
                found_deleted = True
                break

        self.assertFalse(found_deleted)

    def test_delete_movie_fail_404(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.producer)
        }
        m_id = 100
        res = self.client().delete(f'/movies/{m_id}', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_delete_movie_fail_403(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        m_id = 3
        res = self.client().delete(f'/movies/{m_id}', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_delete_actor(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        delete_id_actor = 1
        res = self.client().delete(
            f'/actors/{delete_id_actor}',
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], delete_id_actor)

        res = self.client().get('/actors', headers=header_obj)
        a_data = json.loads(res.data)

        found_deleted = False

        for a in a_data["actors"]:
            if a["id"] == delete_id_actor:
                found_deleted = True
                break

        self.assertFalse(found_deleted)

    def test_delete_actor_fail_404(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        a_id = -100
        res = self.client().delete(f'/actors/{a_id}', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_delete_actor_fail_403(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_assistant)
        }
        a_id = 100
        res = self.client().delete(f'/actors/{a_id}', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])


    def test_update_movie(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.producer)
        }
        update_id_movie = 2
        new_title = "Eyvah eyvah 2"
        res = self.client().patch(
            f'/movies/{update_id_movie}',
            json={
                'title': new_title},
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['updated']['id'], update_id_movie)
        self.assertEqual(data['updated']['title'], new_title)

    def test_update_movie_fail_404(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        update_id_movie = -100
        res = self.client().patch(
            f'/movies/{update_id_movie}',
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_update_actor(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        update_id_actor = 2
        new_name = "Tom Hanks"
        new_age = 54
        res = self.client().patch(
            f'/actors/{update_id_actor}',
            json={
                'name': new_name,
                'age': new_age},
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['updated']['id'], update_id_actor)
        self.assertEqual(data['updated']['name'], new_name)
        self.assertEqual(data['updated']['age'], new_age)

    def test_update_actor_fail_404(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_director)
        }
        update_id_actor = 100
        res = self.client().patch(
            f'/actors/{update_id_actor}',
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_update_actor_fail_403(self):
        header_obj = {
            "Authorization": "Bearer {}".format(self.casting_assistant)
        }
        update_id_actor = 100
        res = self.client().patch(
            f'/actors/{update_id_actor}',
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()