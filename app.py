from flask import Flask, request, render_template
from object_recognizer import ObjectRecognizer
import cv2
import os

app = Flask(__name__, template_folder='./templates')
app.static_folder = './static'

obj_recognizer = ObjectRecognizer(show_conf=False)

@app.route('/', methods=['GET', 'POST'])
def upload_and_detect() : 
	message = request.args.get('message')
	objects, image_save_filename = None, None
	if request.method == 'POST' : 
		image = (request.files.get('image'))
		if image : 
			image_save_filename = 'detected_' + image.filename
			image_path =  os.path.join("static\\images", image.filename)
			image_save_path = os.path.join("static\\images", image_save_filename)
			image.save(image_path)
			detected_image, objects = obj_recognizer.recognize(cv2.imread(image_path))
			cv2.imwrite(image_save_path, detected_image)
	return render_template(
		'upload_and_detect.jinja',
		message=message, 
		detected_image=image_save_filename,
		objects=objects
	)

app.run(port=10000, debug=True)