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
