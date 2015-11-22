all: simple

simple:
	gcc main.c -std=c99 -o simple  `mysql_config --cflags --libs`

release:
	gcc main.c -O3 -m64 -std=c99 -o release  `mysql_config --cflags --libs`

stripped:
	gcc main.c -std=c99 -O3 -m64 -s -o stripped  `mysql_config --cflags --libs`

clean:
	rm -rf *.o simple release stripped
