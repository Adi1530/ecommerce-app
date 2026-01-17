

from backend.domains.schemas.user_process import UserCreate
from backend.domains.services.user_services import create_user, authenticate_user
from backend.tests.base import BaseTestCase

class TestUserService(BaseTestCase):

    def test_create_and_authenticate_user(self):
        user_data = UserCreate(

            email = "test@gmail.com",
            password = "test"
        )

        user = create_user(self.db, user_data)
        self.assertEqual(user.email, user_data.email)

        auth_user = authenticate_user(
            self.db,
            user_data.email,
            user_data.password
        )

        self.assertIsNotNone(auth_user)