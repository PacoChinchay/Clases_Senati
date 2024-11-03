#include <iostream>
using namespace std;

int numero;

int main() {
	setlocale(LC_ALL, "");
	cout << "Ingrese el número de escalones: ";
	cin >> numero;
	
	for (numero; numero >= 0; numero--) {
		for (int f = 1; f <= numero; f++) {
			cout << f;
		}
		cout << endl;
	}
	
	return 0;
}

