#include <iostream>

#include <stdexcept>

using namespace std;

#define TAMANHO_MAXIMO 5

class Nome {

private:
  // Declaração de atributo.
  string nome;

  void validar(string);

public:
  void set(string);

  string get();
};

// Implementações de métodos.
void Nome::validar(string nome) {
  if (nome.length() > TAMANHO_MAXIMO) {
    throw invalid_argument("Argumento invalido.");
  }
}

void Nome::set(string nome) {
  validar(nome);

  this->nome = nome;
}

inline string Nome::get() { return this->nome; }

int main() {

  string dadoA, dadoB;

  cin >> dadoA;

  cin >> dadoB;

  Nome nome;

  try {

    nome.set(dadoA);

  }

  catch (invalid_argument &excessao) {

    cout << excessao.what();
  }

  try {

    nome.set(dadoB);

  }

  catch (invalid_argument &excessao) {

    cout << excessao.what();
  }

  return 0;
}