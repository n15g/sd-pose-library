import json
import logging
import os.path
from typing import List

log = logging.getLogger("sd")


class Pose:
    __path: str
    key: str
    title: str
    tags: List[str]
    layers: List['Layer']

    def __init__(self, path: str) -> None:
        super().__init__()
        self.__path = path
        self.key = os.path.basename(path)
        self.title = ""
        self.tags = []
        self.__load_meta()

    def __load_meta(self) -> None:
        meta_path = self.__path + ".pose"

        try:
            with open(meta_path, "r") as meta_json:
                meta: dict = json.load(meta_json)
        except Exception as e:
            log.error(f"Failed to load [{meta_path}]", exc_info=e)
            return

        self.title = meta.get("title", self.key)
        self.tags = meta.get("tags", [])

    class Layer:
        model: str

        def __init__(self) -> None:
            super().__init__()
