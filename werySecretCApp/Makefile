all: simple

simple:
	gcc main.c -static -std=c99 -o simple  `mysql_config --cflags --libs`

release:
	gcc main.c -static -O3 -m64 -std=c99 -o release  `mysql_config --cflags --libs`
	strip --strip-debug release

stripped:
	gcc main.c -static -std=c99 -O3 -m64 -s -o stripped  `mysql_config --cflags --libs`

smile_everyone:
	cat howToBreak

clean:
	rm -rf *.o simple release stripped
