#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
	char *lista[3];
	char aux[20];
	int longitud;
	
	for(int i = 0; i < 3; i++) {
		printf("\npalabra %d: ", i);
		scanf("%s", aux);
		longitud = strlen(aux);
		lista[i] = (char *) malloc(longitud);
		strcpy(lista[i], aux); //(destino, origen)
	}
	
	//Mostar lista
	printf("\n**********");
	printf("\n  LISTA  ");
	printf("\n**********");
	for(int i = 0; i < 3; i++) {
		printf("\n %d .- %s", i, *(lista+i));
	}
}
