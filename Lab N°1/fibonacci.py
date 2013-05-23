
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 28-Abril-2013
#Actividad : 3 - Fibonacci Lab N°1
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def fibo(n):
    if(n==0):
        return 0
    else:
        if (n==1):
            return 1
        else:
            return (fibo (n-1) + fibo (n-2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():
    

    num=input("Ingrese el numero del termino de la serie fibonacci que desea mostrar : ")

    a=fibo(int(num))

    print("El termino ",num," de la serie fibonacci es ",a)


    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

