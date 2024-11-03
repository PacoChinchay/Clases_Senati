#include <iostream>

using namespace std;

string unidades[] = {"", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"};
string especiales[] = {"diez", "once", "doce", "trece", "catorce", "quince", "diecis�is", "diecisiete","dieciocho", 
						"deicinueve", "veintid�s", "veintitr�s", "veintis�is"};
string decenas[] ={"", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"};

string conversion(int numero) {
	if (numero >= 0 && numero < 10) {
		return unidades[numero];
	} else if (numero >= 10 && numero < 20) {
		return especiales[numero - 10];
	} else if (numero >= 20 && numero < 100) {
		int decena = numero / 10;
		int unidad = numero % 10;
		
		if (unidad == 0) {
			return decenas[decena];
		} else {
			return decenas[decena] + " y " + unidades[unidad];
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
		
		cout << "El n�mero " << numero << " en letras es: " << conversion(numero) << endl;
	return 0;
}
