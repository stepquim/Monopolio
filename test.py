import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    # Esta prueba valida si la celda no es de tipo propiedad
    def test1(self):
        celda1 = Celda("", 1, "Estado", 150, 50)
        persona1 = Persona("Juan", 200, "si")
        juego1 = Juego()
        msg = juego1.validar_movimiento(celda1, persona1)
        self.assertEqual(msg, "No Valido")

    #Esta prueba valida cuando la propiedad no tiene dueño, el monto de la persona es mayor a la propiedad y el turno de la persona le da Si a comprar.
    #Esta es la que viene con el repo.

    def test2(self):
        celda2 = Celda("", 1, "Propiedad", 150, 50)
        persona2 = Persona("Toreto", 160, "si")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2, persona2)
        self.assertEquals(msg, "Usted ha comprado una propiedad")

    #Esta prueba valida cuando la propiedad no tiene dueño, el monto de la persona es mayor al de la propiedad y el turno de la persona no dice Si a comprar

    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160, "no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Sigue jugando")

    #Esta prueba valida cuando la propiedad no tiene dueño y el monto de la persona es menor al valor de la propiedad
    def test4(self):
        celda4 = Celda("", 1, "Propiedad", 250, 50)
        persona4 = Persona("Toreto", 160, "si")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4, persona4)
        self.assertEquals(msg, "No tiene dinero suficiente")

    #Esta prueba valida que el dueño de la celda sea el mismo que el que está jugandp
    def test5(self):
        celda5 = Celda("Toreto", 1, "Propiedad", 250, 50)
        persona5 = Persona("Toreto", 160, "si")
        juego5 = Juego()
        msg = juego5.validar_movimiento(celda5, persona5)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

    #Esta prueba valida que el dueño de la celda no sea el mismo que el que está jugando y que la persona que esté jugando tenga un monto menor al valor de la renta de la propiedad
    def test6(self):
        celda6 = Celda("Toreto", 1, "Propiedad", 250, 250)
        persona6 = Persona("Fernando", 160, "si")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6, persona6)
        self.assertEquals(msg, "Perdio")

    #Esta prueba valida que el dueño de la celda no sea el mismo que el que está jugando y que la persona que esté jugando tenga un monto mayor al valor de la renta de la propiedad
    def test7(self):
        celda7 = Celda("Toreto", 1, "Propiedad", 250, 50)
        persona7 = Persona("Fernando", 160, "si")
        juego7 = Juego()
        msg = juego7.validar_movimiento(celda7, persona7)
        self.assertEquals(msg, "Usted pago renta")

if __name__ == '__main__':
    unittest.main()
