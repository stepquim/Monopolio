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
    #Test2 valida cuando la celda no es una propiedad
    def test2(self):
    	celda3 = Celda("", 1, "Ferrocarril", 150, 50)
    	persona3 = Persona("Toreto", 160,"si")
    	juego3 = Juego()
    	msg = juego3.validar_movimiento(celda3,persona3)
    	self.assertEquals(msg,"No Valido")
    #Test3 valida cuando la celda es una propiedad, el jugador no tiene dinero suficiente
    def test3(self):
    	celda3 = Celda("", 1, "Propiedad", 170, 50)
    	persona3 = Persona("Toreto", 160,"si")
    	juego3 = Juego()
    	msg = juego3.validar_movimiento(celda3,persona3)
    	self.assertEquals(msg,"No tiene dinero suficiente")
    #Test4 valida cuando la celda es una propiedad, la celda no tiene duenio, el jugador tiene dinero suficiente, el jugador decide no comprar la propiedad
    def test4(self):
    	celda3 = Celda("", 1, "Propiedad", 150, 50)
    	persona3 = Persona("Toreto", 160,"no")
    	juego3 = Juego()
    	msg = juego3.validar_movimiento(celda3,persona3)
    	self.assertEquals(msg,"Sigue jugando")
	#Test5 valida cuando la celda es una propiedad, la celda si tiene duenio, el duenio de la celda es el jugador
    def test5(self):
    	celda3 = Celda("Toreto", 1, "Propiedad", 150, 50)
    	persona3 = Persona("Toreto", 160,"no")
    	juego3 = Juego()
    	msg = juego3.validar_movimiento(celda3,persona3)
    	self.assertEquals(msg,"Esta proiedad es suya, continua jugando")
	#Test6 valida cuando la celda es una propiedad, la celda si tiene duenio, el duenio de la celda no es el jugador, el jugador no tiene dinero suficiente para pagar la renta
    def test6(self):
    	celda3 = Celda("Bryan", 1, "Propiedad", 150, 50)
    	persona3 = Persona("Toreto", 40,"no")
    	juego3 = Juego()
    	msg = juego3.validar_movimiento(celda3,persona3)
    	self.assertEquals(msg,"Perdio")
	#Test7 valida cuando la celda es una propiedad, la celda si tiene duenio, el duenio de la celda no es el jugador, el jugador tiene dinero suficiente para pagar la renta
    def test7(self):
    	celda3 = Celda("Bryan", 1, "Propiedad", 150, 50)
    	persona3 = Persona("Toreto", 60,"no")
    	juego3 = Juego()
    	msg = juego3.validar_movimiento(celda3,persona3)
    	self.assertEquals(msg,"Usted pago renta")
if __name__ == '__main__':
    unittest.main()
