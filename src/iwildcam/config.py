import os


class Config:
    data_folder = os.getenv("DATA_FOLDER", "/home/luca/Data")
