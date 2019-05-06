from typing import NamedTuple
from pathlib import Path
from .config import Config


class RawData(NamedTuple):

    train_folder: Path = Config.data_folder / "train"
    train_labels: Path = Config.data_folder / "train.csv"
    test_folder: Path = Config.data_folder / "test"
    test_labels: Path = Config.data_folder / "test.csv"
