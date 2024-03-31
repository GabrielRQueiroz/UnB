#include <iostream>

using namespace std;

class Codigo {

private:
  // Declaração de atributo.
  int valor;

public:
  bool set(int);

  int get();
};

// Implementações de métodos.
bool Codigo::set(int valor) {

  if (valor % 2 != 0) {

    return false;
  }

  this->valor = valor;

  return true;
}

int Codigo::get() { return this->valor; }

int main() {

  Codigo codigo;

  int valor;

  cin >> valor;

  if (valor % 2 == 0 && codigo.set(valor) && codigo.get() == valor) {

    cout << "SUCESSO";

    return 0;
  }

  if (valor % 2 != 0 && !codigo.set(valor) && codigo.get() != valor) {

    cout << "SUCESSO";

    return 0;
  }

  cout << "FALHA";

  return 0;
}