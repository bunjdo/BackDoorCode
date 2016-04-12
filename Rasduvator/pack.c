#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>

uint8_t m_rnd(uint8_t from, uint8_t to) {
    return (rand() % (to - from)) + from;
}

void pack1(FILE* in, FILE* out) {
    uint8_t b;

    int read = 0;

    while((read = fgetc(in)) != EOF) {
        b = read;
        for(int i = 0; i < 8; i++) {
            uint8_t bit = (b & ( 1 << i )) >> i;
            fputc(bit > 0 ? m_rnd(128, 255) : m_rnd(0, 127), out);
        }
    }

}

void pack2(FILE* in, FILE* out) {
    int read = 0;
    while((read = fgetc(in)) != EOF) {
        fputc(read, out);
        for(int i = 0; i < read; i++) {
            fputc(m_rnd(0, 255), out);
        }
    }
}

void pack3(FILE* in, FILE* out) {
    int32_t r1 = 0, r2 = 0;
    while(1) {
        if((r1 = fgetc(in)) == EOF) break;
        if((r2 = fgetc(in)) == EOF) r2 = 0;

        uint16_t sum = r1 + r2;
        uint16_t mul = r1 * r2;

        fwrite(&sum, 1, 2, out);
        fwrite(&mul, 1, 2, out);

        fputc(r1 > r2 ? m_rnd(128, 255) : m_rnd(0, 127), out);
    }
}

int main() {
    srand(time(NULL));
    printf("Pack\n");

    FILE* input1 = fopen("input.txt", "r");
    FILE* output1 = fopen("input.txt.1", "w");
    pack1(input1, output1);
    fclose(input1), fclose(output1);

    FILE* input2 = fopen("input.txt.1", "r");
    FILE* output2 = fopen("input.txt.2", "w");
    pack2(input2, output2);
    fclose(input2), fclose(output2);

    FILE* input3 = fopen("input.txt.2", "r");
    FILE* output3 = fopen("input.txt.rrr", "w");
    pack3(input3, output3);
    fclose(input3), fclose(output3);
}
