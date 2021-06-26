# Identificar
a)	¿Cuál es el problema?
Se robaron los correos de los usuarios de misiontic y los hackers estan probando contraseñas simples.
b)	¿Quiénes son los interesados?
Usuarios de misión tic.
c)	¿Cuál es el objetivo?
Verificar si la contraseña del usuario es segura. 
d)	¿Existen restricciones?
Debe tener una longitud de 6 a 12.
Debe tener 1 Mayuscula.
Debe tener 1 Minuscula.
Debe tener 1 Número.
Debe tener 1 caracter NO alfanumerico.
Debe tener 1 '#'.
No debe tener espacios.
# Definir
a)	¿Qué conozco?
la clave del usuario.

b)	¿Qué debo conocer?
Si cumple con los requisitos para ser una clave segura.
c)	¿Dividir el problema en subproblemas?
1. Leer la clave del usuario.
2. Verificar si cumple con los requisitos.
3. Imprimir si es correcta o incorrecta.
# Estrategia
a)	Ejemplos particulares 
--Requisito 1--
1. Clave: B@nano#1 Retorna: CORRECTO
2. Clave: B@nano# 1 Retorna: INCORRECTO
3. Clave: B@nano#123. Retorna: CORRECTO
# Algoritmo
a)	Escribir algoritmo para cada requisito
--Requisito 1--
Entrada: clave.
Proceso: Evaluar con condicionales segun los requisitos para la clave.
Salida: mensaje.

# Logro --> Programa