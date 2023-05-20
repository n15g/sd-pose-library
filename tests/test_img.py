import os.path
from unittest import TestCase

from assertpy import assert_that

from scripts.img import find_img
from tests import test_resources


class TestImg(TestCase):
    def test_get_png(self) -> None:
        path = os.path.join(test_resources, "test_png")
        assert_that(find_img(path)).is_equal_to(
            os.path.join(test_resources, "test_png.png")
        )

    def test_get_jpg(self) -> None:
        path = os.path.join(test_resources, "test_jpg")
        assert_that(find_img(path)).is_equal_to(
            os.path.join(test_resources, "test_jpg.jpg")
        )

    def test_get_jpeg(self) -> None:
        path = os.path.join(test_resources, "test_jpeg")
        assert_that(find_img(path)).is_equal_to(
            os.path.join(test_resources, "test_jpeg.jpeg")
        )

    def test_get_webp(self) -> None:
        path = os.path.join(test_resources, "test_webp")
        assert_that(find_img(path)).is_equal_to(
            os.path.join(test_resources, "test_webp.webp")
        )