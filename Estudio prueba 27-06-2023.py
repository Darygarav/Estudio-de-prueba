#ejercicio 1
#Ingrese un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10.Ejemplo, si ingresa el número 3, la lista debe contener: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30:
import random
""""
a =int(input("ingrese un numero: "))
lista = [a,a*2,a*3,a*4,a*5,a*6,a*8,a*9,a*10]
print(f"el numero en una lista es {lista}")
"""
#Ejercicio 2:Ingrese números enteros a una lista. Al ingresar un cero se detiene, además debe mostrarlos elementos de ésta en forma ordenada ascendente:
""""
a= True
lista= []
while a!=0:
    a=int(input("ingrese un numero, este se va a agregar a una lista: "))
    lista.append(a)
    print("se a agregadoe el numero a la lista: ", lista)
"""
#Ejercicio 3:Ingresar 10 números a una lista, luego muestre la suma y promedio de los elementos.
"""""
mi_lista = []
s=0

for n in range(10):
    x=int(input("ingrese un numero porfavor: "))
    mi_lista.append(x)
    s= s + x
    p = s/10
    print("la lista de los numeros ingresados", mi_lista, f"la suma de todos los numeros son {s} y el promedio es {p}" )

"""
#Ejercicio 4:Crear una lista con 20 números enteros aleatorios entre 1 y 100. Luego muestre la lista.
"""""
lista = []
x= True
while x:
    for n in  range (20):
        a=int(input("ingrese un numero a la lista enteros aleatorios entre 1 y 100= "))
        if a >= 1 and a<= 100:
            lista.append(a)
            print("la lista de los numero ingresadors son", lista)
        
        else:
            
            print("el valor no es valido")
            break
    break

import random
lista = []
for i in range(20):
    lista.append(random.randint(1, 100))
lista.sort()
print(lista)
    
"""



#Ejercicio 5:Considere la lista del ejercicio 1 y genere una segunda lista con los elementos ordenadosen forma ascendente y una tercera lista con los elementos ordenados descendentemente.Mostrar los tres resultados
""""
a =int(input("ingrese un numero: "))
lista_n= [a,a*2,a*3,a*4,a*5,a*6,a*8,a*9,a*10]
lista_a=[a,a*2,a*3,a*4,a*5,a*6,a*8,a*9,a*10]
lista_d= [a,a*2,a*3,a*4,a*5,a*6,a*8,a*9,a*10]
lista_a.sort()
lista_d.sort(reverse=True)
print("el numero en una lista en orden normal",lista_n)
print("el numero en una lista en orden desendente",lista_d)
print("el numero en una lista en orden ascendente",lista_a)

lista = []

for i in range(1,10):
    lista.append(5*i)
print(lista)
"""
#Ejercicio 6:Crear una lista con números enteros positivos aleatorios entre 1 y 100, luego muestre elnúmero menor y el mayor
""""
lista= []
lista.append (random.randint(1,100))


for i in range(10):
    print(random.randint(1, 1000))
"""
lista_a = ["BBBBBB", "PPPPPPPPPPP", "DDDDD"]
lista_b= [12,1,203]
#lista.reverse()

lista_a.sort(reverse=True)
lista_b.sort(reverse=True)
print(lista_a,lista_b)