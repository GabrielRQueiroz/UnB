#include <iostream>

using namespace std;

// Declarações das classes e implementações dos métodos.
class Elemento {
private:
  int dado;

  Elemento *proximo;

public:
  void setDado(int);

  void setProximo(Elemento *);

  int getDado();

  Elemento *getProximo();
};

class Fila {
private:
  Elemento *primeiro;

  Elemento *ultimo;

public:
  Fila();

  void inserir(Elemento *);

  Elemento *remover();
};

void Elemento::setDado(int dado) { this->dado = dado; }

void Elemento::setProximo(Elemento *proximo) { this->proximo = proximo; }

int Elemento::getDado() { return dado; }

Elemento *Elemento::getProximo() { return proximo; }

Fila::Fila() { primeiro = ultimo = NULL; }

void Fila::inserir(Elemento *elemento) {

  if (primeiro == NULL)

    primeiro = ultimo = elemento;

  else {

    ultimo->setProximo(elemento);

    ultimo = elemento;
  }
}

Elemento *Fila::remover() {

  Elemento *elemento = primeiro;

  if (primeiro == ultimo)

    primeiro = ultimo = NULL;

  else

    primeiro = primeiro->getProximo();

  return elemento;
}

int main() {

  Elemento elementoA, elementoB, elementoC;

  int dado;

  cin >> dado;

  elementoA.setDado(dado);

  cin >> dado;

  elementoB.setDado(dado);

  cin >> dado;

  elementoC.setDado(dado);

  Fila fila;

  fila.inserir(&elementoA);

  fila.inserir(&elementoB);

  fila.inserir(&elementoC);

  cout << fila.remover()->getDado();

  cout << fila.remover()->getDado();

  cout << fila.remover()->getDado();

  return 0;
}