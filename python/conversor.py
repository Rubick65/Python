# Mensaje de bienvenida
print("Bienvenido al conversor de Celsius en Fahrenheit")

# Mensaje que indica al usuario que introduzca una temperatura en celsius
print("Introduzca la temperatura en celsius que será transformada en Fahrenheit:")
celsius = input(); # En python el input siempre es string

print("Temperatura:",celsius) # Imprimimos la temperatura en celsius introducida por el usuario

print(type(celsius)) # Mostramos el tipo de dato de celsius antes de convertilo a decimal

celsius = float(celsius) # Convertimos la temperatura en celsius de string a decimal

print(type(celsius)) # Mostramos el tipo de dato de celsius depués de convertirlo a decimal

# Fahrenheit = (celsius 9/5) + 32
fahrenheit = (celsius * 9/5) + 32 # Realizamos la conversión de celsius en fahrenheti

print("Farenheit:",fahrenheit) # Imprimimos la temperatura en fahrenheit

