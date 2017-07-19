import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    # ===============================================================================================================
    # Test1: Valida cuando es una propiedad, tiene dinero, decide comprar la propiedad entonces continua en el juego.
    #
    def test1(self):
        # dueño, numero, tipo, precio, renta
        celda1 = Celda("", 1, "Propiedad", 150, 50)
        # Nombre, monto, comprar
        persona1 = Persona("Toreto", 160,"si")
        # Instancia de juego
        juego1 = Juego()
        # Celda, Turno-persona
        msg = juego1.validar_movimiento(celda1,persona1)
        # Assert
        self.assertEquals(msg,"Usted ha comprado una propiedad")

    # ===============================================================================================================
    # Test2: Valida cuando es una propiedad, tiene dinero, decide NO comprar la propiedad, continua en el juego.
    #
    def test2(self):
        # dueño, numero, tipo, precio, renta
        celda2 = Celda("", 1, "Propiedad", 150, 50)
        # Nombre, monto, comprar
        persona2 = Persona("Toreto", 160,"no")
        # Instancia de juego
        juego2 = Juego()
        # Celda, Turno-persona
        msg = juego2.validar_movimiento(celda2,persona2)
        # Assert
        self.assertEquals(msg, "Sigue jugando")

    # ===============================================================================================================
    # Test3: Valida cuando es una propiedad, tiene dinero, pero NO TIENE SUFICIENTE DINERO PARA COMPRARLA
    #
    def test3(self):
        # dueño, numero, tipo, precio, renta
        celda3 = Celda("", 1, "Propiedad", 150, 50)
        # Nombre, monto, comprar
        persona3 = Persona("Toreto", 140,"no")
        # Instancia de juego
        juego3 = Juego()
        # Celda, Turno-persona
        msg = juego3.validar_movimiento(celda3,persona3)
        # Assert
        self.assertEquals(msg, "No tiene dinero suficiente")

    # ===============================================================================================================
    # Test4: Valida cuando es una propiedad que TIENE DUEÑO DISTINTO AL JUGADOR CON EL TURNO ACTIVO, tiene dinero para
    #        pagar la renta y la paga
    #
    def test4(self):
        # dueño, numero, tipo, precio, renta
        celda4 = Celda("Juan", 1, "Propiedad", 150, 50)
        # Nombre, monto, comprar
        persona4 = Persona("Toreto", 145,"si")
        # Instancia de juego
        juego4 = Juego()
        # Celda, Turno-persona
        msg = juego4.validar_movimiento(celda4,persona4)
        # Assert
        self.assertEquals(msg, "Usted pago renta")

    # =================================================================================================================
    # Test5: Valida cuando es una propiedad que TIENE DUEÑO DISTINTO AL JUGADOR CON EL TURNO ACTIVO, tiene dinero PERO
    #        NO ES SUFICIENTE PARA PAGAR LA RENTA. Acaba el juego.
    #
    def test5(self):
        # dueño, numero, tipo, precio, renta
        celda5 = Celda("Juan", 1, "Propiedad", 150, 50)
        # Nombre, monto, comprar
        persona5 = Persona("Toreto", 40,"si")
        # Instancia de juego
        juego5 = Juego()
        # Celda, Turno-persona
        msg = juego5.validar_movimiento(celda5,persona5)
        # Assert
        self.assertEquals(msg, "Perdio")

    # =================================================================================================================
    # Test6: Valida cuando la celda actual NO ES UNA PROPIEDAD.
    #       El resto de datos NO SE LLEGAN A VALIDAR, pero igual constan en la funcion y son:
    #       - La celda NO tiene dueño
    #       - La persona tiene dinero suficiente para comprarla.
    #       - Quiere realizar la compra.
    #
    def test6(self):
        # dueño, numero, tipo, precio, renta
        celda6 = Celda("", 1, "No es propiedad", 100, 40)
        # Nombre, monto, comprar
        persona6 = Persona("Toretto", 140, "si")
        # Instancia de juego
        juego6 = Juego()
        # Celda, Turno-persona
        msg = juego6.validar_movimiento(celda6,persona6)
        # Assert
        self.assertEquals(msg, "No Valido")

if __name__ == '__main__':
    unittest.main()
