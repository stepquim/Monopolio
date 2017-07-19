import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    '''
    Test1 valida cuando es una propiedad, 
    tiene dinero, decide comprar la propiedad entonces continua en el juego.
    '''
    def test1(self):
        celda3 = Celda(dueno="", numero=1, tipo="Propiedad", precio=150, renta=50)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted ha comprado una propiedad")

	'''Test2 valida cuando no es propiedad, 
    '''
    def test2(self):
        celda3 = Celda(dueno="", numero=1, tipo="No Propiedad", precio=150, renta=50)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="si")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No Valido")

    '''
    Test1 valida cuando es una propiedad, 
    tiene dinero, decide no comprar la propiedad entonces continua en el juego.
    '''
    def test3(self):
        celda3 = Celda(dueno="", numero=1, tipo="Propiedad", precio=150, renta=50)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Sigue jugando")

    '''
    Test1 valida cuando es una propiedad, 
    no tiene dinero suficiente
    '''
    def test4(self):
        celda3 = Celda(dueno="", numero=1, tipo="Propiedad", precio=180, renta=50)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"No tiene dinero suficiente")

    '''
    Test5 valida cuando es una propiedad, 
    el dueno es el mismo del turno
    '''
    def test5(self):
        celda3 = Celda(dueno="Toreto", numero=1, tipo="Propiedad", precio=180, renta=50)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Esta propiedad es suya, continua jugando")


    '''
    Test6 valida cuando es una propiedad, 
    el dueno no es el mismo del turno, monto mayor que la renta
    '''
    def test6(self):
        celda3 = Celda(dueno="Monica", numero=1, tipo="Propiedad", precio=180, renta=50)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Usted pago renta")


    '''
    Test7 valida cuando es una propiedad, 
    el dueno no es el mismo del turno, monto menor que la renta
    '''
    def test7(self):
        celda3 = Celda(dueno="Monica", numero=1, tipo="Propiedad", precio=180, renta=190)
        persona3 = Persona(nombre="Toreto", monto=160, comprar="no")
        juego3 = Juego()
        msg = juego3.validar_movimiento(celda3,persona3)
        self.assertEquals(msg,"Perdio")

if __name__ == '__main__':
    unittest.main()
