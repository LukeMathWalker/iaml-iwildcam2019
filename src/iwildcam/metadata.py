import pandas as pd
from typing import NamedTuple
from pathlib import Path
from bidict import bidict


class2id = bidict({
    "empty": 0,
    "deer": 1,
    "moose": 2,
    "squirrel": 3,
    "rodent": 4,
    "small_mammal": 5,
    "elk": 6,
    "pronghorn_antelope": 7,
    "rabbit": 8,
    "bighorn_sheep": 9,
    "fox": 10,
    "coyote": 11,
    "black_bear": 12,
    "raccoon": 13,
    "skunk": 14,
    "wolf": 15,
    "bobcat": 16,
    "cat": 17,
    "dog": 18,
    "opossum": 19,
    "bison": 20,
    "mountain_goat": 21,
    "mountain_lion": 22
})

id2class = class2id.inv


class Metadata(NamedTuple):
    category_id: str
    date_captured: str
    file_name: str
    frame_num: str
    id: str
    location: str
    rights_holder: str
    seq_id: str
    seq_num_frames: str
    width: str
    height: str


class MetadataRepository:
    def __init__(self, filepath: Path) -> None:
        assert filepath.suffix == ".csv", "Metadata have to be in a csv file"
        self.filepath = filepath
        # Some images have more than one associated label
        self.data = pd.read_csv(self.filepath)\
            .drop_duplicates(subset="file_name")\
            .set_index(keys="file_name", drop=False, verify_integrity=True)

    def __getitem__(self, item: str) -> Metadata:
        return Metadata(**self.data.loc[item].to_dict())
