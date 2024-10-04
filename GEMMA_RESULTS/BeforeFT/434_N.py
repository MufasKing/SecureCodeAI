def upload_image(image_file):
    with open(image_file, 'rb') as f:
        encoded_image = base64.b64encode(f.read())
    with open('encoded_image.txt', 'w') as f:
        f.write(encoded_image)

def main():
    upload_image('image.jpg')

if __name__ == '__main__':
    main()