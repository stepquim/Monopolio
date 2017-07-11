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
      if (celda.tipo!="Propiedad"):
         # se ejecuta otro codigo
         print("la celda no es una Propiedad")
    	 return "No Valido"
      else:
        if celda.dueno is "":
          if turnoPersona.monto < celda.precio:
              print("salio del juego")
              return "No tiene dinero suficiente"
          else:
    		if turnoPersona.comprar=="si":
    			#puede comprar
    			print("paga para ser el dueno")
    			turnoPersona.monto = turnoPersona.monto - celda.precio
    			return "Usted ha comprado una propiedad"
    		else:
    			return "Sigue jugando"
        else:
          if celda.dueno == turnoPersona.nombre:
              print("es el mismo dueno")
              return "Esta proiedad es suya, continua jugando"
          else:
            if turnoPersona.monto < celda.renta:
                print("pierde el juego no tiene dinero para pagar")
                return "Perdio"
            else:
                print("paga la renta")
                turnoPersona.monto = turnoPersona.monto - celda.renta
                return "Usted pago renta"
