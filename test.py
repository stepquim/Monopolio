import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda1 = Celda("", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toreto", 160,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted ha comprado una propiedad")
		
if __name__ == '__main__':
    unittest.main()
