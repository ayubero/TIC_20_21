#include<stdio.h>

int main() {
	int numeros[10];
	int cont;
	int veces;
	int pos;
	int bolsillo;
	printf("\nIntroduzca 10 numeros enteros: ");
	for(cont = 0; cont < 10; cont++) {
		printf("\nNumero %d: ", cont);
		scanf("%d", &numeros[cont]);
	}
	for(veces = 0; veces < 10; veces++) {
		for(pos = 0; pos < 9; pos++) {
			if(numeros[pos] > numeros[pos+1]) {
				//Intercambiamos
				bolsillo = numeros[pos];
				numeros[pos] = numeros[pos+1];
				numeros[pos+1] = bolsillo;
			}
		}
	}
	//Mostrar
	printf("\nORDENADA: ");
	for(cont = 0; cont < 10; cont++) {
		printf("\nNumero %d: ", numeros[cont]);
	}
	
	return 0;
}
