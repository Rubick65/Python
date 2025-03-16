# Mensaje de bienvenida a la tienda de manzanas
print("=================================")
print("          BIENVENIDO A           ")
print("      LA TIENDA DE MANZANAS      ")
print("=================================")


print("Por favor indíquenos su nombre:") # Le pedimos su nombre al usuario
nombre = input() #Guardamos el nombre en una variable 

print("Ahora indíquenos su apellido:")# Le pedimos al usuario su apellid
apellido = input() # Guardamos el apellido en una variable

nombreCompleto = nombre + " " + apellido # Concatenamos el nombre y el apellido para formar el nombre completo
manzanas = 20 # Declaramos una variable que indica la cantidad de manzanas en la tienda
precio = 5 # Precio de cada manzana en euros

print("Bienvendio",nombreCompleto,"actualmente tenemos",manzanas,"manzanas disponibles, por un precio de",precio,"euros cada una.") # Imprimimos el nombre del usuario la cantidad de manzanas disponibles y el preco de cada una

print("¿Cuantas manzanas quieres comprar?") # Le preguntamos al usuario cuantas manzanas quiere  comprar
cantidad = input() # Guardamos la cantidad de manzanas que quiera el usuario en una variable

cantidad = int(cantidad) # Convertimos el input del usuario de string a int
manzanas -= cantidad # Actualizamos la cantidad de manzanas disponibles en la tienda
precioFinal = cantidad * precio # Calculamos el precio final de las manzanas que quiere comprar el usuario 

print("Manzanas que quieres comprar:",cantidad,"Con un precio total de:",precioFinal,"euros.")# Imprimimos la cantidad de manzanas que el usuario quiere comprar y el precio de las mismas

print("Después de la venta nos quedan",manzanas,"manzanas.") # Imprimimos la cantidad de manzanas restantes después de la compra