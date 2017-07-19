import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")


    #Test2 valida cuando no es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test2(self):
        celda3 = Celda("", 1, "Cualquier Cosa", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No Valido")

    #Test3 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad que es mas cara que su monot entonces sale del juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 140,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")

    #Test4 valida cuando es una propiedad, tiene dinero, decide no comprar la propiedad entonces continua en el juego.
    def test4(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")

    #Test5 valida cuando es una propiedad, tiene dinero, decide no comprar la propiedad entonces continua en el juego.
    def test5(self):
        celda3 = Celda("ruben", 1, "Propiedad", 150, 50)
        persona3 = Persona("ruben", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")

    #Test6 valida cuando es una propiedad, tiene dinero, decide no comprar la propiedad entonces continua en el juego.
    def test6(self):
        celda3 = Celda("jose", 1, "Propiedad", 150, 50)
        persona3 = Persona("ruben", 10,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Perdio")

    #Test7 valida cuando es una propiedad, tiene dinero, decide no comprar la propiedad entonces continua en el juego.
    def test7(self):
        celda3 = Celda("jose", 1, "Propiedad", 150, 50)
        persona3 = Persona("ruben", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted pago renta")

if __name__ == '__main__':
    unittest.main()
