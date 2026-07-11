1
#numero = float(input("Digite um número: "))

#if numero > 0:
  #  print("Positivo")
#elif numero < 0:
  #  print("Negativo")
#else:
 #   print("Zero")
2
#numero=int(input('Digite um numero:'))

#if numero % 2 == 0:
 #   print('Par')
#else:
  #  print('Impar')
3
#num1=float(input('Digite o primeiro numero:'))
#num2=float(input('Digite o segundo numero:'))

#if num1 > num2:
   # print('maior:',num1)
#else:
 #   print('maior;',num2)
4
#num1=float(input('Digite o primeiro numero:'))
#num2=float(input('Digite o segundo numero:'))
#num3=float(input('Digite o terceiro numero:'))

#if num1 >= num2 and num1 >= num3:
 #   print('Maior:',num1)
#elif num2 >= num1 and num2 >= num3:
 #   print('Maior:',num2)
#else:
    #print('Maior:',num3)
5
#num1=float(input('Digite o primeiro numero:'))
#num2=float(input('Digite o segundo numero:'))
#num3=float(input('Digite o terceiro numero:'))

#if num1 <= num2 and num1<= num3:
 #   print('Menor',num1)
#elif num2 <= num1 and num2 <= num3:
 #   print('Menor',num2)
#else:
#  print('Menor',num3)
6
#idade=int(input('Digite a dua idade:'))

#if idade >=18:
  #  print('Voce e maior de idade')
#else:
   # print('Voce e menor de idade')
7
#idade=int(input('Digite a dua idade:'))

#if idade < 16:
 #   print("Não pode votar")
#elif 18 <= idade <= 69:
 #   print("Pode votar e o voto é obrigatório")
#else:
#    print("Pode votar e o voto é facultativo")
8
#nota = float(input("Digite a nota: "))

#if nota >= 7:
 #   print("Aprovado")
#elif nota >= 5:
 #   print("Recuperação")
#else:
#    print("Reprovado")
9
#ano = int(input("Digite um ano: "))

#if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
 #   print("Ano bissexto")
#else:
 #   print("Ano não é bissexto")
10
#a = float(input("Digite o primeiro lado: "))
#b = float(input("Digite o segundo lado: "))
#c = float(input("Digite o terceiro lado: "))

#if a + b > c and a + c > b and b + c > a:

    #if a == b == c:
     #   print("Triângulo Equilátero")

    #elif a == b or a == c or b == c:
    #    print("Triângulo Isósceles")

  #  else:
 #       print("Triângulo Escaleno")

#else:
  #  print("Não forma um triângulo")
11
#compra = float(input("Digite o valor da compra: "))

#if compra >= 200:
#    desconto = compra * 0.10
#elif compra >= 100:
#    desconto = compra * 0.05
#else:
 #   desconto = 0

#total = compra - desconto

#print("Desconto:", desconto)
#print("Valor final:", total)
12
#salario = float(input("Digite o salário: "))

#if salario <= 2000:
#    imposto = 0
#elif salario <= 5000:
#    imposto = salario * 0.10
#else:
#    imposto = salario * 0.20

#print("Imposto:", imposto)
13
#usuario = input("Usuário: ")
#senha = input("Senha: ")

#if usuario == "admin" and senha == "1234":
#    print("Acesso permitido")
#else:
#   print("Usuário ou senha incorretos")
14
#temperatura = float(input("Digite a temperatura: "))

#if temperatura < 18:
 #   print("Frio")
#elif temperatura <= 26:
#    print("Agradável")
#else:
#    print("Quente")
15
#numero = float(input("Digite um número: "))

#if 10 <= numero <= 20:
 #   print("Está no intervalo")
#else:
 #   print("Está fora do intervalo")
16
#numero = int (input("Digite um número: "))

#if numero % 2 == 0 and numero % 3 == 0:
#    print("Divisível por 2 e 3")
#else:
#     print("Não é divisível por 2 e 3")   
17
#numero = int(input("Digite um número: "))
#if numero % 3 == 0 and numero % 5 == 0:
 #   print("Divisível por 3 e 5")
#else:
 #   print("Não é divisível por 3 e 5")
18
#peso = float(input("Digite o peso: "))
#altura = float(input("Digite a altura: "))

#imc = peso / (altura ** 2)

#if imc < 18.5:
#    print("Abaixo do peso")
#elif imc < 25:
#    print("Peso normal")
#else:
#    print("Acima do peso")
19
#numero = int(input("Digite um número: "))

#divisores = 0

#for i in range(1, numero + 1):
#    if numero % i == 0:
#        divisores += 1

#if divisores == 2:
#    print("É primo")
#else:
#    print("Não é primo")
20
#palavra = input("Digite uma palavra: ")

#if palavra == palavra[::-1]:
#    print("É um palíndromo")
#else:
#    print("Não é um palíndromo")
21
#senha = input("Digite uma senha: ")

#tem_numero = False
#tem_letra = False

#for caractere in senha:
#    if caractere.isdigit():
#        tem_numero = True

#    if caractere.isalpha():
 #       tem_letra = True

#if len(senha) >= 8 and tem_numero and tem_letra:
 #   print("Senha forte")
#else:
 #   print("Senha fraca")
22
#altura = float(input("Digite a altura: "))
#idade=int(input("Digite a idade: "))

#if altura >= 1.5 and idade >= 18:
#    print("Pode entrar")
#else:
#    print("Não pode entrar")
23
#renda = float(input("Digite a renda: "))
#divida = input("Possui dívida? (S/N): ").upper

#if renda >= 1000 and divida == 'N':
 #   print("Empréstimo aprovado")
#else:
#    print("Empréstimo negado")
25#
#valor = float(input("Digite o valor: "))
#cupom = input("Digite o cupom: ").upper()

#if cupom == "DESC10":
#    valor = valor * 0.90

#print("Valor final:", valor)
26#
#numero = int(input("Digite um número: "))

#achou = False

#for i in range(numero + 1):
  #  if i * i == numero:
 #       achou = True

#if achou:
#    print("Quadrado perfeito")
#else:
#    print("Não é quadrado perfeito")
27#
#numero = int(input("Digite um número: "))

#soma = 0

#for i in range(1, numero):
#    if numero % i == 0:
#        soma += i

#if soma == numero:
#    print("Número perfeito")
#else:
#   print("Não é número perfeito")
28
#numero = int(input("Digite um número de 3 digitos: "))

#centena = numero // 100
#dezena = (numero // 10) % 10
#unidade = numero % 10

#soma = centena**3 + dezena**3 + unidade**3

#if soma == numero:
 #   print("É um número de Armstrong")
#else:
#    print("Não é um número de Armstrong")
29
#preco = float(input("Digite o preço: "))
#categoria = input("Digite a categoria (A, B ou C): ").upper()

#if categoria == "A":
 #   preco = preco * 0.95
#elif categoria == "B":
#    preco = preco * 0.90
#elif categoria == "C":
 #   preco = preco * 0.85

#print("Preço final:", preco)
30
hora = int(input("Digite a hora (0-23): "))

if 5 <= hora < 11:
    print("Bom dia")
elif 11 <= hora < 18:
    print("Boa tarde")
elif 18 <= hora < 23:
    print("Boa noite")
else:
    print("Hora inválida")