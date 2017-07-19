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
	
    #Test2 valida cuando es una propiedad disponible, tiene dinero pero decide no comprarla	
    def test2(self):
        celda1 = Celda("", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toreto", 160,"no")
        juego1 = Juego()
        msg = juego1.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Sigue jugando")
		
    #Test3 valida cuando es una propiedad, no tiene dinero suficiente para comprarla
    def test3(self):
        celda2 = Celda("", 1, "Propiedad", 150, 50)
        persona2 = Persona("Toreto", 120,"si")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2,persona2)
        self.assertEquals(msg,"No tiene dinero suficiente")
		
    #Test4 valida cuando es una propiedad, pero el que cae en esa propiedad es el mismo dueño
    def test4(self):
        celda4 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona4 = Persona("Toreto", 120,"no")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4,persona4)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")
		
    #Test5 valida cuando es una propiedad, tiene dueño y paga la renta de la misma
    def test5(self):
        celda5 = Celda("Pepito", 1, "Propiedad", 150, 50)
        persona5 = Persona("Toreto", 120,"no")
        juego5 = Juego()
        msg = juego5.validar_movimiento(celda5,persona5)
        self.assertEquals(msg,"Usted pago renta")
	
    #Test6 valida cuando es una propiedad, tiene dueño, pero no tiene dinero para pagarla
    def test6(self):
        celda6 = Celda("Pepito", 1, "Propiedad", 150, 50)
        persona6 = Persona("Toreto", 20,"no")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6,persona6)
        self.assertEquals(msg,"Perdio")
		
    #Test7 valida cuando no es una propiedad
    def test7(self):
        celda7 = Celda("", 1, "Carcel", 150, 50)
        persona7 = Persona("Toreto", 120,"no")
        juego7 = Juego()
        msg = juego7.validar_movimiento(celda7,persona7)
        self.assertEquals(msg,"No Valido")	
		
if __name__ == '__main__':
    unittest.main()
