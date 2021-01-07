#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
	int puntuacion;
	int cont;
	int resultados[6];
	
	srand(time(0));
	for(cont=1; cont<= 6000; cont++){
		puntuacion = rand()%6+1;
		resultados[puntuacion-1] = resultados[puntuacion-1] + 1;
	}
	
	//Mostrar resultados
	for(cont=0; cont < 6; cont++){
		printf("resultados[%d]=%d \n", cont, resultados[cont]);
	}
	
	return 0;
}
