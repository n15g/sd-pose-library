import os.path
from typing import Optional

SUPPORTED_TYPES = ["png", "jpg", "jpeg", "webp"]


def find_img(path) -> Optional[str]:
    """
    Given a path with no extension, scan for known image types and return
    the first found.
    i.e. Given '/foo/bar' it would look for '/foo/bar.jpg', '/foo/bar.png', etc.
    :param path: Base path to interrogate, without an extension.
    :return: Image path if any are found, None if not.
    """
    for ext in SUPPORTED_TYPES:
        full_path = f"{path}.{ext}"
        if os.path.exists(full_path):
            return full_path
    return None
