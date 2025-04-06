from flask import Flask, request, render_template_string
import face_recognition
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_RESULT = '''
<!DOCTYPE html>
<html>
<head><title>Result</title></head>
<body>
  <h2>{{ result_text }}</h2>
  <a href="/">Go Back</a>
</body>
</html>
'''

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    total_faces = len(face_locations)

    result = f"Total {total_faces} Fukra Face(s) Detected!"
    return render_template_string(HTML_RESULT, result_text=result)

if __name__ == '__main__':
    app.run(debug=True)
