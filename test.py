import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):


    #Test1 valida si no es una propiedad
    def test1(self):
        celda3 = Celda("", 1, "Propiedadddd", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No Valido")

    #Test2 valida si es una propiedad y no tiene monto suficiente
    def test2(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 100,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")

    #Test3 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    #Test4 valida cuando es una propiedad, tiene dinero, y no decide comprar la propiedad
    def test4(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")

    #Test5 valida cuando es una propiedad, el dueño no es vacio y el dueño de la celda es igual al turno de la persona
    def test5(self):
        celda3 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")

    #Test6 valida cuando es una propiedad, el dueño no es vacio, el dueño de la celda no es igual al turno de la persona y monto es menor que renta
    def test6(self):
        celda3 = Celda("asd", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 10,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Perdio")

    #Test7 valida cuando es una propiedad, el dueño no es vacio, el dueño de la celda no es igual al turno de la persona y monto es mayor que renta
    def test7(self):
        celda3 = Celda("asd", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 70,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted pago renta")

if __name__ == '__main__':
    unittest.main()
