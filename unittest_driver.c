


#include <stdio.h>
#include <stdlib.h>
#include "tools.h"

int main() 
{
    char *filename = "test.ascii";
    read_ascii_from_filepath(filename);
    printf("Hello, World!\n");

    return EXIT_SUCCESS;
}