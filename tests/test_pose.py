import os.path
from unittest import TestCase

from assertpy import assert_that

from scripts.pose import Pose


class TestPose(TestCase):
    def test_xmas_tree(self):
        pose = Pose(os.path.join("db", "test_package", "xmas"))

        assert_that(pose.key).is_equal_to("xmas")
        assert_that(pose.title).is_equal_to("Christmas Tree Payload")
        assert_that(pose.tags).contains("waving", "depth map")
