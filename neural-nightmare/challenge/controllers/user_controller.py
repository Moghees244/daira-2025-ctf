import os
import keras
import numpy as np
from flask import render_template, request, jsonify

def homepage():
    return render_template('home.html')

# Allowed extensions for Keras model files
ALLOWED_EXTENSIONS = {'keras'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Only .keras files are accepted.'}), 400
    
    file_path = os.path.join('/uploads', file.filename)
    file.save(file_path)

    # Load Keras model
    try:
        model = keras.models.load_model(file_path, safe_mode=False)
        return jsonify({'message': f'File {file.filename} uploaded successfully!', 'output': ''}), 201
    except Exception as e:
        return jsonify({'error': f'Failed to load model: {str(e)}'}), 500
    
    if os.path.exists(file_path):
        os.remove(file_path)

