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

     # Test2 valida cuando no es una propiedad, tiene dinero, desea comprar pero no es valido la compra.
    def test2(self):
        celda4 = Celda("", 1, "casualidad", 0, 0)
        persona4 = Persona("Julio", 300, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda4, persona4)
        self.assertEquals(msg, "No Valido")

    # Test3 valida cuando es una propiedad, no tiene dinero, pierde por no poder comprar y sale del juego.

    def test3(self):
        celda5 = Celda("", 3, "Propiedad", 250, 50)
        persona5 = Persona("Roberto", 150, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda5, persona5)
        self.assertEquals(msg, "No tiene dinero suficiente")

    # Test4 valida cuando es una propiedad, si tiene dinero, no decide comprarla y sigue el juego.
    def test4(self):
        celda3 = Celda("", 2, "Propiedad", 250, 50)
        persona3 = Persona("Victor", 360, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Sigue jugando")

    # Test5 valida cuando es una propiedad, si tiene dinero, pero ya le pertenece y continua el juego.
    def test5(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 250, 50)
        persona3 = Persona("Toreto", 160, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

    # Test6 valida cuando es una propiedad, no tiene dinero, no es dueno y no puede pagar la renta por lo tanto pierde el juego.
    def test6(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 250, 50)
        persona7 = Persona("Gabriel", 20, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona7)
        self.assertEquals(msg, "Perdio")

    # Test7 valida cuando es una propiedad, si tiene dinero, no es dueno y  puede pagar la renta.
    def test7(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 250, 50)
        persona7 = Persona("Julio", 300, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona7)
        self.assertEquals(msg, "Usted pago renta")


if __name__ == '__main__':
    unittest.main()
