#forma de como usar un ciclo infinito
i = 1
t=int(input("ingresa el numero de tabla que se va a calcular: "))
while i<=10:
    R= t*i
    print(t,"x",i,"=", R)
    i+=1



    #forma con el ciclo for con solo la indicacion del limite 
for i in range(10):
        print("contando", i)


#ciclo for con donde solo se indica donde empieza y donde termina 
for i in range(1, 10):
        print("contando", i)


#ciclo for con indicacion de donde a donde va a ir saltando 
for i in range(1, 10,2 ):
        print("contando", i)

#formas de como utilizar el ciclo for 
palabra = input("ingresa palbra: ")
for letra in palabra:
       print(letra)

#contar cuentas vocales tiene una palabra
#palabra (a e i o u)

contar_vocales = input("ingresa palabra: ")

contador = 0

for letra in contar_vocales:
    if letra.lower() in "aeiou":
        contador += 1
   
print ("la palabra: ", contar_vocales, "tiene: ", contador, "vocales")


#upper convertir en mayusculas
#lower convertir en minusculas

#listas

lista1 = [0,1,2,3,4,5,6,7,8]



 #en python se puedde poner cualquier elemento o caracter a la lista
for elemento in lista1:
      print (elemento)
  

#formas de imprimir una lista
edad = 0
lista2 = []
while edad >= 0:        
    edad = int(input("ingresa tu edad: "))

    lista2.append(edad)

print (lista2)


