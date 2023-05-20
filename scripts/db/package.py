import json
import logging
import os
from typing import Optional

log = logging.getLogger("sd")


class Package:
    __path: str
    key: str
    name: Optional[str] = ""
    source: Optional[str] = ""

    def __init__(self, path: str) -> None:
        super().__init__()
        self.__path = path
        self.key = os.path.basename(self.__path)
        self.name = self.key
        self.__load_meta()

    def __load_meta(self) -> None:
        log.info(f"Loading package [{self.__path}]")
        meta_path = os.path.join(self.__path, "_meta.json")
        if not os.path.exists(meta_path):
            return

        try:
            with open(meta_path, "r") as meta_json:
                meta: dict = json.load(meta_json)
        except Exception as e:
            log.error(f"Failed to load [{meta_path}]", exc_info=e)
            return

        self.name = meta.get("name", self.key)
        self.source = meta.get("source", "")
