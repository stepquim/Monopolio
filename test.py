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

    #Test2 valida cuando es una propiedad, la propiedad tiene dueno, no tiene dinero para la renta entonces sale del juego.
    def test2(self):
        celda6 = Celda("Juan", 1, "Propiedad", 150, 50)
        persona6 = Persona("Claudia", 40,"no")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6,persona6)
        self.assertEquals(msg,"Perdio")

if __name__ == '__main__':
    unittest.main()
