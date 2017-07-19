import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    #Test2 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test2(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160,"si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    # Test3 valida cuando no es una propiedad, por lo tanto retornará no valido.
    def test3(self):
        celda3 = Celda("", 1, "NoPropiedad", 150, 50) #celda.tipo = "No propiedad"
        persona3 = Persona("Toreto", 160, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "No Valido")

    # Test4 valida cuando es una propiedad, el monto de la persona es menor que el precio pro lo tanto no tiene dinero para comprar.
    def test4(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 120,"si") #monto de la persona = 120
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")

    # Test5 valida cuando es una propiedad, tiene dinero, pero decide no comprar la propiedad, entonces continua en el juego.
    def test5(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 180,"no") #decide no comprar, comprar = "no"
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")

    # Test6 valida cuando es una propiedad, tiene dueño, pero el dueño es el mismo jugador que tiene el turno.
    def test6(self):
        celda3 = Celda("Gabriel", 1, "Propiedad", 150, 50)
        persona3 = Persona("Gabriel", 180,"no") #persona "Gabriel" es igual al propiestario
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")


    # Test7 valida cuando es una propiedad, tiene dueño, y el jugador no tiene dinero para pagar la renta.
    def test7(self):
        celda3 = Celda("Gabriel", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 20, "no") #monto de persona menor al de la renta
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Perdio")

    # Test8 valida cuando es una propiedad, tiene dueño, y el jugador tiene dinero para pagar la renta, entonces continua el juego.
    def test8(self):
        celda3 = Celda("Gabriel", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 100, "no") #dinero de persona mayor a la ernta a pagar
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Usted pago renta")

if __name__ == '__main__':
    unittest.main()
