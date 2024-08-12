from flask import Flask, request, send_file
from flask_cors import CORS
import os
from ultralytics import YOLO
from PIL import Image

# init Flask app
app = Flask(__name__)
CORS(app)

# init YOLO
modelv8 = YOLO("weights//yolov8n.pt")
modelv9 = YOLO("weights//yolov9c.pt")
modelv10 = YOLO("weights//yolov10n.pt")

@app.route('/<version>',methods=['POST'])
def home_page(version):
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    
    if file.filename == '':
        return 'No selected image', 400

    # select model
    if version == 'yolov8':
        model = modelv8
    elif version == 'yolov9':
        model = modelv9
    elif version == 'yolov10':
        model = modelv10
    else:
        return 'Invalid model version', 400

    if file:
        # load image
        image = Image.open(file.stream)

        # process image
        result_path = os.path.join('.//result_img',file.filename)
        results = model(image)
        results[0].save(result_path)  # This saves the processed image to disk

        # Send the processed image back
        return send_file(
            result_path,
            as_attachment=True,
            mimetype='image/png'
        )



if __name__ == "__main__":
    app.run(debug=True)