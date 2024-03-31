#include <iostream>

using namespace std;

class Estudante {

     private:

     // Declarações de atributos.



     public:    

          Estudante(string);

          static int getContador();

          string getNome();

};

// Implementações de métodos.



int Estudante::contador = 0;

int main(){

     string nomeA, nomeB;   

     cin >> nomeA;

     cin >> nomeB;

     cout << Estudante::getContador();

     Estudante estudanteA(nomeA);

     cout << Estudante::getContador();

     cout << estudanteA.getNome();  

     Estudante estudanteB(nomeB);    

     cout << Estudante::getContador();

     cout << estudanteB.getNome();  

     return 0;

}