import os
from pathlib import Path


class Config:
    data_folder: Path = Path(os.getenv("DATA_FOLDER", "/home/luca/Data/iwildcam-2019-fgvc6"))
