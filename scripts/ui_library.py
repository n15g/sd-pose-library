import logging

import gradio as gr
from PIL import Image

from scripts.db.pose_db import PoseDB

log = logging.getLogger(__name__)


class UILibrary:
    __db: PoseDB
    __package_dropdown: gr.Dropdown = None
    __gallery: gr.Gallery = None
    view: gr.Blocks

    def __init__(self, db: PoseDB) -> None:
        super().__init__()
        self.__db = db

    def create_view(self) -> gr.Blocks:
        with gr.Column(elem_classes="sdpl_library") as view:
            self.__package_dropdown = gr.Dropdown()
            self.__gallery = gr.Gallery(type="pil")

            self.update_package_list()
            self.__package_dropdown.change(
                fn=self.__on_select_package,
                inputs=self.__package_dropdown,
                outputs=self.__gallery
            )

        return view

    def __get_package_list(self) -> list[str]:
        return list(self.__db.keys())

    def update_package_list(self):
        if self.__package_dropdown is not None:
            package_list = self.__get_package_list()
            selected = package_list[0] if len(package_list) > 0 else None
            self.__package_dropdown.choices = package_list
            self.__package_dropdown.value = selected

    def __on_select_package(self, key: str) -> list[Image]:
        pkg = self.__db[key]
        paths = list(map(lambda pose: pose.get_image(), pkg.poses))
        images = []
        for path in paths:
            try:
                img = Image.open(path)
                images.append(img)
            except Exception as e:
                log.error(f"Failed to load image [{path}]", exc_info=e)
        return images
