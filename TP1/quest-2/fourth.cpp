#include <iostream>

using namespace std;

// Declarações de classes.
class Codigo {

private:
  int valor;

  static const int LIMITE = 100;

public:
  void set(int);

  int get();
};

class Preco {

private:
  int preco;

  static const int LIMITE = 200;

public:
  void set(int);

  int get();
};

class Pedido {
private:
  Codigo codigo;

  Preco preco;

public:
  void setCodigo(Codigo);

  void setPreco(Preco);

  Codigo getCodigo();

  Preco getPreco();
};
// Implementações de métodos.
inline int Codigo::get() { return valor; }

void Codigo::set(int valor) {

  if (valor > LIMITE)

    throw invalid_argument("Argumento invalido.");

  this->valor = valor;
}

inline int Preco::get() { return preco; }

void Preco::set(int preco) {

  if (preco > LIMITE)

    throw invalid_argument("Argumento invalido.");

  this->preco = preco;
}

void Pedido::setCodigo(Codigo codigo) { this->codigo = codigo; }

void Pedido::setPreco(Preco preco) { this->preco = preco; }

Codigo Pedido::getCodigo() { return codigo; }

Preco Pedido::getPreco() { return preco; }

// Função main.

int main() {

  int dadoA, dadoB;

  cin >> dadoA;

  cin >> dadoB;

  Codigo codigo;

  Preco preco;

  try {

    codigo.set(dadoA);

    preco.set(dadoB);

  }

  catch (invalid_argument &excecao) {

    cout << "FALHA";

    return 0;
  }

  Pedido pedido;

  pedido.setCodigo(codigo);

  pedido.setPreco(preco);

  cout << pedido.getCodigo().get();

  cout << pedido.getPreco().get();

  return 0;
}