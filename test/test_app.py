import unittest
from app import app
from drop_tables import drop
from create_tables import create
from database import User, Pixels
from flask import jsonify

t_app = app
t_app.config["TESTING"] = True

class TestApi(unittest.TestCase):

    def setUp(self) -> None:
        drop()
        create()

    def test_default(self):
        with t_app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

    def test_home(self):
        with t_app.test_client() as c:
            resp = c.get('/home')
            self.assertEqual(resp.status_code, 200)

    def test_profile(self):
        user = User.create(username='test', password='password')
        with t_app.test_client() as c:
            resp = c.get('/profile/test')
            self.assertEqual(resp.status_code, 200)

    def test_login(self):
        user = User.create(username='test', password='password')
        data2 = {'username': 'new_user', 'password': 'P@ssw0rd'}
        data3 = {'username': 'test', 'password': 'password'}
        with t_app.test_client() as c:
            resp = c.post('/login')
            self.assertEqual(resp.status_code, 400)
            resp = c.post('/login', data=data2)
            self.assertEqual(resp.status_code, 400)
            resp = c.post('/login', data=data3)
            self.assertRaises(ValueError)
            resp = c.get('/login')
            self.assertEqual(resp.status_code, 200)

    def test_register(self):
        user = User.create(username='test', password='password')
        data = {'new_username':'newuser', 'new_password':'P@ssw0rd', 'v_password':'P@ssw0rd'}
        data2 = {'new_username':'newuser', 'new_password':'password'}
        data3 = {'new_username': 'test', 'new_password': 'P@ssw0rd'}
        with t_app.test_client() as c:
            resp = c.post('/register', data=data)
            self.assertEqual(resp.status_code, 302)
            resp = c.post('/register', data=data2)
            self.assertEqual(resp.status_code, 400)
            resp = c.post('/register', data=data3)
            self.assertEqual(resp.status_code, 400)
            resp = c.get('/register')
            self.assertEqual(resp.status_code, 200)

    def test_store_pixels(self):
        data = {'pixel': 'black', 'pixel2': 'black'}
        data2 = {'pixel': 'white', 'pixel2': None}
        with t_app.test_client() as c:
            resp = c.post('/canvas/test_user', json=data)
            self.assertEqual(resp.status_code, 200)
            resp = c.post('/canvas/test_user', json=data2)
            self.assertEqual(resp.status_code, 400)

    def test_get_pixels(self):
        pixel = Pixels.insert(user_id='test', pixel='A011', color='black').execute()
        with t_app.test_client() as c:
            resp = c.get('/canvas/test')
            self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
