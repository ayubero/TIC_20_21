#include <iostream>
using namespace std;

void dibujarLateral(int valor) {
    for (int l = 0; l < valor; l++) {
        cout << " ";
    }
}

int main(){
    int altura;

    cout << "Escribe un numero entero para calcular la altura del arbol: ";
    cin >>altura;

    int ancho_max = 2*altura - 1; //Base del árbol

    for (int i = 1; i <= altura; i++){
        int ancho = 2*i - 1; //Ancho del arbol en esa fila
        int lateral = (ancho_max - ancho) / 2; //Espacio dejado a cada lado de cada fila del arbol

        //Dibujar lateral izquierdo
        dibujarLateral(lateral);

        //Dibujar fila del arbol
        for (int a = 0; a < ancho; a++) {
            cout << "@";
        }

        //Dibujar lateral derecho
        dibujarLateral(lateral);

        cout << "\n"; //Salto de linea
    }

    //Dibujar tronco
    int lateral_base = (ancho_max - 1) / 2;
    dibujarLateral(lateral_base);
    cout << "‖";
    dibujarLateral(lateral_base);
}
