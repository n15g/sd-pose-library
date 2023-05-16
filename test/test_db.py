import os
from unittest import TestCase

from assertpy import assert_that
import tempfile

from scripts.db import DB
from scripts.pose_library import PoseLibrary


class TestDB(TestCase):
    def test_clear(self):
        db = DB()
        assert_that(db.is_empty()).is_true()

        db.add_library(PoseLibrary("blah", "Blah"))
        assert_that(db.is_empty()).is_false()

        db.clear()
        assert_that(db.is_empty()).is_true()
