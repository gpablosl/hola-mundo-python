print("me lmao jeff")
#este es un comentario
numero = 4
print(numero)
print("mi numero: " + str(numero))
print()
numero = "Cuatro"
print("mi numero: " + numero)


a = 356
b = 80

#if
if a > b:
    print("A es mayor que b")
    print("sigo estando en el bloque del if")
else:
    print("A no es mayor que B")

print("afuera del if")

#for / ciclo
frutas = ["Manzana", "Sandía", "Melón", "Mango"]
for fruta in frutas:
    print("Fruta: " + fruta)
#funciones
def mi_funcion():
    print("Estoy en una funcion")
#funciones con parametros
def saludar(nombre, apellidos):
    print("Hola " + nombre + " " + apellidos)

mi_funcion()
saludar("German","Pablos")