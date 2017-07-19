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


    def test2(self):
        celda = Celda("jose", 2 , "Propiedad", 200, 50)
        persona = Persona("raul", 25, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda,persona)
        self.assertEquals(msg,"Perdio")

    def test3(self):
        celda = Celda("jose", 2 , "Propiedad", 200, 50)
        persona = Persona("raul", 100, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda,persona)
        self.assertEquals(msg,"Usted pago renta")

    def test4(self):
        celda = Celda("jose", 2 , "Propiedad", 200, 50)
        persona = Persona("jose", 100, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda,persona)
        self.assertEquals(msg,"Esta propiedad es suya, continua jugando")

    def test5(self):
        celda = Celda("jose", 2 , "Camara", 200, 50)
        persona = Persona("jose", 100, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda,persona)
        self.assertEquals(msg,"No Valido")

    def test6(self):
        celda = Celda("", 1, "Propiedad", 150, 50)
        persona = Persona("Toreto", 100,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda,persona)
        self.assertEquals(msg,"No tiene dinero suficiente")

    def test7(self):
        celda = Celda("", 1, "Propiedad", 150, 50)
        persona = Persona("Toreto", 200,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda,persona)
        self.assertEquals(msg,"Sigue jugando")





if __name__ == '__main__':
    unittest.main()
