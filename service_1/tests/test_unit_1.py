from flask_testing import TestCase
from flask import url_for
from requests_mock import mock
from service_1.application import app


class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service-2:5000/get/weapon', text='Sword')
            m.get('http://service-3:5000/get/damage', json=15)
            m.post('http://service-4:5000/post/status', json={
                "name": "Sharp",
                "level": "Adept",
                "effect": "Fire"
            })

            response = self.client.get(url_for('index'))


        self.assert200(response)
        self.assertIn("It is called the Adept Sharp Sword of Fire", response.data.decode())