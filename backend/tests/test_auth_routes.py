from backend.tests.base import BaseTestCase


class TestAuthRoutes(BaseTestCase):

    def test_register_and_login(self):
        payload = {"email": "test@gmail.com", "password": "test"}

        r = self.client.post("/auth/register", json=payload)
        self.assertEqual(r.status_code, 200)

        r = self.client.post("/auth/login", json=payload)
        self.assertEqual(r.status_code, 200)
        self.assertIn("access_token", r.json())
