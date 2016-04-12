#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

void unpack1(FILE* in, FILE* out) {
    uint8_t b;
    uint8_t br = 0;

    int read = 0;

    int i = 0;
    while((read = fgetc(in)) != EOF) {
        if(i >= 8) {
            fputc(br, out);
            i = 0;
            br = 0;
        }
        b = read;

        if(b > 127) br |= 1 << i;
        i++;
    }
    fputc(br, out);
}

void unpack2(FILE* in, FILE* out) {
    int read = 0;
    while((read = fgetc(in)) != EOF) {
        fputc(read, out);

        for(int i = 0; i < read; i++) {
            fgetc(in);
        }
    }
}

void unpack3(FILE* in, FILE* out) {
    int read = 0;
    while(1) {
        uint16_t r1, r2;
        size_t n1, n2;
        n1 = fread(&r1, 1, 2, in);
        n2 = fread(&r2, 1, 2, in);

        uint8_t rn = fgetc(in);

        if(n1 == 0 || n2 == 0) {
            break;
        }

        int s = 0;
        for(int i = 0; i < 256; i++) {
            for(int j = 0; j < 256; j++) {
                if(i + j == r1 && i * j == r2) {
                    if (rn < 128) {
                        fputc(MIN(i, j), out);
                        fputc(MAX(i, j), out);
                    } else {
                        fputc(MAX(i, j), out);
                        fputc(MIN(i, j), out);
                    }


                    goto m1;
                }
            }
        }

        m1:
        continue;
    }
}

int main() {
    printf("UnPack\n");

    FILE* input1 = fopen("input.txt.rrr", "r");
    FILE* output1 = fopen("output.txt.1", "w");
    unpack3(input1, output1);
    fclose(input1), fclose(output1);

    FILE* input2 = fopen("output.txt.1", "r");
    FILE* output2 = fopen("output.txt.2", "w");
    unpack2(input2, output2);
    fclose(input2), fclose(output2);

    FILE* input3 = fopen("output.txt.2", "r");
    FILE* output3 = fopen("output.txt", "w");
    unpack1(input3, output3);
    fclose(input3), fclose(output3);
}
