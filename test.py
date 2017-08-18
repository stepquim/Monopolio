import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda1 = Celda("", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toreto", 160,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted ha comprado una propiedad")
        
    def test2(self):
            celda1 = Celda("", 1, "cualquier_cosa", 150, 50)
            persona1 = Persona("Toreto", 160,"si")
            juego = Juego()
            msg = juego.validar_movimiento(celda1,persona1)
            self.assertEquals(msg,"No Valido")

    #No tiene dinero suficiente
    def test3(self):
        celda1 = Celda("", 1, "Propiedad", 200, 50)
        persona1 = Persona("Toreto", 160,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"No tiene dinero suficiente")

    #Usted ha comprado una propiedad
    def test4(self):
        celda1 = Celda("", 1, "Propiedad", 160, 50)
        persona1 = Persona("Toreto", 200,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    #Sigue jugando
    def test5(self):
        celda1 = Celda("", 1, "Propiedad", 160, 50)
        persona1 = Persona("Toreto", 200,"no")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Sigue jugando")

    #Esta proiedad es suya, continua jugando
    def test6(self):
        celda1 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toreto", 160,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Esta proiedad es suya, continua jugando")

    def test7(self):
        celda1 = Celda("Saul", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toti", 10,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Perdio")

    def test8(self):
        celda1 = Celda("Saul", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toti", 100,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted pago renta")
        
if __name__ == '__main__':
    unittest.main()
