import click
import matplotlib.pyplot as plt
from numpy.random import choice
from PIL import Image
from ..paths import RawData
from ..metadata import MetadataRepository, id2class


@click.command()
@click.option('--set', default="train", help='Either "train" or "test".')
@click.option('--n', default=8, help='The number of images to be visualized.')
def explore(set: str, n: int) -> None:
    (folder, metadata_filepath) = (
        (RawData.train_folder, RawData.train_labels)
        if set == "train"
        else (RawData.test_folder, RawData.test_labels)
    )
    metadata = MetadataRepository(metadata_filepath)
    image_filenames = [x for x in folder.iterdir()]
    random_selection = choice(image_filenames, size=n, replace=False)
    for image_filename in random_selection:
        category_id = metadata[image_filename.name].category_id
        class_name = id2class[category_id]
        with Image.open(image_filename) as image:
            plt.imshow(image)
            plt.suptitle(image_filename.name)
            plt.title(class_name)
            plt.show()


if __name__ == "__main__":
    explore()
