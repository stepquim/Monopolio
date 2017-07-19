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

    # Test3 valida cuando es una propiedad que no tiene dueño, no tiene dinero suficiente para comprar entonces sale del juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 200, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")

    #Test4 valida cuando es una propiedad que no tiene dueño, tiene dinero, no desea comprar la propiedad entonces continua en el juego.
    def test4(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")

    #Test5 valida cuando es una propiedad cuyo dueño es él mismo.
    def test5(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")

    #Test6 valida cuando es una propiedad que tiene dueño y monto de la Persona es menor que valor de pago de renta.
    def test6(self):
        celda3 = Celda("Goku", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 40,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Perdio")

    # Test7 valida cuando es una propiedad que tiene dueño y monto de la Persona es mayor que valor de pago de renta, entonces la paga.
    def test7(self):
        celda3 = Celda("Goku", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 200,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted pago renta")

if __name__ == '__main__':
    unittest.main()
