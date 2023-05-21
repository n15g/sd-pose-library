import glob
import json
import logging
import os
from typing import Optional, List

from scripts.db.pose import Pose

POSE_GLOB = "*.pose"

log = logging.getLogger(__name__)


class Package:
    __path: str
    key: str
    name: Optional[str] = ""
    source: Optional[str] = ""
    poses: List[Pose]

    def __init__(self, path: str) -> None:
        super().__init__()
        self.__path = path
        self.key = os.path.basename(self.__path)
        self.name = self.key
        self.__load_meta()
        self.poses = []
        self.__load_poses()

    def __load_meta(self) -> None:
        log.info(f"Loading package [{self.__path}]")
        meta_path = os.path.join(self.__path, "_meta.json")

        try:
            with open(meta_path, "r") as meta_json:
                meta: dict = json.load(meta_json)
        except Exception as e:
            log.warning(f"Failed to load [{meta_path}]", exc_info=e)
            return

        self.name = meta.get("name", self.key)
        self.source = meta.get("source", "")

    def __load_poses(self) -> None:
        paths = glob.glob(os.path.join(self.__path, POSE_GLOB))
        for path in paths:
            pose = Pose(path)
            self.poses.append(pose)
