CXX=		gcc 
CXXFLAGS=	-std=gnu99 -Wall


all: hello					# Default target

hello: 		main.o hello.o			# Executable target
		$(CXX) -o hello main.o hello.o 

main.o:		main.c				# Object targets
		$(CXX) $(CXXFLAGS) -c -o main.o main.c

hello.o:	hello.c
		$(CXX) $(CXXFLAGS) -c -o hello.o hello.c

clean:						# Clean target
		rm -f hello *.o
