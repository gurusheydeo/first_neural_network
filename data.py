# loads the training and test data along with the labels from data images

import numpy as np
from pathlib import Path
from PIL import Image
from logging import getLogger, basicConfig, DEBUG

log = getLogger(__name__)
basicConfig(level=DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Data:
    """
    Class to represent the data with their load and process functions
    The data is represented as a 3D array of pixels
    The first dimension represents the image
    The second dimension represents the row of pixels
    The third dimension represents the column of pixels
    The data is in the path "data"
    the data folder is structured as follows:
    data
    ├── test
    │   ├── Apple_test
    │   │    ├── Apple Braeburn_0.jpg
    │   │    ├── ...
    │   │    └── Apple Braeburn_142.jpg
    │   └── Mango_test
    │        ├── Mango_0.jpg
    │        ├── ...
    │        └── Mango_142.jpg
    └── training
        ├── Apple_train
        │    ├── Apple Braeburn_2.jpg
        │    ├── ...
        │    └── Apple Braeburn_491.jpg
        └── Mango_train
             ├── Mango_2.jpg
             ├── ...
             └── Mango_489.jpg
    """

    def __init__(self):
        pass

    def load_images(self, path: Path) -> np.ndarray:
        """
        Load the images from the given path
        :param path: path object representing the directory containing the images
        :return: array of images which have been converted into array of pixels (flattened)
        """
        images = []
        # Iterate through each file in the directory and subdirectories
        for image_path in path.glob('**/*.jpg'):
            # Process each image
            img_array = self.process_image(image_path)
            images.append(img_array)
        # Stack all image arrays into a single numpy array
        images_array = np.stack(images)
        log.debug(f"Loaded images from {path} with shape {images_array.shape}")
        return images_array

    def process_image(self, image_path: Path) -> np.ndarray:
        """
        Process the image at the given path
        :param image_path: path object representing the image
        :return: array of pixels representing the image
        """
        with Image.open(image_path) as img:
            # Resizing the image to 64x64
            img = img.resize((64, 64))
            # Convert image to RGB - should already be in RGB but just in case
            img = img.convert('RGB')
            # Convert image to a numpy array
            img_array = np.array(img)

            return img_array

    def get_test_data(self) -> np.ndarray:
        """
        Get the test data
        :return: array of test images
        """
        return self.load_images(Path('data/test'))

    def get_training_data(self) -> np.ndarray:
        """
        Get the training data
        :return: array of training images
        """
        return self.load_images(Path('data/training'))


def main():
    data = Data()
    test_data = data.get_test_data()
    # # training_data = data.get_training_data()
    # print(f"Test Data: {test_data.shape}")
    # # print(f"Training Data: {training_data.shape}")
    log.info("Data loaded successfully")


if __name__ == '__main__':
    main()

