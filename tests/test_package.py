from unittest import TestCase

from assertpy import assert_that

from scripts.package import Package


class TestPackage(TestCase):
    def test_load(self):
        pkg = Package("db/test_package")

        assert_that(pkg.key).is_equal_to("test_package")
        assert_that(pkg.name).is_equal_to("Test Package")
        assert_that(pkg.source).is_equal_to("https://github.com/n15g/sd-pose-library")

    def test_load_no_meta(self):
        pkg = Package("db/no_meta")

        assert_that(pkg.key).is_equal_to("no_meta")
        assert_that(pkg.name).is_equal_to("no_meta")
        assert_that(pkg.source).is_equal_to("")

    def test_load_partial_meta(self):
        pkg = Package("db/partial_meta")

        assert_that(pkg.key).is_equal_to("partial_meta")
        assert_that(pkg.name).is_equal_to("Partial Meta")
        assert_that(pkg.source).is_equal_to("")
