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

    #Test2 valida cuando una celda es propiedad, tiene dinero, decide
    #no comprar la propiedad y se continua el juego
    def test2(self):
        celda2 = Celda("", 2, "Propiedad", 100, 40)
        persona2 = Persona("Persona2", 130, "no")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2, persona2)
        self.assertEquals(msg, "Sigue jugando")

    #Test3 valida cuando una celda es propiedad, tiene dueño, tiene dinero para pagar la renta
    def test3(self):
        celda1 = Celda("Dueño1", 2, "Propiedad", 120, 35)
        persona1 = Persona("Persona2", 70, "no")
        juego1 = Juego()
        msg = juego1.validar_movimiento(celda1, persona1)
        self.assertEquals(msg, "Usted pago renta")

    #Test4 valida cuando una celda es propiedad, tiene dueño, no tiene dinero, pierde el juego
    def test4(self):
        celda4 = Celda("Dueño2", 2, "Propiedad", 120, 55)
        persona4 = Persona("Persona4", 30, "no")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4, persona4)
        self.assertEquals(msg,"Perdio")

    #Test5 valida cuando una celda es propiedad del mismo jugador
    def test5(self):
        celda5 = Celda("Propietario", 7, "Propiedad", 100, 40)
        persona5 = Persona("Propietario", 85, "")
        juego5 = Juego()
        msg = juego5.validar_movimiento(celda5, persona5)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

    #test6 valida cuando la celda no es una propiedad
    def test6(self):
        celda6 = Celda("", 2, "no_esPropiedad", 100, 0)
        persona6 = Persona("persona6", 100, "")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6, persona6)
        self.assertEquals(msg, "No Valido")

    #test7 valida cuando una celda es propiedad, no tiene dueño, quiere comprar, no tiene suficiente dinero
    def test7(self):
        celda7 = Celda("", 2, "Propiedad", 200, 60)
        persona7 = Persona("persona6", 50, "si")
        juego7 = Juego()
        msg = juego7.validar_movimiento(celda7, persona7)
        self.assertEquals(msg, "No tiene dinero suficiente")    


if __name__ == '__main__':
    unittest.main()
