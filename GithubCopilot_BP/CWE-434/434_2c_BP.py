import os

import base64

from werkzeug.utils import secure_filename

import uuid



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def generate_random_filename(extension):

    return str(uuid.uuid4()) + '.' + extension



def upload_image(file, upload_dir='uploads', encoded_dir='encoded'):

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        random_filename = generate_random_filename(filename.rsplit('.', 1)[1])

        upload_path = os.path.join(upload_dir, random_filename)

        encoded_path = os.path.join(encoded_dir, random_filename + '.txt')



        # Ensure directories exist

        os.makedirs(upload_dir, exist_ok=True)

        os.makedirs(encoded_dir, exist_ok=True)



        # Save the uploaded file

        file.save(upload_path)



        # Read and encode the image

        with open(upload_path, "rb") as image_file:

            encoded_string = base64.b64encode(image_file.read()).decode()



        # Write the encoded string to a separate file

        with open(encoded_path, "w") as file:

            file.write(encoded_string)



        return True, "File uploaded and encoded successfully."

    else:

        return False, "File extension not allowed."