from typing import Dict, Optional

from scripts.img import find_img


class Layer:
    __path: str
    model: Optional[str]

    def __init__(self, path: str) -> None:
        super().__init__()
        self.__path = path
        self.model = None

    def load(self, data: Dict) -> None:
        self.model = data.get("model")

    def get_image(self) -> Optional[str]:
        return find_img(self.__path)
