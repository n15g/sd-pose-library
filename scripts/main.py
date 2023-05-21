import asyncio
import logging
import os

import gradio as gr

from modules import script_callbacks, scripts
from modules.paths import models_path
from scripts.db.pose_db import PoseDB
from scripts.ui_library import UILibrary

log = logging.getLogger(__name__)

extension_path = scripts.basedir()
db_path = os.path.join(models_path, "pose-db")
bootstrap_path = os.path.join(scripts.basedir(), "bootstrap")

log.info("SD Pose Library")
log.info(f"Extension directory [{extension_path}]")
log.info(f"Data directory [{db_path}]")

db = PoseDB(db_path)


async def load_db() -> None:
    await db.load()


asyncio.run(load_db())

library_ui = UILibrary(db)


def on_db_update():
    library_ui.update_package_list()


db.on_load(on_db_update)


def on_ui_tabs() -> list[tuple[gr.Blocks, str, str]]:
    with gr.Blocks(elem_classes="sdpl_main") as pose_library_tab:
        library_ui.create_view()
    return [(pose_library_tab, "Pose Library", "poselib_tab")]


script_callbacks.on_ui_tabs(on_ui_tabs)
