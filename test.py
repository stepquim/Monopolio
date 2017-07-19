import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego. (2,4,5,7,8       )
    def test1(self):
        print("test1")
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")
        print("\n")

    # Test2 valida cuando la celda NO es una propiedad (2,3,14)
    def test2(self):
        print("test2")
        celda3 = Celda("", 1, "Carcel", 150, 50)
        persona3 = Persona("Toreto", 160, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "No Valido")
        print("\n")

    # Test3 valida cuando es una propiedad, sin dueño, monto es menor al precio (2,4,5,6,14)
    def test3(self):
        print("test3")
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 100, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "No tiene dinero suficiente")
        print("\n")

        # Test4 valida cuando es una propiedad  y le pertenece al mismo jugador (2,4,9,10,14)
    def test4(self):
        print("test4")
        celda3 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 100, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")
        print("\n")

    # Test5 valida cuando es una propiedad, con dueño distinto al mismo jugador y el monto es menor a la renta (2,4,9,11,12,14)
    def test5(self):
        print("test5")
        celda3 = Celda("Totora", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 20, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Perdio")
        print("\n")

    # Test6 valida cuando es una propiedad, con dueño distinto al mismo jugador y el monto es mayor igual a la renta (2,4,9,11,13,14)
    def test6(self):
        print("test6")
        celda3 = Celda("Totora", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 200, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Usted pago renta")
        print("\n")

if __name__ == '__main__':
    unittest.main()
