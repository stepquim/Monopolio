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
	
	def test2(self):
		celda3 = Celda("", 1, "algo", 150, 50)
		persona3 = Persona("Toreto", 160,"si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3,persona3)
		self.assertEquals(msg,"No Valido")
	
	def test3(self):
		celda3 = Celda("", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 100,"si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3,persona3)
		self.assertEquals(msg,"No tiene dinero suficiente")
		
	def test4(self):
		celda3 = Celda("", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 160,"no")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3,persona3)
		self.assertEquals(msg,"Sigue jugando")
	
	def test5(self):
		celda3 = Celda("Toreto", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 160,"no")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3,persona3)
		self.assertEquals(msg,"Esta proiedad es suya, continua jugando")
	
	def test6(self):
		celda3 = Celda("Joyce", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 40,"si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3,persona3)
		self.assertEquals(msg,"pierde el juego no tiene dinero para pagar")
	
if __name__ == '__main__':
    unittest.main()
