import asyncio
import logging
import os
import shutil
from typing import Optional, List, Callable

from scripts.db.package import Package

log = logging.getLogger(__name__)
BOOTSTRAP_PATH = os.path.join(os.path.dirname(__file__), "bootstrap")


class PoseDB:
    __db_path: str
    __packages: dict[str, Package]
    __loaded: bool
    __load_observers: list[Callable[['PoseDB'], None]]

    def __init__(self, db_path: str) -> None:
        super().__init__()
        self.__db_path = db_path
        self.__packages = dict()
        self.__loaded = False
        self.__load_observers = list()

        if not os.path.exists(self.__db_path):
            log.info(f"Creating db directory. {self.__db_path}")
            os.mkdir(self.__db_path)

    def __getitem__(self, key):
        return self.__packages[key]

    def is_empty(self) -> bool:
        return len(self.__packages) == 0

    async def load(self) -> None:
        self.__bootstrap()
        self.__packages = dict()
        tasks = [self.__load_package(pkg) for pkg in os.listdir(self.__db_path)]
        results: List[Package] = await asyncio.gather(*tasks)
        packages = filter(lambda x: x is not None, results)

        for pkg in packages:
            self.__packages[pkg.key] = pkg

        self.__loaded = True
        for observer in self.__load_observers:
            observer(self)

    def on_load(self, cb: Callable[['PoseDB'], None]) -> None:
        self.__load_observers.append(cb)
        if self.__loaded:
            cb(self)

    async def __load_package(self, key: str) -> Optional[Package]:
        path = os.path.join(self.__db_path, key)
        if not os.path.isdir(path):
            log.warning(f"Skipping non-package in pose db [{path}]")
            return None
        pkg = Package(path)
        return pkg

    def __bootstrap(self) -> None:
        if len(os.listdir(self.__db_path)) == 0:
            log.info("Bootstrapping empty database.")
            shutil.copytree(BOOTSTRAP_PATH, self.__db_path, dirs_exist_ok=True)
