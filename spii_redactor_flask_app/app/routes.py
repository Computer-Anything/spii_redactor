from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from app import extract_text, redact_pii, process_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        redacted_text, original_image = process_image(file_path)
        
        return render_template('result.html', redacted_text=redacted_text, original_image=original_image)

    return redirect(url_for('index'))