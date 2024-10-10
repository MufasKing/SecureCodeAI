#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <sstream>
#include <iomanip>
#include <openssl/evp.h>

// Function to encode data to base64
std::string base64_encode(const std::vector<unsigned char>& data) {
    BIO *bio, *b64;
    BUF_MEM *bufferPtr;
    
    b64 = BIO_new(BIO_f_base64());
    bio = BIO_new(BIO_s_mem());
    bio = BIO_push(b64, bio);
    
    BIO_set_flags(bio, BIO_FLAGS_BASE64_NO_NL); // Ignore newlines
    BIO_write(bio, data.data(), data.size());
    BIO_flush(bio);
    BIO_get_mem_ptr(bio, &bufferPtr);
    
    std::string base64_data(bufferPtr->data, bufferPtr->length);
    BIO_free_all(bio);
    
    return base64_data;
}

// Function to upload and process the image
void upload_image(const std::string& image_path, const std::string& output_path) {
    // Read the image file into a byte array
    std::ifstream image_file(image_path, std::ios::binary);
    if (!image_file) {
        std::cerr << "Error opening image file: " << image_path << std::endl;
        return;
    }
    
    std::vector<unsigned char> image_data((std::istreambuf_iterator<char>(image_file)),
                                          std::istreambuf_iterator<char>());
    image_file.close();
    
    // Encode the image data to base64
    std::string encoded_image = base64_encode(image_data);
    
    // Write the encoded image to the output file
    std::ofstream output_file(output_path);
    if (!output_file) {
        std::cerr << "Error opening output file: " << output_path << std::endl;
        return;
    }
    
    output_file << encoded_image;
    output_file.close();
    
    std::cout << "Image successfully uploaded and encoded to base64." << std::endl;
}

int main() {
    std::string image_path = "path/to/your/image.jpg";
    std::string output_path = "path/to/output/file.txt";
    
    upload_image(image_path, output_path);
    
    return 0;
}