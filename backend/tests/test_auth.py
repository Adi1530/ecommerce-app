
from backend.tests.base import BaseTestCase
from backend.domains.core.auth import create_access_token
from backend.domains.core.config import settings
from jose import jwt

class TestAuth(BaseTestCase):

    def test_create_access_token(self):
        token = create_access_token({"sub" : "testcase@gmail.com"})

        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        self.assertEqual(decoded["sub"], "testcase@gmail.com")