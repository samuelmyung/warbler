"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from app import app
import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError


from models import db, User, Message, Follow

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class MessageModelTestCase(TestCase):
    def setUp(self):
        Message.query.delete()

        msg = Message(
            text="message",
            timestamp="2024-03-08 12:00:00",
            user_id="u1")

        db.session.commit()
        self.msg_id = msg.id
        self.msg = msg

    def tearDown(self):
        db.session.rollback()

    def test_msg_instance(self):
        self.assertIsInstance(self.msg, Message)

    def test_msg_text_msg_user(self):
        msg = Message.query.get(self.msg)
        u1 = User.signup("u1", "u1@email.com", "password", None)

        self.assertIn(u1.messages, msg)
