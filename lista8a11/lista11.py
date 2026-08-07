1
#array = []

#print(len(array))
2
#numeros = [10, 20, 30, 40, 50]

#print("Primeiro:", numeros[0])
#print("Último:", numeros[-1])
3
#numeros = [10,20,30]

#numeros.append(40)

#print(numeros)
4
#numeros = [10,20,30,40]

#numeros.pop()

#print(numeros)
5
#numeros = [20, 30, 40]

#numeros.insert(5,10)

#print(numeros)
6
#numeros = [10,20,30,40]

#numeros.pop(0)

#print(numeros)
7
#numeros = []

#for i in range(10):

 #   numero = int(input('Digite um numero:'))

 #   numeros.append(numero)

#print(numeros)
8
#numeros = [10,20,30,40]

#soma = 0

#for numero in numeros:

 #   soma += numero

#print(soma)
9
#numeros =[10,20,30,40]

#soma = 0 

#for numero in numeros:

 #   soma += numero

#media = soma / len(numeros)

#print(media)
10
#numeros = [10, 20, 30, 40,50,60]

#maior = numeros[0]

#for numero in numeros:

 #   if numero > maior:
  #      maior = numero

#print(maior)
11
#numeros = [6, 12, 34 , 65, 2,64, 9]

#menor = numeros[0]

#for numero in numeros:

# if numero < menor:
   # menor = numero

#print(menor)
12
#numeros = [2,4 ,5,8,12,56,78,90]

#contador = 0

#for numero in numeros:

  #  if numero % 2 == 0:

 #       contador += 1

#print(contador)
13
#numeros = [2,4 ,5,8,12,56,78,90]

#contador = 0

#for numero in numeros:

 #   if numero % 2 != 0:

 #    contador += 1

#print(contador)
14
#numeros = [-7, 9, 4, -19, -12, 15 ]

#positivos = []

#for numero in numeros:

  #  if numero > 0: 
 #       positivos.append(numero)

#print(positivos)
15
#numeros = [-7, 9, 4, -19, -12, 15 ]

#negativos = []

#for numero in numeros:
 #   if numero < 0:

#        negativos.append(numero)

#print(negativos)
16
#numeros = [-7, 9, 4, -19, -12, 15 ]

#x = int(input('Digite um numero:'))

#encontrou = False

#for numero in numeros:

 #   if numero == x:
  #      encontrou = True

#print(encontrou)
17
#numeros = [-7, 9, 4, -19, -12, 15 ]

#x = int(input("Digite um número: "))

#indice = -1

#for i in range(len(numeros)):

 #   if numeros[i] == x:

  #      indice = i
   #     break

#print(indice)
18
#numeros = [-7, 9, 4, -19, -12, 15 ]

#copia = numeros.copy()

#print(copia)
19
#numeros = [-7, 9, 4, -19, -12, 15 ]

#invertido = []

#for i in range(len(numeros) - 1, -1, -1):

#    invertido.append(numeros[i])

#print(invertido)
20
#numeros = [6, 12, 34 , 65, 2,64, 9]

#numeros.sort

#print(numeros)
21
#numeros = [1, 2, 3, 2, 4, 1, 5]

#unico = []

#for numero in numeros:

  #  if numero not in unico:

 #       unico.append(numero)

#print(unico)
22
#numeros = [2, 3, 3 , 4, 2, 5, 5, 3, 3]

#frequencia = {}

#for numero in numeros:

 #   if numero in frequencia:

  #      frequencia[numero] += 1

   # else:

    #    frequencia[numero] = 1

#for numero, quantidade in frequencia.items():

 #   print(numero, "->", quantidade)
23
#numeros = [2, 3, 3 , 4, 2, 5, 5, 3, 3]

#frequencia = {}

#or numero in numeros:

   # if numero in frequencia:
    #    frequencia[numero] += 1
  #  else:
 #       frequencia[numero] = 1

#moda = None
#maior = 0

#for numero in frequencia:

  #  if frequencia[numero] > maior:

 #       maior = frequencia[numero]
#        moda = numero

#print("Moda:", moda)
24
#numeros = [2, 3, 3 , 4, 2, 5, 5, 3, 3]

#numeros.sort()

#meio = len(numeros) // 2

#if len(numeros) % 2 == 0:

 #   mediana = (numeros[meio - 1] + numeros[meio]) / 2

#else:

 #   mediana = numeros[meio]

#print(mediana)
25
#umeros = [6, 12, 34 , 65, 2,64, 9]

#maior = max(numeros)

#segundo = numeros[0]

#for numero in numeros:

 #   if numero != maior and numero > segundo:

  #      segundo = numero

#print(segundo)
26
#numeros = [10, 80, 40, 20, 70]

#menor = min(numeros)

#segundo = numeros[0]

#for numero in numeros:

  #  if numero != menor and numero < segundo:

 #       segundo = numero

#print(segundo)
27
#numeros = [1,2,3,4,5,6,7,8,9]

#k = int(input("Digite K: "))

#for i in range(0, len(numeros), k):

#    print(numeros[i:i+k])
28
a = [1,2,3]

b = [4,5,6]

c = []

for i in range(len(a)):

    c.append(a[i] + b[i])

print(c)
29
a = [1,2,3]

b = [3,4,5]

resultado = []

for numero in a + b:

    if numero not in resultado:

        resultado.append(numero)

print(resultado)
30
numeros = [10,20,30,40,50]

ordenado = True

for i in range(len(numeros)-1):

    if numeros[i] > numeros[i+1]:

        ordenado = False
        break

print(ordenado)


