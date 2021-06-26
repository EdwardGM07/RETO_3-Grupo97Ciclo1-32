"""
Edward Camilo Gonzalez Monje, 
edwardcamilo2020@gmail.com 
Grupo 97 - ciclo 1,
"""
#================ FUNCION ===========================


def clave_segura(clave)->str:
#Metodo para verificar si la clave es segura
    mensaje = None
    cantidad = len(clave)
    minuscula = False
    mayuscula = False
    numero = False
    noEspacio = False
    numeral = False
    alfanumerico = False
    #Creacion de variables

    if cantidad > 5 and cantidad < 13:
      #Ingresa si la longitud de la clave esta entre 6 a 12 caracteres
        for i in clave:
            #Recorre la palabra clave 
            if i.islower():
              #Comprueba si ese caracter es minuscula
                minuscula = True

            if i.isupper():
              #Comprueba si ese caracter es mayuscula
                mayuscula = True

            if i.isnumeric():
              #Comprueba si ese caracter es numerico
                numero = True

            if not i.isalnum():
              #Comprueba si ese caracter no es alfanumerico
                alfanumerico = True

            if not i.isspace():
              #Comprueba si ese caracter no es un espacio
                noEspacio = True

            if i == "#":
              #Comprueba si ese caracter es un numeral
                numeral = True

        if minuscula == True and mayuscula == True and numero == True and alfanumerico == True and noEspacio == True and numeral == True:
          #Ingresa si todos los datos son verdaderos
            mensaje = "CORRECTO"
            #Asigna a la variable que la clave es correcta
        else:          
            mensaje = "INCORRECTO"
            #Asigna a la variable que la clave es incorrecta porque almenos uno es falso
    else:
        mensaje = "INCORRECTO"
        #Asigna a la variable que la clave es incorrecta porque no cumple con la longitud

    return str(mensaje)


#==================== PRUEBA ========================

clave = "Orlando.#529"  # clave valida
result = clave_segura(clave)  # llamada de funcion
print(result)  # mostrar valor
