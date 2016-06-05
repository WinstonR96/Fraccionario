#Declaro la clase y sus Atributos
class Fraccionario:
    numerador=0
    denominador=0


   #Constructor
    def __init__(self, num, den):
        self.numerador = num
        self.denominador = den

    #Metodo ToString
    def __str__(self):
        cadena = self.numerador," / ",self.denominador
        return cadena


    #MetodoS GET

    def getNumerador(self):
        return self.numerador

    def getDenominador(self):
        return self.denominador
    #Metodos SET
    def setNumerador(self, num):
        self.numerador=num

    def setDenominador(self, den):
        self.denominador=den

    #Metodo Para Imprimir
    def imprimir(self):
        return "Numerador: ",self.numerador," Denominador: ",self.denominador

    #Metodos propios de fracciones

    def esHomogenea(self, f):
        if(self.denominador == f.denominador):
            return True
        else:
            return False

    def invertir(self):
        print (self.denominador," / ", self.numerador)

    def esPositiva(self):
        if ((self.numerador>0 and self.denominador>0) or (self.numerador<0 and self.denominador<0)):
            return "Es positiva"
        else:
            return "Es negativa"

    def valorFraccion(self):
        return self.numerador/self.denominador

    def suma(self, f):
        if(self.esHomogenea(f)):
            return Fraccionario(self.numerador+f.numerador, self.denominador)
        else:
            return Fraccionario(self.numerador*f.denominador + self.denominador*f.numerador, self.denominador*f.denominador)

    def resta(self, f):
        if (self.esHomogenea(f)):
            return Fraccionario(self.numerador - f.numerador, self.denominador)
        else:
            return Fraccionario(self.numerador * f.denominador - self.denominador * f.numerador,
                                self.denominador * f.denominador)


    def multiplicacion(self, f):
        return Fraccionario(self.numerador*f.numerador, self.denominador*f.denominador)

    def division(self, f):
        return Fraccionario(self.numerador*f.denominador, self.denominador*f.numerador)