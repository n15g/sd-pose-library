import json
import logging
import os.path
from typing import List, Dict, Optional

from scripts.db.layer import Layer
from scripts.img import find_img

log = logging.getLogger(__name__)


class Pose:
    __path: str
    __base_path: str
    key: str
    title: str
    tags: List[str]
    layers: List[Layer]

    def __init__(self, path: str) -> None:
        super().__init__()
        self.__path = path
        self.__base_path = self.__get_base_path(path)
        self.key = os.path.basename(self.__base_path)
        self.title = ""
        self.tags = []
        self.layers = []
        self.__load_meta()

    @staticmethod
    def __get_layer_path(path: str, index: int) -> str:
        return f"{path}.{index}"

    @staticmethod
    def __get_base_path(path: str) -> str:
        return os.path.splitext(path)[0]

    def __load_meta(self) -> None:
        try:
            with open(self.__path, "r") as meta_json:
                meta: dict = json.load(meta_json)
        except Exception as e:
            log.warning(f"Failed to load [{self.__path}]", exc_info=e)
            return

        self.title = meta.get("title", self.key)
        self.tags = meta.get("tags", [])
        self.__load_layers(meta.get("layers", []))

    def __load_layers(self, layers_list: List[Dict]) -> None:
        for i, layer_dict in enumerate(layers_list):
            layer = Layer(self.__get_layer_path(self.__base_path, i))
            layer.load(layer_dict)
            self.layers.append(layer)

    def get_image(self) -> Optional[str]:
        return find_img(self.__base_path)
