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

    #PRUEBA LA RAMA CUANDO NO ES UNA PROPIEDAD RETORNA NO VALIDO E IMPRIME EL MENSAJE LA CELDA NO ES UNA PROPIEDAD
    def testZ1(self):
        celdaz1 = Celda("", 1, "", 150, 50)
        personaz1 = Persona("Toreto", 160, "si")
        juegoz1 = Juego()
        msg = juegoz1.validar_movimiento(celdaz1,personaz1)
        self.assertAlmostEqual(msg,"No Valido")

    # PRUEBA LA RAMA CUANDO EL PERSONA NO TIENE MONTO SUFIECIENTE PRECIO=500 Y MONTO=100 ,
    #  IMPRIME EL  MENSAJE SALIO DEL JUEGO
    def testZ2(self):
        celdaz2 = Celda("", 1, "Propiedad", 500, 50)
        personaz2 = Persona("Toreto", 100, "si")
        juegoz2 = Juego()
        msg = juegoz2.validar_movimiento(celdaz2, personaz2)
        self.assertAlmostEqual(msg, "No tiene dinero suficiente")

    # PRUEBA LA RAMA CUANDO EL PERSONA  TIENE MONTO SUFIECIENTE PRECIO=100 Y MONTO=500  PERO NO TIENE EL TURNO PARA COMNPRAR
    #  NO IMPRIME NINGUN MENSAJE SOLO DEFVUELVE "Sigue jugando"
    def testZ3(self):
        celdaz3 = Celda("", 1, "Propiedad", 100, 50)
        personaz3 = Persona("Toreto", 500, "no")
        juegoz3 = Juego()
        msg = juegoz3.validar_movimiento(celdaz3, personaz3)
        self.assertAlmostEqual(msg, "Sigue jugando")

    # PRUEBA LA RAMA CUANDO LA CELDA TIENE DUEÑO Y CONINCIDE CON LA PERSONA
    #   IMPRIME MENSAJE "es el mismo dueno"
    def testZ4(self):
        celdaz4 = Celda("Toreto", 1, "Propiedad", 100, 50)
        personaz4 = Persona("Toreto", 500, "no")
        juegoz4 = Juego()
        msg = juegoz4.validar_movimiento(celdaz4, personaz4)
        self.assertAlmostEqual(msg, "Esta proiedad es suya, continua jugando")

    # PRUEBA LA RAMA CUANDO LA CELDA TIENE DUEÑO Y ES DISTINTO A LA PERSONA PERO NO TIENE SUFIECIENTE PARA LA RENTA
    #   IMPRIME MENSAJE "pierde el juego no tiene dinero para pagar"
    def testZ5(self):
        celdaz5 = Celda("Israel", 1, "Propiedad", 100, 500)
        personaz5 = Persona("Toreto", 100, "no")
        juegoz5 = Juego()
        msg = juegoz5.validar_movimiento(celdaz5, personaz5)
        self.assertAlmostEqual(msg, "Perdio")

    # PRUEBA LA RAMA CUANDO LA CELDA TIENE DUEÑO Y ES DISTINTO A LA PERSONA PERO SI TIENE SUFIECIENTE PARA LA RENTA
    #   IMPRIME MENSAJE "paga la renta"
    def testZ6(self):
        celdaz6 = Celda("Israel", 1, "Propiedad", 100, 500)
        personaz6 = Persona("Toreto", 1000, "no")
        juegoz6 = Juego()
        msg = juegoz6.validar_movimiento(celdaz6, personaz6)
        self.assertAlmostEqual(msg, "Usted pago renta")


if __name__ == '__main__':
    unittest.main()
