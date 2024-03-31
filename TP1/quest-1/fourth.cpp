#include <iostream>

using namespace std;

class Estudante {

private:
  // Declarações de atributos.
  static int contador;
  string nome;

public:
  Estudante(string);

  static int getContador();

  string getNome();
};

// Implementações de métodos.
Estudante::Estudante(string nome) {
  this->nome = nome;
  this->contador++;
}

int Estudante::getContador() { return Estudante::contador; }

string Estudante::getNome() { return this->nome; }

int Estudante::contador = 0;

int main() {

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