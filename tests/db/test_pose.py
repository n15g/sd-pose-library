import os.path
from unittest import TestCase

from assertpy import assert_that

from scripts.db.pose import Pose
from tests import test_resources


class TestPose(TestCase):
    def test_xmas_tree(self):
        path = os.path.join(test_resources, "db", "test_package", "xmas")
        pose = Pose(path)

        assert_that(pose.key).is_equal_to("xmas")
        assert_that(pose.title).is_equal_to("Christmas Tree Payload")
        assert_that(pose.tags).contains("waving", "depth map", "normal map")

        assert_that(pose.layers).is_length(4)

        assert_that(pose.layers[0].model).is_equal_to("openpose")
        assert_that(pose.layers[1].model).is_equal_to("depth")
        assert_that(pose.layers[2].model).is_equal_to("normal")
        assert_that(pose.layers[3].model).is_equal_to("canny")

    def test_get_img(self):
        path = os.path.join(test_resources, "db", "test_package", "xmas")
        pose = Pose(path)
        assert_that(pose.get_image()).ends_with("xmas.png")

    def test_get_img_when_no_img(self):
        path = os.path.join(test_resources, "db", "test_package", "minimal")
        pose = Pose(path)
        assert_that(pose.get_image()).is_none()

    def test_missing_meta(self):
        path = os.path.join(test_resources, "db", "invalid")
        pose = Pose(path)
        assert_that(pose.title).is_equal_to("")
