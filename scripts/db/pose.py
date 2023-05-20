import json
import logging
import os.path
from typing import List, Dict, Optional

from scripts.db.layer import Layer
from scripts.img import find_img

log = logging.getLogger("sd")


class Pose:
    __path: str
    key: str
    title: str
    tags: List[str]
    layers: List[Layer]

    def __init__(self, path: str) -> None:
        super().__init__()
        self.__path = path
        self.key = os.path.basename(path)
        self.title = ""
        self.tags = []
        self.layers = []
        self.__load_meta()

    @staticmethod
    def __get_layer_path(path: str, index: int) -> str:
        return f"{path}.{index}"

    def __load_meta(self) -> None:
        meta_path = self.__path + ".pose"

        try:
            with open(meta_path, "r") as meta_json:
                meta: dict = json.load(meta_json)
        except Exception as e:
            log.warning(f"Failed to load [{meta_path}]", exc_info=e)
            return

        self.title = meta.get("title", self.key)
        self.tags = meta.get("tags", [])
        self.__load_layers(meta.get("layers", []))

    def __load_layers(self, layers_list: List[Dict]) -> None:
        for i, layer_dict in enumerate(layers_list):
            layer = Layer(self.__get_layer_path(self.__path, i))
            layer.load(layer_dict)
            self.layers.append(layer)

    def get_image(self) -> Optional[str]:
        return find_img(self.__path)
