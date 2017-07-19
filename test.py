import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

##class Celda:dueno,numero,tipo,precio,renta
##class Persona:nombre,monto,comprar


class Test(unittest.TestCase):
    #Test1 valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    def test1(self):
        celda1 = Celda("", 1, "Propiedad", 150, 50)
        persona1 = Persona("Toreto", 160,"si")
        juego1 = Juego()
        msg = juego1.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Usted ha comprado una propiedad")
    #Test 2 valida cuando es una propiedad
    def test2(self):
        celda2=Celda("",1,"NOPROPIEDAD",150,50)
        persona2 = Persona("Toreto", 160, "si")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2, persona2)
        self.assertEquals(msg, "No valido")
    #Test3 cuando no tiene dueño y no tiene dinero para comprar, aunque si desee comprar
    def test3(self):
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        persona3 = Persona("Toreto", 100, "si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3, persona3)
        self.assertEquals(msg, "No tiene dinero suficiente")
    #Test4 cuando tiene dinero para comprar pero no desea
    def test4(self):
        celda4 = Celda("", 1, "Propiedad", 150, 50)
        persona4 = Persona("Toreto", 200, "no")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4, persona4)
        self.assertEquals(msg, "Sigue jugando")

    #Cuando la ficha tiene dueño
    #Test5 cuando dueño es el mismo jugador
    def test5(self):
        celda5 = Celda("Toreto", 1, "Propiedad", 150, 50)
        persona5 = Persona("Toreto", 200, "si")
        juego5 = Juego()
        msg = juego5.validar_movimiento(celda5, persona5)
        self.assertEquals(msg, "Esta proiedad es suya, continua jugando")

    #Cuando dueño es el otro jugador
    #Test 6 Cuando el jugador tiene menos dinero que el costo de renta
    def test6(self):
        celda6 = Celda("O'Connell", 1, "Propiedad", 150, 50)
        persona6 = Persona("Toreto", 25, "si")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6, persona6)
        self.assertEquals(msg, "Perdio")

    # Test 7 Cuando el jugador tiene menos dinero que el costo de renta
    def test7(self):
        celda7 = Celda("O'Connell", 1, "Propiedad", 150, 50)
        persona7 = Persona("Toreto", 250, "si")
        juego7 = Juego()
        msg = juego7.validar_movimiento(celda7, persona7)
        self.assertEquals(msg, "Usted pago renta")

if __name__ == '__main__':
    unittest.main()
