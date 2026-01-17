import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from backend.domains.main import app
from backend.domains.core.database import Base
from backend.domains.core.config import settings


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        cls.client= TestClient(app)

    def setUp(self):
        self.db= TestingSessionLocal()

    def tearDown(self):
        self.db.rollback()
        self.db.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)
