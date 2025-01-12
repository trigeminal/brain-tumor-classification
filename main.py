# app.py
from flask import Flask, request, jsonify
import os
from lib.config import UPLOAD_FOLDER
from lib.load_model import load_model
from lib.image_processor import preprocess_image
from lib.predictor import predict_image

app = Flask(__name__)

# Load the trained model
model = load_model()

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # Save the file temporarily
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Preprocess the image
        img_arr = preprocess_image(file_path)

        # Make prediction
        predicted_class_index, predicted_class_label, confidence = predict_image(
            model, img_arr
        )

        # Clean up the temp file
        os.remove(file_path)

        # Return the prediction
        return jsonify(
            {
                "confidence": confidence,
                "confidence_percentage": f"{confidence*100:.2f}%",
                "predicted_class_index": predicted_class_index,
                "predicted_class": predicted_class_label,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
