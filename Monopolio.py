class Persona:
  nombre = ""
  monto = 0
  comprar = ""
  def __init__(self, nombre, monto,comprar):
        self.nombre = nombre
        self.monto = monto
        self.comprar = comprar

class Persona:
  nombre = ""
  monto = 0
  comprar = ""
  def __init__(self, nombre, monto,comprar):
        self.nombre = nombre
        self.monto = monto
        self.comprar = comprar

class Celda:
  dueno = ""
  numero= 0
  tipo = ""
  precio = 0
  renta =  0
  def __init__(self, dueno, numero,tipo,precio,renta):
        self.dueno =  dueno
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.renta = renta


class Juego:
    def validar_movimiento(self,celda,turnoPersona):
      if (celda.tipo!="Propiedad"):#1
         # se ejecuta otro codigo
         print("la celda no es una Propiedad")#2
       return "No Valido"
      else:
        if celda.dueno is "":#3
          if turnoPersona.monto < celda.precio:#4
              print("salio del juego")#5
              return "No tiene dinero suficiente"
          else:
        if turnoPersona.comprar=="si":#6
          #puede comprar
          print("paga para ser el dueno")#7
          turnoPersona.monto = turnoPersona.monto - celda.precio
          return "Usted ha comprado una propiedad"
        else:
          return "Sigue jugando"
        else:
          if celda.dueno == turnoPersona.nombre:#8
              print("es el mismo dueno")#9
              return "Esta proiedad es suya, continua jugando"
          else:
            if turnoPersona.monto < celda.renta:#10
                print("pierde el juego no tiene dinero para pagar")#11
                return "Perdio"
            else:
                print("paga la renta")#12
                turnoPersona.monto = turnoPersona.monto - celda.renta
                return "Usted pago renta"

    