import numpy as np
from .config import CLASS_LABELS


def predict_image(model, img_array):
    predictions = model.predict(img_array)
    predicted_class_index = int(np.argmax(predictions, axis=1)[0])
    predicted_class_label = CLASS_LABELS[predicted_class_index]
    confidence = float(predictions[0][predicted_class_index])
    return predicted_class_index, predicted_class_label, confidence
