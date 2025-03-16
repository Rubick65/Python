# Variables que guardan mi nombre(No hace falta decalrar el tipo de variable cómo en java)
nombre = "Rubén"
apellido = "Martín"
edad = 20

# Actualizamos la variable de nombre cambiando su valor original
nombre = "Luis"
print(nombre,apellido,"Edad:",edad ) # Imprimimos por pantalla el nombre y el apellido

edad = 25 # Actualizamos la variable edad 

print(nombre,apellido,"Edad:",edad )  # Volvemos a imprimir la información con la edad actualizada

edad = 25 + 2 # Cambiamos el valor de la edad sumandole dos

print(nombre,apellido,"Edad:",edad ) # Imprimimos la información actualizada

edad = 20 + edad # Cambiamos el valor de la edad sumandole 20 a su propio valor

print(nombre,apellido,"Edad:",edad ) # Imprimimos la información actualizada

edad = 20 / edad # Cambiamos el valor de la edad dividiendo 20 a su propio valor

print(nombre,apellido,"Edad:",edad ) # Imprimimos la información actualizada

edad = 20 - edad # Cambiamos el valor de la edad restandole 20 a su propio valor

print(nombre,apellido,"Edad:",edad ) # Imprimimos la información actualizada

edad = 20 * edad # Cambiamos el valor de la edad multiplicando 20 a su propio valor

print(nombre,apellido,"Edad:",edad ) # Imprimimos la información actualizada

print(type(edad)) # Imprimimo el tipo de variable de edad(float)