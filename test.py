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
if __name__ == '__main__':
    unittest.main()


class Test(unittest.TestCase):
    #Test2 valida cuando no es una propiedad
    def test2(self):
        celda3 = Celda("", 1, "NoPropiedad", 150, 50)
        persona3 = Persona("Fergie", 40,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"la celda no es una Propiedad")
if __name__ == '__main__':
    unittest.main()

class Test(unittest.TestCase):
    #Test3 valida cuando  es una propiedad y no tiene suficiente dinero
    def test2(self):
        celda3 = Celda("Alan", 1, "Propiedad", 250, 130)
        persona3 = Persona("Edison", 100,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")
if __name__ == '__main__':
    unittest.main()

class Test(unittest.TestCase):
    #Test4 valida cuando  es una propiedad y ya es mi propiedad
    def test2(self):
        celda3 = Celda("Sara", 1, "Propiedad", 250, 130)
        persona3 = Persona("Sara", 300,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")
if __name__ == '__main__':
    unittest.main()

class Test(unittest.TestCase):
    #Test5 valida cuando  es una propiedad,tiene dueño y no tengo dinero para la renta
    def test2(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 250, 130)
        persona3 = Persona("Sara", 100,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"pierde el juego no tiene dinero para pagar")
if __name__ == '__main__':
    unittest.main()

class Test(unittest.TestCase):
    #Test6 valida cuando  es una propiedad,tiene dueño y aun tengo dinero para la renta
    def test2(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 250, 130)
        persona3 = Persona("Alan", 200,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted pago renta")
if __name__ == '__main__':
    unittest.main()
class Test(unittest.TestCase):
    #Test7 valida cuando  es una propiedad, no tiene dueño y  tengo dinero pero no se desea comprar
    def test2(self):
        celda3 = Celda("", 1, "Propiedad", 250, 130)
        persona3 = Persona("Fergie", 300,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")
if __name__ == '__main__':
    unittest.main()