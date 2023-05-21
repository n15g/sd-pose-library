import os.path
from unittest import TestCase

from assertpy import assert_that

from scripts.db.package import Package
from tests import test_resources


class TestPackage(TestCase):
    def test_load(self):
        path = os.path.join(test_resources, "db", "test_package")
        pkg = Package(path)

        assert_that(pkg.key).is_equal_to("test_package")
        assert_that(pkg.name).is_equal_to("Test Package")
        assert_that(pkg.source).is_equal_to("https://github.com/n15g/sd-pose-library")

    def test_load_no_meta(self):
        path = os.path.join(test_resources, "db", "no_meta")
        pkg = Package(path)

        assert_that(pkg.key).is_equal_to("no_meta")
        assert_that(pkg.name).is_equal_to("no_meta")
        assert_that(pkg.source).is_equal_to("")

    def test_load_partial_meta(self):
        path = os.path.join(test_resources, "db", "partial_meta")
        pkg = Package(path)

        assert_that(pkg.key).is_equal_to("partial_meta")
        assert_that(pkg.name).is_equal_to("Partial Meta")
        assert_that(pkg.source).is_equal_to("")

    def test_load_poses(self):
        path = os.path.join(test_resources, "db", "test_package")
        pkg = Package(path)

        assert_that(pkg.poses).is_length(3)
