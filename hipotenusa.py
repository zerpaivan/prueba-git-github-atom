# script para calcular la hipotenusa de un triangulo
from math import sqrt


def hipotenusa(b, h):
    hip = sqrt(b ** 2 + h ** 2)
    return hip


if __name__ == "__main__":

    b = 3
    h = 4
    print("la hipotenusa es: ", hipotenusa(b, h))
