import tensorflow as tf
from .config import MODEL_PATH


def load_model():
    return tf.keras.models.load_model(MODEL_PATH)
