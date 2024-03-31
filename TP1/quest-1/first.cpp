#include <iostream>

using namespace std;

class Codigo {

     private:

          int valor;

     public:

          void set(int);

          int get();

};

// Implementações de métodos.

void Codigo::set (int valor){

     this->valor = valor;

}

int Codigo::get(){

     return this->valor;

}


int main(){

     Codigo codigo; 

    int valor;

    cin >> valor;

     codigo.set(valor);

    cout << codigo.get();

    return 0;

}