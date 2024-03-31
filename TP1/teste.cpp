#include <iostream>

#include <cmath>

using namespace std;

class SolidoGeometrico{

    public:

        virtual void desenhar() = 0;

        virtual float calcularArea() = 0;

        virtual float calcularVolume() = 0;

};

class Esfera:public SolidoGeometrico {

    private:

        float raio;

    public:

        Esfera(float);

        float calcularArea();

        float calcularVolume();

};

inline Esfera::Esfera(float raio){

    this->raio = raio;

}

inline float Esfera::calcularArea(){

    return (4 * M_PI * pow(raio, 2));

}

inline float Esfera::calcularVolume(){

    return ((4 * M_PI * pow(raio, 3))/3);

}

int main() {

    Esfera esfera(10);

    cout << "Area   = " << esfera.calcularArea()   << endl;

    cout << "Volume = " << esfera.calcularVolume() << endl;

    return 0;

}