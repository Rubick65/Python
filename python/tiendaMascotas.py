# Mensaje de incio de la tienda de mascotas
print("****************************")
print("**       BIENVENIDO A     **")
print("**  LA TIENDA DE MASCOTAS **")
print("****************************")

# Declaración de variables
numPerros = 10 # Cantidad de perros en la tienda
numGatos = 15 # Cantidad de gatos en la tienda
numPajaros = 7 # Cantidad de pajaros en la tienda
suma = numPajaros +  numGatos + numPajaros # Suma de la cantidad de animales en la tienda


print("Introducza su nombre:") # Pedimos el nombre al usuario
nombre = input() # Guardamos el nombre en una variable

print("Ahora su apellido:") # Pedimos el apellido al usuario
apellido = input()# Guardamos el apellido en una variable


nombreCompleto = nombre + " " + apellido # Concatenamos dos variables de tipo String

print("Bienvenido",nombreCompleto)

# Mostramos la cantidad de animales en la tinenda y la suma de todos
print("Actualmente contamos con:")
print("Perros:",numPerros,"Gatos:",numGatos,"Pajaros:",numPajaros)
print("En total tenemos",suma,"animales.")