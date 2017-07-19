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




if __name__ == '__main__':
    unittest.main()
