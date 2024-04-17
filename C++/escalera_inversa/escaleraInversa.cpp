#include <iostream>
using namespace std;

int numero;

int main() {
	setlocale(LC_ALL, "");
	cout << "Ingrese el número de escalones: ";
	cin >> numero;
	
	for (int i = 1; i <= numero; i++) {
		for (int f = i; f > 0; f--) {
			cout << f;
		}
		cout << endl;
	}
	
	return 0;
}

