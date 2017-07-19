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
        juego1 = Juego()
        msg = juego1.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    #Test2 valida cuando es una propiedad, tiene dinero, no decide comprar la propiedad entonces continua en el juego.
    def test2(self):
        celda2 = Celda("", 1, "Propiedad", 150, 50)
        persona2 = Persona("Fernando", 260,"no")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2,persona2)
        self.assertEquals(msg,"Sigue jugando")

    #Test3 valida cuando es una propiedad, no tiene dinero suficiente entonces sale del juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Fernando", 40,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente") #salio del juego

if __name__ == '__main__':
    unittest.main()