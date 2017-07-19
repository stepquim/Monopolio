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
    #Test2 valida cuando no es una propiedad.
    def test2(self):
        celda3 = Celda("", 1, "Carcel", 0, 0)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"la celda no es una Propiedad")
    # Test3 valida cuando es una propiedad, no tiene dinero.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 60, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "No tiene dinero suficiente")
    # Test4 valida cuando es una propiedad, si tiene dinero, decide no comprar la propiedad.
    def test4(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Sigue jugando")
    # Test5 valida cuando es una propiedad, el es el dueño.
    def test5(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

if __name__ == '__main__':
    unittest.main()
