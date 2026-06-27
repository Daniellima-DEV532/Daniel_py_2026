1
#valor1=float(input('Digite o primeiro valor:'))
#valor2=float(input('Digite o segundo valor:'))
#valor3=float(input('Digite o terceiro valor'))
 
#soma=valor1+valor2+valor3
#media=soma/3
#print('Soma e igual a:',soma)
#print('Meida e igual a:',media)
2
#distancia = float(input("Digite a distância: "))
#tempo = float(input("Digite o tempo: "))

#velocidade = distancia / tempo

#print("Velocidade média:", velocidade)
3
#distancia=float(input('Digite a distancia:'))
#consumo=float(input('digite o valor do consumo:'))
#litros=distancia/consumo
#print('Litros necessarios:',litros)
4
#quantidade=float(input('Digite a quantidade:'))
#preço=float(input('Digite o preço:'))
#total=quantidade=preço
#print('O valor da compra é:',total)
5
#compra=float(input('Digite o valor da compra:'))
#imposto=float(input('Digite o percentual de imposto:'))
              
#valor_imposto=compra * imposto / 100
#total_final = compra + valor_imposto

#print("Valor do imposto:", valor_imposto)
#print("Total final:", total_final)
6
#salario=float(input('Digite o valo do salario:'))
#comissão=float(input('Digite o valor da comissão:'))
#numero_vendas=float(input('Digite o numero de vendas:'))
#salario_final=salario+(comissão*numero_vendas)

#print('O salario final e de:',salario_final)
7
#valor = float(input("Digite o valor vendido: "))
#percentual = float(input("Digite a comissão (%): "))

#comissao = valor * percentual / 100

#print("Comissão:", comissao)
8
#principal=float(input('Digite o valor principal:'))
#taxa=float(input('Digite a taxa (%):'))
#tempo=float(input('Digite o tempo:'))
#juros=principal*taxa*tempo/100
#montante=principal+juros

#print("Juros:", juros)
#print("Montante:", montante)
9
#a=int(input('Digite a base:'))
#b=int(input('Digite o expoente:'))
#resultado=1 
#for i in range(b):
#    resultado = resultado * a

#print(resultado)
10
#n=int(input('Digite N:'))
#soma=0
#for i in range(1,n +1):
#    soma=soma+i
#print("Soma:", soma)
11
#n=int(input('Digite N:'))
#produto=1 
#for i in range(1, n + 1):
  #  produto=produto*i
#print('produto:',produto)
#12
#peso=float(input('Digite seu peso:'))
#altura=float(input('Digite sua altura:'))
#imc=peso/(altura**2)
#print('IMC',imc)
13
#nota1=float(input('Digite a peimeira nota:'))
#nota2=float(input('Digite a segunda nota:'))
#nota3=float(input('Digite a terceira nota:'))
#nota4=float(input('Digite a quarta nota:'))
#media=(nota1+nota2+nota3+nota4)/4
#maior=max(nota1,nota2,nota3,nota4)
#menor=min(nota1,nota2,nota3,nota4)
#print('Media:',media)
#print('Maior:',maior)
#print('Menor',menor)
14
#custo = float(input("Digite o custo de fábrica: "))
#distribuidor = custo * 0.28
#impostos = custo * 0.45
#preco_final = custo + distribuidor + impostos
#print("Preço final:", preco_final)
15
#dolares = float(input("Digite o valor em dólares: "))
#cotacao = float(input("Digite a cotação: "))
#reais = dolares * cotacao
#print("Valor em reais:", reais)
16
#v1=int(input('Digite o preimeiro valor:'))
#v2=int(input('Digite o segundo valor:'))
#v3=int(input('Digite o terceiro valor:'))
#lista=[v1,v2,v3]
#lista.sort()

#print(lista)
17
#numero = int(input("Digite um número: "))

#achou = False

#for i in range(numero + 1):
 #   if i * i == numero:
 #       achou = True

#if achou:
#    print("Quadrado perfeito")
#else:
#    print("Não é quadrado perfeito")
18
#a = float(input('digite o valo de a:'))
#b = float(input('digite o valor de b:'))
#c = float(input('digite o valor de c:'))

#if a + b > c and a + c > b and b + c > a:
#    print("Forma triângulo")
#else:
#    print("Não forma triângulo")
19
#base=float(input('Digite a base:'))
#altura=float(input('Ddigite a altura:'))
#area=(base*altura)/2
#print('A area é:',area)
20
#numero = input("Digite um número: ")

#soma = 0

#for digito in numero:
 #   soma += int(digito)

#print("Soma dos dígitos:", soma)
21
#numero = input("Digite um número: ")

 #print("Quantidade de dígitos:", len(numero))
22.
#n = int(input("Digite N: "))

#a = 1
#b = 1

#for i in range(n):
#    print(a)

    #proximo = a + b
    #a = b
    #b = proximo
23
#numero = int(input("Digite um número: "))

#divisores = 0

#for i in range(1, numero + 1):
 #   if numero % i == 0:
  #      divisores += 1

#if divisores == 2:
  #  print("É primo")
#else:
   # print("Não é primo")
24
#a = int(input("Digite o primeiro número: "))
#b = int(input("Digite o segundo número: "))

#while b != 0:
 #   resto = a % b
 #   a = b
    #b = resto

#print("MDC:", a)
25
#a = int(input('Digite um numero:'))
#b = int(input('Digite outro numero:'))

#x = a
#y = b

#while y != 0:
#    resto = x % y
#    x = y
#    y = resto

#mdc = x

#mmc = abs(a * b) // mdc

#print("MMC:", mmc)
26
#n=int(input('Digite N:'))
#fatorial=1
#for i in range(1, n +1):
 #   fatorial*=i
#print('fatorial:',fatorial)
27
#numeros = []

#for i in range(5):
   # numero = float(input("Digite um número: "))
  #  numeros.append(numero)

#soma = numeros[0] + numeros[2]

#subtracao = numeros[1] - numeros[3]

#produto = 1

#for numero in numeros:
  #  produto *= numero

#print("Soma:", soma)
#print("Subtração:", subtracao)
#print("Produto:", produto)

#if numeros[0] != 0:
  #  divisao = numeros[4] / numeros[0]
  #  print("Divisão:", divisao)
#else:
 #   print("Não é possível dividir por zero.")
28
#consumo=float(input('Digite o valor do consumo:'))
#preco=float(input('Digite o preço em kwm:'))
#conta=consumo*preco
#print('valor da conta:',conta)
29
#anos=int(input('Anos:'))
#meses=int(input('Meses:'))
#Dias=int(input('Dias:')) 

#total=anos*365+meses*30+Dias
#print('Total de dias:',total)
30
sanduiches = int(input("Quantidade de sanduíches: "))

queijo = sanduiches * 100
presunto = sanduiches * 50
carne = sanduiches * 100

print("Queijo:", queijo / 1000, "kg")
print("Presunto:", presunto / 1000, "kg")
print("Carne:", carne / 1000, "kg")