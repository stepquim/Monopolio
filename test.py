import unittest
from Monopolio import *

class Test(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")
		
    #Test21 valida cuando es No es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test2(self):
        celda3 = Celda("", 1, "Carrito", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"la celda no es una Propiedad")
		
if __name__ == '__main__':
    unittest.main()
