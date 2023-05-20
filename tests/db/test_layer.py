import json
import os.path
from unittest import TestCase

from assertpy import assert_that

from scripts.db.layer import Layer
from tests import test_resources


def load_layer(pose_path: str, index: int) -> Layer:
    with open(pose_path + ".pose", "r") as meta_json:
        meta: dict = json.load(meta_json)

    layer = Layer(pose_path + f".{index}")
    layer.load(meta["layers"][index])
    return layer


class TestLayer(TestCase):

    def test_load(self):
        pose_path = os.path.join(test_resources, "db", "test_package", "xmas")
        layer = load_layer(pose_path, 0)

        assert_that(layer.model).is_equal_to("openpose")
        assert_that(layer.get_image()).ends_with("png")

    def test_minimal(self):
        pose_path = os.path.join(test_resources, "db", "test_package", "minimal")
        layer = load_layer(pose_path, 0)

        assert_that(layer.model).is_none()
        assert_that(layer.get_image()).is_none()
