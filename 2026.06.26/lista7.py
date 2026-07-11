1
#for i in range(11):
   # print(i)
2
#for i in range(10, -1, -1):
  #  print(i)
3
#for i in range(2, 21, 2):
   # print(i)
4 
#for i in range(1, 21, 2):
  #  print(i)
5
#soma = 0

#for i in range(1, 101):
   # soma += i

#print(soma)
6
#produto = 1

#for i in range(1, 11):
 #   produto *= i

#print(produto)
7
#n = int(input("Digite um número: "))

#for i in range(1, n + 1):
    #print(i)
8
#n = int(input("Digite um número: "))

#for i in range(n, 0, -1):
 #   print(i)
9
#n = int(input("Digite um número: "))

#for i in range(3, n + 1, 3):
#    print(i)    
10
#for i in range(1, 11):
  #  print(f"5 x {i} = {5 * i}")
11
#numero = int(input("Digite um número: "))

#for i in range(1, 11):
 #   print(f"{numero} x {i} = {numero * i}")
12
#n = int(input("Digite um número: "))

#fatorial = 1

#for i in range(1, n + 1):
 #   fatorial *= i

#print("Fatorial:", fatorial)
13
#a = 1
#b = 1

#for i in range(20):
 #   print(a)

 #   proximo = a + b
 #   a = b
 #   b = proximo
14
#n = int(input("Quantos termos deseja mostrar? "))

#a = 1
#b = 1

#for i in range(n):
 #   print(a)
#
  #  proximo = a + b
   # a = b
    #b = proximo
15
#for numero in range(2, 51):

 #   divisores = 0

  #  for i in range(1, numero + 1):

   #     if numero % i == 0:
    #        divisores += 1

   # if divisores == 2:
   #     print(numero)
16
#n=int(input("Digite um número: "))

#contador = 0

#for i in range(1, n + 1):

  #  if i % 2 == 0:
 #       contador += 1

#print("Quantidade de pares:", contador)
17
#n=int(input("Digite um número: "))

#contador = 0

#for i in range(1, n + 1):
 #   if i % 2 != 0:
 #       contador += 1

#print("Quantidade de ímpares:", contador)
18
#n=int(input("Digite um número: "))

#soma = 0

#for i in range(1, n + 1):
  #  if i % 2 == 0:
 #       soma += i

#print("Soma dos pares:", soma)
19
#n = int(input("Digite um número: "))

#soma = 0

#for i in range(1, n + 1):

 #   if i % 2 != 0:
 #       soma += i

#print("Soma:", soma)
20
#for i in range(1, 101):

   # if i % 3 == 0 and i % 5 == 0:
  #      print("FizzBuzz")

 #   elif i % 3 == 0:
#        print("Fizz")

    #elif i % 5 == 0:
    #    print("Buzz")

   # else:
   #     print(i)
21
#n=int(input("Digite um número: "))

#for i in range(1, n + 1):
 #   if n % i == 0:
#        print(i)
22
#n = int(input("Digite um número: "))

#divisores = 0

#for i in range(1, n + 1):

  #  if n % i == 0:
 #       divisores += 1

#if divisores == 2:
 #   print("É primo")

#else:
 #   print("Não é primo")
23
#maior = int(input("Digite um número: "))

#for i in range(9):

    #numero = int(input("Digite um número: "))

    #if numero > maior:
    #    maior = numero

#print("Maior número:", maior)
24
#menor = int(input("Digite um número: "))

#for i in range(9):

   # numero = int(input("Digite um número: "))

   # if numero < menor:
   #     menor = numero

#print("Menor número:", menor)
25
#soma = 0

#for i in range(10):

    #numero = int(input("Digite um número: "))
    #soma += numero

#media = soma / 10

#print("Média:", media)
26
#contador = 0

#for i in range(10):

 #   numero = int(input("Digite um número: "))

  #  if numero > 8:
   #     contador += 1

#print("Quantidade:", contador)
27
contador = 0

for i in range(10):

    numero = int(input("Digite um número: "))

    if 0 <= numero <= 100:
        contador += 1

print("Quantidade:", contador)
28
for i in range(100, 201):

    if i % 2 != 0:
        print(i)
29
a = int(input("Digite A: "))
b = int(input("Digite B: "))

if a <= b:

    for i in range(a, b + 1):
        print(i)

else:

    for i in range(a, b - 1, -1):
        print(i)
30
for i in range(1, 11):
    print("*" * i)