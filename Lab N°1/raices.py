
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 28-Abril-2013
#Actividad : 6 - Raices Lab N°1
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Calcula los resultados de una ecuacion cuadratica
def raices(a,b,c):

    res1= (-b-(b^2+4*a*c)**(1/2))/(2*a) #Resultado 1
    res2= (-b+(b^2+4*a*c)**(1/2))/(2*a) #Resultado 2

    #Primer valor
    print("Primer resultado de la ecuacion cuadratica es",res1,"del tipo",type(res1))

    #Segundo valor
    print("Segundo resultado de la ecuacion cuadratica es",res2,"del tipo",type(res2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():

    #Valor del coeficiente de x^2
    a=input("Ingrese el termino 'a' de la ecuacion cuadratica ")

    #Comprueba que a no sea 0
    if a==0:
        print("ERROR, 'a' no puede ser 0")
        return 0
    #Valor del coeficiente de x
    b=input("Ingrese el termino 'b' de la ecuacion cuadratica ")

    #Valor del coeficiente que no lleva x
    c=input("Ingrese el termino 'c' de la ecuacion cuadratica ")
    
    #Calcula los valores de la funcion cuadratica
    raices(int(a),int(b),int(c))

    return 0


#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
