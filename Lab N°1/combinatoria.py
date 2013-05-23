
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 28-Abril-2013
#Actividad : 5 - Combinatoria Lab N°1
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Funcion que retorna el resultado del coeficiente binominal
def combinatoria(n,k):
    nfac=1
    kfac=1
    facnk=n-k
    auxfacnk=1

    #Factorial de n
    while(n):
        nfac=nfac*n 
        n=n-1
        
    #Factorial de k
    while(k):
        kfac=kfac*k
        k=k-1
    #Calcula el factorial de n-k
    while(facnk):
        auxfacnk=auxfacnk*facnk
        facnk=facnk-1

    #Retorna el resultado de n!/((n-k)!*k)
    return nfac/(auxfacnk*kfac)

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#


def main():

    #Ingreso de los valores de n y k
    n=input("Ingrese el termino 'n' del numero combinatorio : ")
    k=input("Ingrese el termino 'k' del numero combinatorio : ")

    #Comprueba que k sea mayor que 0
    if int(k)<0:
        print("el termino 'k' tiene que ser mayor a 0")
    
    else:
        #Comprueba que k sea menor que n
        if int(k)>int(n):
            print("el termino 'k' debe ser menor o igual al termino 'n'")

        #Imprime el resultado de la operacion solo si las condiciones de arriba de cumplen
        else:
            print("El numero combinatorio es : ",combinatoria(int(n),int(k)))



    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
