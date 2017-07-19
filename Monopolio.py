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
      if (celda.tipo!="Propiedad"):  #1
         # se ejecuta otro codigo
         print("la celda no es una Propiedad") #2
    	 return "No Valido"  #3
      else:
        if celda.dueno is "":  #4
          if turnoPersona.monto < celda.precio:  #5
              print("salio del juego") #6
              return "No tiene dinero suficiente"  #7
          else:
    		if turnoPersona.comprar=="si":  #8
    			#puede comprar
    			print("paga para ser el dueno") #9
    			turnoPersona.monto = turnoPersona.monto - celda.precio  #10
    			return "Usted ha comprado una propiedad" #11
    		else:
    			return "Sigue jugando" #12
        else:
          if celda.dueno == turnoPersona.nombre: #13
              print("es el mismo dueno") #14
              return "Esta proiedad es suya, continua jugando" #15
          else:
            if turnoPersona.monto < celda.renta: #16
                print("pierde el juego no tiene dinero para pagar") #17
                return "Perdio" #18
            else:
                print("paga la renta") #19
                turnoPersona.monto = turnoPersona.monto - celda.renta #20
                return "Usted pago renta" #21
