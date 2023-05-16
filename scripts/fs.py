import logging
import os
import shutil

log = logging.getLogger("sd")


def bootstrap(db_path: str, bootstrap_path: str) -> None:
    if not os.path.exists(db_path):
        log.info(f"Creating db directory. {db_path}")
        os.mkdir(db_path)

    if len(os.listdir(db_path)) == 0:
        log.info(f"Bootstrapping empty database.")
        shutil.copytree(bootstrap_path, db_path, dirs_exist_ok=True)
