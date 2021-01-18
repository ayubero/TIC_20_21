#include <iostream>
using namespace std;

int a[3][3]; 
int b[3][3];

int main() { 
    num_filas = sizeof(a) / sizeof(a[0]);
    num_columnas = sizeof(a[0]) / sizeof(a[0][0]);
    
    cout << "Num de filas: " << num_filas << "\n";
	cout << "Num de columnas: " << num_columnas << "\n";
	
	//Establecer los valores de los elementos de las matrices
	for(int n = 0; n < num_filas; n++) {
		for(int m = 0; m < num_columnas; m++) {
			cout << "Fila " << n << " Columna " << m << " : ";
			cin >> x;
			a[n][m] = x;
			b[n][m] = x;
		}
	}
	
	//Mostar las matrices
	
	return 0;
}
