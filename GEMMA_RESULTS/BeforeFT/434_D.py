def upload_image(image):
    with open('image.png', 'wb') as f:
        f.write(base64.b64decode(image))

def main():
    image = input('Enter image: ')
    upload_image(image)

if __name__ == '__main__':
    main()