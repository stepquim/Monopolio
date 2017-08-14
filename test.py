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
    #Test4 valida cuando es una propiedad, no tiene dinero
    def test4(self):
        celda4 = Celda("", 3, "Propiedad", 150, 60)
        persona4 = Persona("Christian", 100,"si")
        juego4= Juego()
        msg = juego4.validar_movimiento(celda4,persona4)
        self.assertEquals(msg,"No tiene dinero suficiente")

class Test5(unittest.TestCase):
    #Test5 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test5(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")

class Test6(unittest.TestCase):
    #Test6 valida cuando es una propiedad, es el mismo dueño
    def test6(self):
        celda6 = Celda("Christian", 1, "Propiedad", 150, 50)
        persona6 = Persona("Christian", 160,"no")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6,persona6)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")

class Test7(unittest.TestCase):
    def test7(self):
        celda7 = Celda("Christian", 3, "Propiedad", 150, 60)
        persona7 = Persona("Christian", 100,"si")
        juego7= Juego()
        msg = juego7.validar_movimiento(celda7,persona7)
        self.assertEquals(msg,"Perdio")

class Test8(unittest.TestCase):
    #Test7 valida cuando es una propiedad, no tiene dinero
    def test8(self):
        celda8 = Celda("Christian", 3, "Propiedad", 150, 60)
        persona8 = Persona("Christian", 180,"si")
        juego8= Juego()
        msg = juego8.validar_movimiento(celda8,persona8)
        self.assertEquals(msg,"Usted pago renta")
		
if __name__ == '__main__':
    unittest.main()
