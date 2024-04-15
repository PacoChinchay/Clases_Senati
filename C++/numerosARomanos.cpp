#include <iostream>

using namespace std;

string unidades[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

string decenas[] ={"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};

string conversion(int numero) {
	
	if (numero >= 0 && numero < 10) {
		return unidades[numero];
	} else if (numero >= 10 && numero < 100) {
		int decena = numero / 10;
		int unidad = numero % 10;
		
		if (unidad == 0) {
			return decenas[decena];
		} else {
			return decenas[decena] + unidades[unidad];
		}
	} else {
		cout << "N�mero fuera de rango";
	}
}

int main() {
		setlocale(LC_ALL, "");
	
		int numero;
		cout << "Ingrese un n�mero entre 0 y 99: ";
		cin >> numero;
		
		cout << "El n�mero " << numero << " en Romanos es: " << conversion(numero) << endl;
	return 0;
}
