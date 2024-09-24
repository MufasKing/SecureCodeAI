#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <b64/encode.h>

void upload_image(const std::string& input_file, const std::string& output_file) {
    // Read the image file into a vector
    std::ifstream image_file(input_file, std::ios::binary);
    if (!image_file) {
        std::cerr << "Error opening input file: " << input_file << std::endl;
        return;
    }

    // Read the contents of the file into a vector
    std::vector<char> buffer((std::istreambuf_iterator<char>(image_file)), std::istreambuf_iterator<char>());
    image_file.close();

    // Base64 encode the image
    std::string encoded_image;
    base64::encoder encoder;
    encoder.encode(buffer.data(), buffer.size(), std::back_inserter(encoded_image));

    // Write the encoded image to the output file
    std::ofstream output_file_stream(output_file);
    if (!output_file_stream) {
        std::cerr << "Error opening output file: " << output_file << std::endl;
        return;
    }

    output_file_stream << encoded_image;
    output_file_stream.close();

    std::cout << "Image uploaded and encoded successfully!" << std::endl;
}

int main() {
    // Example usage of the upload_image function
    std::string input_image_path = "path/to/your/image.jpg";
    std::string output_encoded_path = "path/to/your/output.txt";
    
    upload_image(input_image_path, output_encoded_path);
    
    return 0;
}
