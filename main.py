#!flask/bin/python
import os
import urllib.request
import shutil
from os import path
from app import app
from mv import mv
from txt import text
from flask import Flask, request, redirect, jsonify, send_from_directory, abort, render_template
from werkzeug.utils import secure_filename



CLIENT_IMAGES = '/home/yehor/tz/templates'
app.config['CLIENT_IMAGES'] = CLIENT_IMAGES


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'tf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		text()
		mv()
		return render_template('sg.txt')
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp




if __name__ == "__main__":
    app.run(debug=True)
