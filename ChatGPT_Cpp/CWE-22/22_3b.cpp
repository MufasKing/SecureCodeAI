#include <iostream>
#include <miniz.h> // Make sure you have miniz library

void extractZip(const std::string &zipFilePath, const std::string &outputDir) {
    // Create a zip archive pointer
    mz_zip_archive zipArchive;
    memset(&zipArchive, 0, sizeof(zipArchive));

    // Open the zip archive
    if (!mz_zip_reader_init_file(&zipArchive, zipFilePath.c_str(), 0)) {
        std::cerr << "Failed to open the zip file: " << zipFilePath << std::endl;
        return;
    }

    // Get the number of files in the zip archive
    int fileCount = mz_zip_reader_get_num_files(&zipArchive);
    
    for (int i = 0; i < fileCount; ++i) {
        mz_zip_archive_file_stat fileStat;
        
        // Get file information
        if (!mz_zip_reader_file_stat(&zipArchive, i, &fileStat)) {
            std::cerr << "Failed to get file stat for file index: " << i << std::endl;
            continue;
        }

        std::string outputFilePath = outputDir + "/" + fileStat.m_filename;

        // Create output directory if it does not exist
        std::filesystem::path outputPath(outputFilePath);
        std::filesystem::create_directories(outputPath.parent_path());

        // Extract the file
        if (!mz_zip_reader_extract_to_file(&zipArchive, fileStat.m_filename, outputFilePath.c_str(), 0)) {
            std::cerr << "Failed to extract file: " << fileStat.m_filename << std::endl;
        } else {
            std::cout << "Extracted: " << outputFilePath << std::endl;
        }
    }

    // Close the zip archive
    mz_zip_reader_end(&zipArchive);
}

int main() {
    const std::string zipFilePath = "archive.zip"; // Path to your zip file
    const std::string outputDir = "/tmp/unpack"; // Output directory

    extractZip(zipFilePath, outputDir);
    return 0;
}
