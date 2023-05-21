import asyncio
import logging
import os

from modules import script_callbacks, scripts
from modules.paths import models_path
from scripts.db.pose_db import PoseDB
from scripts.ui import on_ui_tabs

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

script_callbacks.on_ui_tabs(on_ui_tabs)
