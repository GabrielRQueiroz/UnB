#include <iostream>

using namespace std;

class Nome {

private:
  string nome;

public:
  void set(string);

  string get();
};

class Matricula {

private:
  int matricula;

public:
  void set(int);

  int get();
};

class Estudante {

private:
  Nome nome;

  Matricula matricula;

public:
  Estudante(Nome &, Matricula &);

  Nome getNome();

  Matricula getMatricula();
};

void Nome::set(string nome) {
  this->nome = nome;
}

string Nome::get() {
  return this->nome;
}

void Matricula::set(int matricula) {
  this->matricula = matricula;
}

int Matricula::get() {
  return this->matricula;
}

Estudante::Estudante(Nome &nome, Matricula &matricula) {
  this->nome = nome;

  this->matricula = matricula;
}

Nome Estudante::getNome() {
  return this->nome;
}

Matricula Estudante::getMatricula() {
  return this->matricula;
}


int main() {

  string dadoA;

  int dadoB;

  cin >> dadoA;

  cin >> dadoB;

  Nome nome;

  Matricula matricula;

  nome.set(dadoA);

  matricula.set(dadoB);

  Estudante estudante(nome, matricula);

  cout << estudante.getNome().get();

  cout << estudante.getMatricula().get();

  return 0;
}