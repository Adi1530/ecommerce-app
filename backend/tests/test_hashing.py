from backend.domains.core.hashing import hash_password, verify_password
from backend.tests.base import BaseTestCase


class TestHashing(BaseTestCase):

    def test_hashing(self):
        password = "test_secret@123"
        hashed_password = hash_password(password)

        self.assertNotEqual(password, hashed_password)
        self.assertTrue(verify_password(password, hashed_password))
