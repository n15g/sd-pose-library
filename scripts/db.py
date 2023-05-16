from scripts.pose_library import PoseLibrary


class DB:
    __db_dir: str
    __libraries: dict[str, PoseLibrary]

    def __init__(self) -> None:
        super().__init__()
        self.__libraries = dict()

    def clear(self) -> None:
        self.__libraries = dict()

    def is_empty(self) -> bool:
        return len(self.__libraries) == 0

    def add_library(self, library: PoseLibrary) -> None:
        self.__libraries[library.key] = library
