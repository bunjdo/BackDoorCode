#include <stdlib.h>
#include <iostream>
#include <time.h>
#include <string>

int trueNum = 0;

void gamestep() {
	int guess = 0;
	std::cout << "Please enter the number: ";
	std::cin >> guess;
	if (guess < trueNum) {
		if (guess < trueNum - 10) std::cout << "Too cold\n"; else std::cout << "Cold\n";
	} else if (guess > trueNum) {
		if (guess > trueNum + 10) std::cout << "Too hot\n"; else std::cout << "Hot\n";
	} else {
		std::cout << "You win! New game? (y/n)\n";
		char c = '\n';
		while (c != 'y' && c != 'n' && c != 'Y' && c != 'N') std::cin >> c;
		if (c == 'y' || c == 'Y') {
			trueNum = rand() % 100;
		} else {
			exit(0);
		}
	}
}

void check() {
	std::cout << "Please enter CD-key:\n";
	int digit[13];
	std::string str;
	std::cin >> str;
	if (str.size() < 13) {
		std::cout << "Key is incorrect!\n";
		exit(0);
	}
	for (int i = 0; i < 13; i++) {
		digit[i] = str[i] - 48;
	}
	int x = 3;
	for (int i = 0; i < 12; i++) {
		x += (2 * x) ^ digit[i];
	}
	int lastDigit = x % 10;
	if (lastDigit == digit[12]) {
		std::cout << "Key is correct. Enjoy your playing :)\n";
	} else {
		std::cout << "Key is incorrect!\n";
		exit(0);
	}
}

int main() {
	std::cout << "Welcome to the best game ever!\n";
	srand(time(NULL));
	trueNum = rand() % 100;
	check();
	while (true) {
		gamestep();
	}
    return 0;
}

