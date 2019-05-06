import os
from typing import NamedTuple
from pathlib import Path


class Config(NamedTuple):
    data_folder: Path = Path(os.getenv("DATA_FOLDER", "/home/luca/Data"))
