#include <iostream>
using namespace std;

int a[3][3]; 
int b[3][3];
int c[3][3]; //Resultado

int num_filas = sizeof(a) / sizeof(a[0]);
int num_columnas = sizeof(a[0]) / sizeof(a[0][0]);

void operar(string operacion) {
    if (operacion == "+") {
        //Suma
        for(int n = 0; n < num_filas; n++) {
            for(int m = 0; m < num_columnas; m++) {
                c[n][m] = a[n][m] + b[n][m];
            }
        }
    }else if (operacion == "-") {
        //Resta
        for(int n = 0; n < num_filas; n++) {
            for(int m = 0; m < num_columnas; m++) {
                c[n][m] = a[n][m] - b[n][m];
            }
        }
    }

    //Mostrar resultado
    cout << "RESULTADO:\n";
    for(int n = 0; n < num_filas; n++) {
		for(int m = 0; m < num_columnas; m++) {
			cout << c[n][m] << "  ";
		}
        cout << "\n";
	}
}

int main() {
    cout << "Num de filas: " << num_filas << "\n";
	cout << "Num de columnas: " << num_columnas << "\n";
	
    //MATRIZ A
    cout << "MATRIZ A:\n";
	//Establecer los valores de los elementos de las matrices
	for(int n = 0; n < num_filas; n++) {
		for(int m = 0; m < num_columnas; m++) {
            int x;
			cout << "Fila " << n+1 << " Columna " << m+1 << " : ";
			cin >> x;
			a[n][m] = x;
		}
	}
	//Mostar las matrices
    for(int n = 0; n < num_filas; n++) {
		for(int m = 0; m < num_columnas; m++) {
			cout << a[n][m] << "  ";
		}
        cout << "\n";
	}

    //MATRIZ B
    cout << "MATRIZ A:\n";
	//Establecer los valores de los elementos de las matrices
	for(int n = 0; n < num_filas; n++) {
		for(int m = 0; m < num_columnas; m++) {
            int x;
			cout << "Fila " << n+1 << " Columna " << m+1 << " : ";
			cin >> x;
			b[n][m] = x;
		}
	}
	//Mostar las matrices
    for(int n = 0; n < num_filas; n++) {
		for(int m = 0; m < num_columnas; m++) {
			cout << b[n][m] << "  ";
		}
        cout << "\n";
	}

    //OPERAR
    string operacion;
    cout << "Introduzca + para sumar y - para restar las matrices: ";
    cin >> operacion;
    operar(operacion);
	
	return 0;
}
