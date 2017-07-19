import unittest

from Monopolio import *


#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

#CC = 6 + 1 = 7
class Test(unittest.TestCase):

    #Test 1: Valida cuando no es una propiedad
    def test1(self):
        celdaT1 = Celda("", 1, "No propiedad", 0, 0)
        personaT1 = Persona("Edison", 160, "no")
        juegoT1 = Juego()
        msg = juegoT1.validar_movimiento(celdaT1, personaT1)
        self.assertEquals(msg, "No Valido")

    #Test 2: Valida cuando es propiedad, no tiene dueño, no tiene dinero suficiente
    def test2(self):
        celdaT2 = Celda("", 1, "Propiedad", 150, 50)
        personaT2 = Persona("Edison", 100, "si")
        juegoT2 = Juego()
        msg = juegoT2.validar_movimiento(celdaT2, personaT2)
        self.assertEquals(msg, "No tiene dinero suficiente")


    #Test3 valida cuando es una propiedad, no tiene dueño, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test3(self):
        celdaT3 = Celda("", 1, "Propiedad", 150, 50)
        personaT3 = Persona("Toreto", 160,"si")
        juegoT3 = Juego()
        msg = juegoT3.validar_movimiento(celdaT3,personaT3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    #Test4 valida cuando es una propiedad, no tiene dueño, tiene dinero, no decide comprar la propiedad entonces continua en el juego.
    def test4(self):
        celdaT4 = Celda("", 1, "Propiedad", 150, 50)
        personaT4 = Persona("Edison", 160, "no")
        juegoT4 = Juego()
        msg = juegoT4.validar_movimiento(celdaT4, personaT4)
        self.assertEquals(msg, "Sigue jugando")

    #Test 5: Valida cuando es una propiedad, tiene dueño, mismo dueño
    def test5(self):
        celdaT5 = Celda("Edison", 1, "Propiedad", 150, 50)
        personaT5 = Persona("Edison", 160, "no")
        juegoT5 = Juego()
        msg = juegoT5.validar_movimiento(celdaT5, personaT5)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

    #Test 6: Valida cuando es una propiedad, tiene dueño, no soy el dueño, no tengo dinero suficiente para pagar la renta
    def test6(self):
        celdaT6 = Celda("Veronica", 1, "Propiedad", 150, 50)
        personaT6 = Persona("Edison", 40, "no")
        juegoT6 = Juego()
        msg = juegoT6.validar_movimiento(celdaT6, personaT6)
        self.assertEquals(msg, "Perdio")

    #Test 7: Valida cuando es propiedad, tiene dueño, no soy el dueño, si tengo dinero para pagar la renta
    def test7(self):
        celdaT7 = Celda("Veronica", 1, "Propiedad", 150, 50)
        personaT7 = Persona("Edison", 100, "no")
        juegoT7 = Juego()
        msg = juegoT7.validar_movimiento(celdaT7, personaT7)
        self.assertEquals(msg, "Usted pago renta")

if __name__ == '__main__':
    unittest.main()
