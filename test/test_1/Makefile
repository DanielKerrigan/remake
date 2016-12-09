# Comment
CXX=		g++ # Comment
CXXFLAGS=	-g -Wall -std=gnu++11

#all: 		comment
all:		detour

solution:	solution.cpp
	$(CXX) solution.cpp $(CXXFLAGS) -o solution
	touch test.xyz

detour: solution

clean:
	rm solution test.xyz

cycle: cycle1
	echo 1

cycle1: cycle2
	echo 2

cycle2: cycle3
	echo 3

cycle3: cycle
	echo 3
