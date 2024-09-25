#include <iostream>
#include <fstream>
#include <string>
#include <miniz.h>
#include <sys/stat.h>
#include <filesystem>

namespace fs = std::filesystem;

void unzip(const std::string &zipFilePath, const std::string &outputDir) {
    // Create output directory if it doesn't exist
    if (!fs::exists(outputDir)) {
        fs::create_directories(outputDir);
    }

    // Open the ZIP archive
    mz_zip_archive zipArchive;
    memset(&zipArchive, 0, sizeof(zipArchive));
    if (!mz_zip_reader_init_file(&zipArchive, zipFilePath.c_str(), 0)) {
        std::cerr << "Failed to open zip file: " << zipFilePath << std::endl;
        return;
    }

    // Get the number of files in the ZIP archive
    int fileCount = (int)mz_zip_reader_get_num_files(&zipArchive);
    for (int i = 0; i < fileCount; i++) {
        mz_zip_archive_file_stat fileStat;
        if (mz_zip_reader_file_stat(&zipArchive, i, &fileStat)) {
            std::string outputFilePath = outputDir + "/" + fileStat.m_filename;
            
            // Create necessary directories for the output file
            fs::path outputPath(outputFilePath);
            if (!fs::exists(outputPath.parent_path())) {
                fs::create_directories(outputPath.parent_path());
            }

            // Extract the file
            if (!mz_zip_reader_extract_to_file(&zipArchive, i, outputFilePath.c_str(), 0)) {
                std::cerr << "Failed to extract file: " << fileStat.m_filename << std::endl;
            } else {
                std::cout << "Extracted: " << fileStat.m_filename << " to " << outputFilePath << std::endl;
            }
        }
    }

    // Close the ZIP archive
    mz_zip_reader_end(&zipArchive);
}

int main() {
    const std::string zipFilePath = "archive.zip";
    const std::string outputDir = "/tmp/unpack";

    unzip(zipFilePath, outputDir);
    return 0;
}
