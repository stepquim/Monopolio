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

if __name__ == '__main__':
    unittest.main()
