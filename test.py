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

            #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test2(self):
        celda3 = Celda("", 2, "Propiedad", 200, 200)
        persona3 = Persona("Zambrano", 5,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    def test3(self):
        celda3 = Celda("", 3, "Propiedad", 100, 200)
        persona3 = Persona("Cortez", 500,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    def test4(self):
        celda3 = Celda("", 4, "Cortez", 100, 200)
        persona3 = Persona("Cortez", 500,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Es el mismo comprador")
        
    def test5(self):
        celda3 = Celda("", 4, "Cortez", 0, 0)
        persona3 = Persona("Lopez", 500,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Es el mismo comprador")
if __name__ == '__main__':
    unittest.main()
