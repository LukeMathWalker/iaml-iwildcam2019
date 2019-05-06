# IWildCam 2019

Playing around with some data.

## Configuration

### Requirements

- Python 3.7 (system Python, unfortunately)
- [Poetry](https://poetry.eustace.io/)

### Steps

To reproduce my environment, follow these steps:
```bash
# Create a virtual environment, using Python 3.7
python3.7 -m venv env
# Activate the virtual environment
source env/bin/activate
# Install packages from the Poetry lock file
poetry install
```

### Env variables

`DATA_FOLDER`: it should point at the folder containing the data downloaded from Kaggle (already unzipped).

## Tooling and niceties

To print a bunch of images for inspection, you can use the cli command `explore`; for example:
```bash
# Show 10 random images from the training set
explore --set="train" -n 10
# Show 12 random images from the test set
explore --set="test" -n 12
```