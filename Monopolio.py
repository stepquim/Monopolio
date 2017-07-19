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
    #numeracion del procesoa recorrer
    def validar_movimiento(self,celda,turnoPersona): #1
      if (celda.tipo!="Propiedad"): #2
         # se ejecuta otro codigo
         print("la celda no es una Propiedad")
    	 return "No Valido" #3
      else:
        if celda.dueno is "": #4
          if turnoPersona.monto < celda.precio: #5
              print("salio del juego")
              return "No tiene dinero suficiente" #6
          else:
    		if turnoPersona.comprar=="si": #7
    			#puede comprar
    			print("paga para ser el dueno")
    			turnoPersona.monto = turnoPersona.monto - celda.precio
    			return "Usted ha comprado una propiedad" #8
    		else:
    			return "Sigue jugando" #9
        else:
          if celda.dueno == turnoPersona.nombre: #10
              print("es el mismo dueno")
              return "Esta proiedad es suya, continua jugando" #11
          else:
            if turnoPersona.monto < celda.renta: #12
                print("pierde el juego no tiene dinero para pagar")
                return "Perdio" #13
            else:
                print("paga la renta")
                turnoPersona.monto = turnoPersona.monto - celda.renta
                return "Usted pago renta" #14
