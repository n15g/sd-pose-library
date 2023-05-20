import os
import tempfile
from unittest import IsolatedAsyncioTestCase

from assertpy import assert_that

from scripts.db.pose_db import PoseDB
from tests import test_resources


class TestDB(IsolatedAsyncioTestCase):
    def test_create_dir(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            db_path = os.path.join(tmp_path, "test-db")
            assert_that(db_path).does_not_exist()

            PoseDB(db_path)
            assert_that(db_path).exists()

    def test_is_empty(self):
        with tempfile.TemporaryDirectory() as db_path:
            db = PoseDB(db_path)
            assert_that(db.is_empty()).is_true()

    async def test_bootstrap(self):
        with tempfile.TemporaryDirectory() as db_path:
            db = PoseDB(db_path)

            bootstrap_path = os.path.join(test_resources, "db")

            await db.bootstrap(bootstrap_path)

            assert_that(db_path).exists()

    async def test_load(self):
        db = PoseDB(os.path.join(test_resources, "db"))
        await db.load()

        assert_that(db["no_meta"]).is_not_none()
        assert_that(db["test_package"]).is_not_none()
