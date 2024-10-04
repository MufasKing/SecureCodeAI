#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char buffer[1024];
    int i;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <format string>
", argv[0]);
        exit(1);
    }

    printf("Enter a string: ");
    scanf("%1023[^
]%*c", buffer);

    printf("You entered: %s
", buffer);

    return 0;
}