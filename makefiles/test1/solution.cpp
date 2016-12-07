// Challenge 01: Rotating Arrays

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Main Execution

int main(int argc, char *argv[]) {

	char z;
	vector<char> inputs;
	while( cin >> z){
		inputs.push_back(z);
	}

	int length;
	int rotations;
	char direction;
	vector<vector<int> > results;
	vector<int> numbers;

	auto x = inputs.begin();
	while( x != inputs.end()){
		length = *x - 48;
		x++;
		rotations = *x - 48;
		x++;
		direction = *x;
		for( int i = 0; i < length; i++){
			x++;
			numbers.push_back(*x - 48);
		}

		if( direction == 'L' ){
			for( int r = 0; r < rotations; r++){
				for( int j = 3; j >= 0; j--){
					swap(numbers[4], numbers[j]);
				}
			}
		} else {
			for( int r = 0; r < rotations; r++){
				for( int j = 1; j < 5; j++){
					swap(numbers[0], numbers[j]);
				}
			}
		}

		results.push_back(numbers);
		while( !numbers.empty() ){
			numbers.pop_back();
		}
		x++;
	}

	for( auto ai = results.begin(); ai != results.end(); ai++){
		for( auto bi = (*ai).begin(); bi != (*ai).end(); bi++){
		//	auto test = bi;
			if( *bi == (*ai).back() ) 
				cout << *bi;
			else {cout << *bi << " ";}
		}
		cout << endl;
	}
    return 0;
}

// vim: set sts=4 sw=4 ts=8 expandtab ft=cpp:
