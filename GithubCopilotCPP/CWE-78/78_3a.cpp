#include <iostream>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>

void print(const char* format, ...) {
    char buffer[256];
    va_list args;
    va_start(args, format);
    vsnprintf(buffer, sizeof(buffer), format, args);
    va_end(args);
    system(buffer);
}

int main() {
    print("ls");
    return 0;
}