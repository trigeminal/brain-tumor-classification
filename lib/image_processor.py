import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.densenet import preprocess_input
from .config import IMAGE_HEIGHT, IMAGE_WIDTH


def preprocess_image(image_path):
    img = load_img(image_path, target_size=(IMAGE_HEIGHT, IMAGE_WIDTH))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array
