import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    # Test0 valida cuando es una propiedad, no tiene dueño, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test0(self):
        celda0 = Celda("", 1, "", 0, 0)
        persona0 = Persona("Fernando", 160, "")
        juego0 = Juego()
        msg = juego0.validar_movimiento(celda0, persona0)
        self.assertEquals(msg, "No Valido") #la celda no es una propiedad

    #Test1 valida cuando es una propiedad, no tiene dueño, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda1 = Celda("", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toreto", 160,"si")
        juego1 = Juego()
        msg = juego1.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    #Test2 valida cuando es una propiedad, no tiene dueño, tiene dinero, no decide comprar la propiedad entonces continua en el juego.
    def test2(self):
        celda2 = Celda("", 1, "Propiedad", 150, 50)
        persona2 = Persona("Fernando", 260,"no")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2,persona2)
        self.assertEquals(msg,"Sigue jugando")

    #Test3 valida cuando es una propiedad, no tiene dueño, no tiene dinero suficiente entonces sale del juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Fernando", 40,"no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente") #salio del juego

    # Test4 valida cuando es una propiedad, el dueño es el mismo jugardor entonces continua jugando.
    def test4(self):
        celda4 = Celda("Fernando", 1, "Propiedad", 150, 50)
        persona4 = Persona("Fernando", 160, "")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4, persona4)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")  #es el mismo dueño

    # Test5 valida cuando es una propiedad, tiene dueño, comprada por otros jugadores, tiene dinero.
    def test5(self):
        celda5 = Celda("Marcos", 1, "Propiedad", 150, 50)
        persona5 = Persona("Fernando", 260, "")
        juego5 = Juego()
        msg = juego5.validar_movimiento(celda5, persona5)
        self.assertEquals(msg, "Usted pago renta")  # paga la renta

    # Test6 valida cuando es una propiedad, tiene dueño, comprada por otros jugadores, no tiene dinero.
    def test6(self):
        celda6 = Celda("Marcos", 1, "Propiedad", 150, 50)
        persona6 = Persona("Fernando", 20, "")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6, persona6)
        self.assertEquals(msg, "Perdio")  #pierde el juego no tiene dinero para pagar
if __name__ == '__main__':
    unittest.main()