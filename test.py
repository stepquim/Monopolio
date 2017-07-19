import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

#CC= 6 + 1 = 7

class Test(unittest.TestCase):
	#Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
	def test1(self):
		celda3 = Celda("", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 160,"si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3,persona3)
		self.assertEquals(msg,"Usted ha comprado una propiedad")

	# Test2 valida cuando es una propiedad, tiene dinero, no decide comprar la propiedad entonces continua en el juego.
	def test2(self):
		celda3 = Celda("", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 160, "no")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3, persona3)
		self.assertEquals(msg, "Sigue jugando")

	# Test3 valida cuando es una propiedad, no tiene dinero
	def test3(self):
		celda3 = Celda("", 1, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 120, "si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3, persona3)
		self.assertEquals(msg, "No tiene dinero suficiente")

	# Test4 valida cuando no es una propiedad
	def test4(self):
		celda3 = Celda("", 5, "Carcel", 0, 0)
		persona3 = Persona("Toreto", 120, "no")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3, persona3)
		self.assertEquals(msg, "No Valido")

	# Test5 valida cuando es una propiedad, tiene dueño, dueño es mismo jugador
	def test5(self):
		celda3 = Celda("Toreto", 2, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 120, "si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3, persona3)
		self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

	# Test6 valida cuando es una propiedad, tiene dueño, no es dueño el jugador, monto jugador menor a renta
	def test6(self):
		celda3 = Celda("Maria", 3, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 20, "si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3, persona3)
		self.assertEquals(msg, "Perdio")

	# Test7 valida cuando es una propiedad, tiene dueño, no es dueño el jugador, monto jugador mayor a renta
	def test7(self):
		celda3 = Celda("Maria", 3, "Propiedad", 150, 50)
		persona3 = Persona("Toreto", 70, "si")
		juego3 = Juego()
		msg = juego3.validar_movimiento(celda3, persona3)
		self.assertEquals(msg, "Usted pago renta")

if __name__ == '__main__':
	unittest.main()
