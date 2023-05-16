import logging
import os

from modules import script_callbacks, scripts
from modules.paths import models_path
from scripts import fs
from scripts.ui import on_ui_tabs

log = logging.getLogger("sd")

extension_path = scripts.basedir()
db_path = os.path.join(models_path, "pose-db")
bootstrap_path = os.path.join(scripts.basedir(), "bootstrap")

log.info(f"SD Pose Library")
log.info(f"Extension directory [{extension_path}]")
log.info(f"Data directory [{db_path}]")

fs.bootstrap(db_path, bootstrap_path)

script_callbacks.on_ui_tabs(on_ui_tabs)
