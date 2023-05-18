from unittest import TestCase
from assertpy import assert_that
from scripts import fs
import os
import tempfile


class TestFs(TestCase):
    def test_bootstrap(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            db_path = os.path.join(tmp_path, "test-db")
            assert_that(db_path).does_not_exist()

            bootstrap_path = os.path.abspath(os.path.join("..", "bootstrap"))
            print(db_path)
            print(bootstrap_path)

            fs.bootstrap(db_path, bootstrap_path)
            assert_that(db_path).exists()

            print(os.listdir(db_path))
            assert_that(os.path.join(db_path, "built-in", "package-info.json")).exists()
