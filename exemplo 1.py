import math

class esfera:

    def __init__(self,cor,raio):

        self.cor = cor
        self.raio = raio


    def volume(self):

        vol = (4/3)*math.pi*(self.raio**3)

        return vol


    def area(self,ar):

        ar = 4*math.pi*(self.raio**2)

    return area

bola1 = esfera('vermelha',4)
bola2 = esfera('azul',7)

print(f'O volume da bola 1 é {bola1.volume()}cm^3')
print(f'A área superficial da bola 1 é {bola1.area()}cm^2')

print(bola1.volume())
print(esfera.volume(bola1))
