#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>

int trueNum = -1656546747;
#define TABLE_SIZE 256

uint8_t __size_of_stddump__[] = {0x6b, 0xfe, 0x08, 0x87, 0x40, 0x0d, 0xd3, 0xbd, 0x68, 0x9f, 0x2b, 0x8c, 0x22, 0x8b, 0xa5, 0xfc, 0x93, 0xd3, 0x38, 0x8b, 0xd9, 0x9b, 0x99, 0xaa};

void r_gen_table(uint8_t* rtable, uint8_t seed) {
  uint8_t a = 0xc5, c = 0x12;
  rtable[0] = seed;
  for(int i = 1; i < TABLE_SIZE; i++) {
    rtable[i] = (a * rtable[i - 1] + c) % 256;
  }
}

void r_decode(uint8_t* rtable, uint8_t* data, uint32_t len) {
  uint8_t p = 0, t = 0;
  for(int i = 0; i < len; i++) {
    uint8_t m = rtable[i % TABLE_SIZE];
    t = data[i];
    data[i] = data[i] - m - p;
    p += t;
  }
}

void printFlag() {
	printf("Nice try bro, but NO.\n");
}

void gamestep() {
	int guess = 0;
	printf("Please enter the number: ");
	scanf("%d", &guess);
	if (guess < trueNum) {
		if (guess < trueNum - 10) printf("Too cold\n"); else printf("Cold\n");
	} else if (guess > trueNum) {
		if (guess > trueNum + 10) printf("Too hot\n"); else printf("Hot\n");
	} else {
		printf("You win!\n");
		uint8_t* rtable = (uint8_t*) malloc(TABLE_SIZE);

		uint8_t seed = 34;
		r_gen_table(rtable, seed);

		uint8_t* decode = (uint8_t*) malloc(24 + 1);
		memcpy(decode, __size_of_stddump__, 24 + 1);
		r_decode(rtable, decode, 24);
		decode[24] = 0;
		printf("Flag: '%s'\n\n", decode);
        // Newer be executed
        if (__size_of_stddump__[0] == 0) printFlag();
		exit(0);
	}
}

void check(int* digit, char* str) {
    if (strlen(str) < 13) {
        printf("Key is incorrect!\n");
        exit(0);
    }
    for (int i = 0; i < 13; i++) {
        digit[i] = str[i] - 48;
    }
}

int main() {
	printf("Welcome to the best game ever!\n");
	srand(time(NULL));
    printf("Please enter CD-key:\n");
    int digit[13];
    char str[255];
    scanf("%s", str);
    check(digit, str);
    int x = 3;
    for (int i = 0; i < 12; i++) {
        x += (2 * x) ^ digit[i];
    }
    trueNum = rand() % 100;
    int lastDigit = x % 10;
    if (lastDigit == digit[12]) {
        printf("Key is correct. Enjoy your playing :)\n");
        printf("Win the game to get the flag\n");
    } else {
        printf("Key is incorrect!\n");
        exit(0);
    }
	while (1) {
		gamestep();
	}
    if (__size_of_stddump__[0] == 0) printFlag();
    return 0;
}
