from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from sdf_SMILES import sdf_to_smiles

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'sdf'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def handle_file_upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Call the sdf_to_smiles function to process the file
        try:
            smiles_file = sdf_to_smiles(filepath, output_dir=app.config['UPLOAD_FOLDER'])
            flash(f"File processed successfully! SMILES saved to {smiles_file}")
        except Exception as e:
            flash(f"Error processing file: {e}")
        
        return redirect(url_for('upload_file'))
    else:
        flash('Invalid file type. Only .sdf files are allowed.')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)