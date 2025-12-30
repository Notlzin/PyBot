// math_plugin.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float add(float a, float b) {
    return a + b;
}

float sub(float a, float b) {
    return a - b;
}

float mul(float a, float b) {
    return a * b;
}

float divi(float a, float b) {
    return a / b;
}

int main(int argc, char** argv) {
    if (argc != 4) {
        printf("error\n");
        return 1;
    }

    char* op = argv[1];
    float a = atof(argv[2]);
    float b = atof(argv[3]);

    float result = 0.0f;

    if (strcmp(op, "add") == 0) result = add(a, b);
    else if (strcmp(op, "sub") == 0) result = sub(a, b);
    else if (strcmp(op, "mul") == 0) result = mul(a, b);
    else if (strcmp(op, "div") == 0) result = divi(a, b);
    else {
        printf("unknown_op\n");
        return 1;
    }

    printf("%.6f\n", result);
    return 0;
}
