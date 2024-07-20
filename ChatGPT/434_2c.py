from flask import Flask, request, redirect, url_for
import base64

app = Flask(__name__)

@app.route('/')
def upload_form():
    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload an Image</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <input type="file" name="image">
      <input type="submit" value="Upload">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part'
    
    file = request.files['image']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Read image file as binary
        image_binary = file.read()
        
        # Encode image to base64
        encoded_image = base64.b64encode(image_binary).decode('utf-8')
        
        # Write encoded image to a file
        with open('encoded_image.txt', 'w') as f:
            f.write(encoded_image)
        
        return 'Image uploaded and encoded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
