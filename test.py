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

    #Test2 valida cuando es una propiedad, esta libre  y no tiene dinero para comprarla pero trata de comprarla.
    def test2(self):
        celda=Celda("",2, "Propiedad",150,50)
        persona= Persona("Carlos",140,"si")
        juego=Juego()
        msg=juego.validar_movimiento(celda,persona)
        self.assertEquals(msg,"No tiene dinero suficiente")

    # Test3 valida cuando es una propiedad, tiene dinero, decide NO comprar la propiedad entonces continua en el juego.
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 160, "No")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Sigue jugando")

    # Test4 valida cuando No es una propiedad
    def test4(self):
        celda3 = Celda("", 1, "Especial", 0, 0)
        persona3 = Persona("Toreto", 160, "No")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "No Valido")


     # Test 5 valida cuando la propiedad en la que cae ya tiene duenho, pero es el mismo jugador
    def test5(self):
        celda3 = Celda("Carlos", 1, "Propiedad", 150, 50)
        persona3 = Persona("Carlos", 160, "No")
        juego=Juego()
        msg=juego.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")


    # Test 6 valida cuando la propiedad en la que cae ya tiene duenho, pero el jugador no puede pagar el valor de la renta

    def test6(self):
        celda3 = Celda("Carlos", 1, "Propiedad", 500, 250)
        persona3 = Persona("Luis", 160, "No")
        juego = Juego()
        msg = juego.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Perdio")

    # Test 7 valida cuando la propiedad en la que cae ya tiene duenho, y el jugador paga la renta
    def test7(self):
        celda3 = Celda("Carlos", 1, "Propiedad", 400, 150)
        persona3 = Persona("Luis", 160, "No")
        juego = Juego()
        msg = juego.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "Usted pago renta")

if __name__ == '__main__':
    unittest.main()
