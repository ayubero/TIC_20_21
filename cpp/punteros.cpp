#include<iostream>
using namespace std;

int main() {
	int x = 3;
	int *px = &x;
	
	cout << "Direccion de memoria: " <<  &x;
	cout << "\nValor: " << *px;
	
	return 0;
}
