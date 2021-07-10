import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies



class capstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""
    def setUp(self):

        self.app = create_app()
        self.Executive_Token =os.getenv('EXECUTIVE_ROLE_TOKEN')
        self.Directed_Token = os.getenv('DIRECTED_ROLE_TOKEN')
        self.client = self.app.test_client
        self.database_path = "postgresql://postgres:9048@localhost:5432/capstone_test"
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        
        
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_movies_with_EXECUTIVE_authorization(self):
        res = self.client().post('/movies', json={"title":"testing222233", "genres":"TEST2223"}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_403error_post_movies_with_DIRECTED_authorization(self):
        res = self.client().post('/movies', json={"title":"testing32323", "genres":"TEST22323"}, headers={
            "Authorization": 'bearer '+ self.Directed_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_400error_post_movies_with_emptyTITLE(self):
        res = self.client().post('/movies', json={"title":"", "genres":"TEST2"}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_post_actors(self):
        res = self.client().post('/actors', json={"fullname":"Khalmfkdfkmfied", "age":50}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_400error_post_actors(self):
        res = self.client().post('/actors', json={"fullname":"", "age":50}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_update_movies(self):
        res = self.client().patch('/movies/6', json={"title":"CHAkwmdkwmdD", "genres":"DRAsdsdMA"}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
    
    def test_422error_update_movies(self):
        res = self.client().patch('/movies/7', json={"title":"", "genres":"DRAMA"}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_update_actors(self):
        res = self.client().patch('/actors/3', json={"fullname":"SAAAARA", "age":20}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_422error_update_actors(self):
        res = self.client().patch('/actors/3', json={"fullname":"", "age":20}, headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_delete_movies_EXECUTIVE_ROLE(self):
        res = self.client().delete('/movies/6', headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_403error_delete_movies_DIRECTED_ROLE(self):
        res = self.client().delete('/movies/9', headers={
            "Authorization": 'bearer '+ self.Directed_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_delete_actors(self):
        res = self.client().delete('/actors/3', headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404error_delete_actors(self):
        res = self.client().delete('/actors/30', headers={
            "Authorization": 'bearer '+ self.Executive_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

if __name__ == "__main__":
    unittest.main()