import click
from numpy.random import choice
from PIL import Image
from ..paths import RawData


@click.command()
@click.option('--set', default="train", help='Either "train" or "test".')
@click.option('--n', default=8, help='The number of images to be visualized.')
def explore(set: str, n: int) -> None:
    folder = RawData.train_folder if set == "train" else RawData.test_folder
    image_filenames = [x for x in folder.iterdir()]
    random_selection = choice(image_filenames, size=n, replace=False)
    for image_filename in random_selection:
        with Image.open(image_filename) as image:
            image.show()


if __name__ == "__main__":
   explore()
