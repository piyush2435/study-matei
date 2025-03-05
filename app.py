import os
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Folder where study materials are stored
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_material')
def get_material():
    selected_class = request.args.get('class')

    # Construct the folder path based on selected class
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], f'class_{selected_class}')

    if not os.path.exists(folder_path):  # If folder doesn't exist, return message
        return jsonify({"message": "No study materials available yet.", "files": []})

    files = os.listdir(folder_path)  # List available files
    file_links = [f"/download/{selected_class}/{file}" for file in files]

    return jsonify({"files": file_links})

@app.route('/download/<class_name>/<filename>')
def download_file(class_name, filename):
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], f'class_{class_name}')
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(debug=True)

