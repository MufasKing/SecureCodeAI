#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>
#include <tar.h>
#include <archive.h>
#include <archive_entry.h>

class FileHandle {
public:
    FileHandle(const std::string& filename, std::ios_base::openmode mode) {
        file.open(filename, mode);
        if (!file.is_open()) {
            throw std::runtime_error("Failed to open file");
        }
    }

    ~FileHandle() {
        if (file.is_open()) {
            file.close();
        }
    }

    std::fstream& get() {
        return file;
    }

private:
    std::fstream file;
};

class TarFile {
public:
    TarFile(const std::string& filename, const std::string& mode) {
        archive = archive_write_new();
        if (mode == "w") {
            archive_write_add_filter_gzip(archive);
            archive_write_set_format_pax_restricted(archive);
            archive_write_open_filename(archive, filename.c_str());
        } else if (mode == "r") {
            archive_read_support_filter_all(archive);
            archive_read_support_format_all(archive);
            archive_read_open_filename(archive, filename.c_str(), 10240);
        } else {
            throw std::runtime_error("Unsupported mode");
        }
    }

    ~TarFile() {
        if (archive) {
            archive_write_free(archive);
        }
    }

    struct archive* get() {
        return archive;
    }

private:
    struct archive* archive;
};

int main() {
    try {
        // Using FileHandle to open a file
        {
            FileHandle fileHandle("example.txt", std::ios::out);
            std::fstream& file = fileHandle.get();
            file << "Hello, World!" << std::endl;
        } // FileHandle destructor will close the file here

        // Using TarFile to create a tar archive
        {
            TarFile tarFile("example.tar.gz", "w");
            struct archive* a = tarFile.get();
            struct archive_entry* entry = archive_entry_new();
            archive_entry_set_pathname(entry, "example.txt");
            archive_entry_set_size(entry, 13); // Size of "Hello, World!\n"
            archive_entry_set_filetype(entry, AE_IFREG);
            archive_entry_set_perm(entry, 0644);
            archive_write_header(a, entry);
            archive_write_data(a, "Hello, World!\n", 13);
            archive_entry_free(entry);
        } // TarFile destructor will close the archive here

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}