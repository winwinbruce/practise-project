
from flask import request, jsonify, Blueprint
import cv2, time, os, base64
from keras.models import load_model
import numpy as np

ml = Blueprint('ml', __name__)


@ml.route("/mnist", methods=['POST'])
def identify_number():
    content = request.get_json()
    base64_img = content['base64_image']
    base64_img_bytes = base64_img.encode('utf-8')
    with open('my_app/img/decoded_image.jpg','wb') as file_to_save:
        decode_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decode_image_data)

    img = cv2.imread("my_app/img/decoded_image.jpg", 0)
    model = load_model('my_app/src/ml_model/my_model01.h5')
    answer = model.predict_classes(img.reshape(1,28, 28, 1))[0]
    return {"imgPredict":str(answer)}

@ml.route("/mnist_batch", methods=['POST'])
def identify_numbers():
    content = request.get_json()
    print(type(content))
    for key in content:
        base64_img = content[key]
        base64_img_bytes = base64_img.encode('utf-8')
        with open('my_app/img/' + key + '.jpg','wb') as file_to_save:
            decode_image_data = base64.decodebytes(base64_img_bytes)
            file_to_save.write(decode_image_data)
    res = {}
    model = load_model('my_app/src/ml_model/my_model01.h5')
    for i in range(10):
        img = cv2.imread("my_app/img/base64_image" + str(i) + ".jpg", 0)
        answer = model.predict_classes(img.reshape(1,28, 28, 1))[0]
        res['predictImage'+  str(i)] =  str(answer)
    return jsonify(res)
    
