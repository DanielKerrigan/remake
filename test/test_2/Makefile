all: hello					# Default target

hello: 		main.o hello.o			# Executable target
		gcc -o hello main.o hello.o 

main.o:		main.c				# Object targets
		gcc -std=gnu99 -Wall -c -o main.o main.c

hello.o:	hello.c
		gcc -std=gnu99 -Wall -c -o hello.o hello.c

clean:						# Clean target
		rm -f hello *.o
