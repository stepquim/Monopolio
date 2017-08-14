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
		
		
class Test2(unittest.TestCase):
    #Test2 valida que no es una propiedad
    def test2(self):
        celda2 = Celda("", 2, "Carcel", 100, 60)
        persona2 = Persona("Christian", 160,"si")
        juego2= Juego()
        msg = juego2.validar_movimiento(celda2,persona2)
        self.assertEquals(msg,"No Valido")

class Test4(unittest.TestCase):
    #Test1 valida cuando es una propiedad, no tiene dinero
    def test2(self):
        celda4 = Celda("", 3, "Propiedad", 150, 60)
        persona4 = Persona("Christian", 100,"si")
        juego4= Juego()
        msg = juego4.validar_movimiento(celda4,persona4)
        self.assertEquals(msg,"No tiene dinero suficiente")

class Test5(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")
		
if __name__ == '__main__':
    unittest.main()
