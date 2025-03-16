#Prueba condicionales 
print("Introduzca su nombre:")# Le pedimos el nombre al usuario
nombre = input() # Guardamos el nombre en una variable

# Condicional para comprobar que los datos del usuario son correctos
if nombre == "Rubén":
    print("Bienvenido Rubén") # Mensaje de bienvenida
    print("Ahora introduzca su edad:") # Pregunta al ususario por su edad
    edad = input() # Guardamos la edad en una variable
    edad = int(edad) # Convertimos la edad de str a int
    
    # Condicional para comprobar que la edad del usuario se encuentre dentro del rango
    if edad  <  18 or edad > 65:
        print("Lo siento no pueden acceder menores de edad o mayores de 65") #
    else:
        print("Identificación aceptada")
else:
    print("Nombre incorrecto intentelo de nuevo")
