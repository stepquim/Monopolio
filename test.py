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

    # Test2 valida cuando no es una propiedad, tiene dinero y quiere comprarla.
    def test2(self):
        celda4 = Celda("", 2, "No Propiedad", 0, 0)
        persona4 = Persona("Toreto", 160,"si")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4,persona4)
        self.assertEquals(msg,"la celda no es una Propiedad")

    # Test3 valida cuando es una propiedad, no tiene dueño, no tiene dinero suficiente para comprar entonces sale del juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 200, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")
if __name__ == '__main__':
    unittest.main()
