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

    #Test2 valida si la celda no es del tipo propiedad, por lo que no es valido
    def test2(self):
        celda2 = Celda("", 1, "Nada",0,0)
        persona2 = Persona("Oscar", 200, "no")
        juego2 = Juego()
        msg = juego2.validar_movimiento(celda2, persona2)
        self.assertEqual(msg, "No Valido")

    #Test3 valida si la persona no tiene el monto suficiente para comprar la "celda", el resultado debe salir que "No tiene dinero suficiente"
    #Para que cumpla la condicion,  la celda no tiene dueno y el precio debe ser superior al monto de la persona
    def test3(self):
        celda = Celda("", 1, "Propiedad", 200, 50)
        persona = Persona("Oscar", 100, "si")
        juego = Juego()
        msg = juego.validar_movimiento(celda, persona)
        self.assertEqual(msg, "No tiene dinero suficiente")

    #Test 4 valida  si la persona es el mi dueno de la celda
    #Para que cumpla la condicion, los parametros Persona.nombre y Celda.dueno deben ser Strings iguales
    def test4(self):
        celda4 = Celda("Oscar", 2, "Propiedad", 200, 50)
        persona4 = Persona("Oscar", 200, "si")
        juego4 = Juego()
        msg = juego4.validar_movimiento(celda4, persona4)
        self.assertEqual(msg, "Esta proiedad es suya, continua jugando")

    #Test 5 valida si el monto de la persona es menor al de la renta.
    # Si es cierto, la persona pierde el juego.
    def test5(self):
        celda5 = Celda("Pepe", 3, "Propiedad", 250, 100)
        persona5 = Persona("Oscar", 90, "si")
        juego5 = Juego()
        msg = juego5.validar_movimiento(celda5, persona5)
        self.assertEqual(msg, "Perdio")

    #Test 6 valida si el monto de la persona que cae en la celda, es mayor a su renta
    #Si es cierto, la persona paga la renta
    def test6(self):
        celda6 = Celda("Pepe", 3, "Propiedad", 250, 100)
        persona6 = Persona("Oscar", 500, "si")
        juego6 = Juego()
        msg = juego6.validar_movimiento(celda6, persona6)
        self.assertEqual(msg, "Usted pago renta")

if __name__ == '__main__':
    unittest.main()
