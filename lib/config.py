# config.py
import os

# Image dimensions
IMAGE_HEIGHT = 299
IMAGE_WIDTH = 299

# Paths
UPLOAD_FOLDER = "temp"
MODEL_PATH = os.path.join("models", "densenet121_model.keras")

# Class labels
CLASS_LABELS = ["glioma_tumor", "meningioma_tumor", "no_tumor", "pituitary_tumor"]
