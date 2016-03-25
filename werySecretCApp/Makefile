all: release

release:
	gcc main.c -static -O3 -m64 -std=c99 -o release  `mysql_config --cflags --libs`
	strip --strip-debug release

smile_everyone:
	cat howToBreak

clean:
	rm -rf *.o simple release stripped
