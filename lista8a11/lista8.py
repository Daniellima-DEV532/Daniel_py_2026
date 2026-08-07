1
#soma = 0

#numero = int(input("Digite um número (0 para sair): "))

#while numero != 0:
  #  soma += numero
 #   numero = int(input("Digite um número (0 para sair): "))

#print("Soma:", soma)
#2
#soma = 0
#contador = 0

#numero = int(input("Digite um número (0 para sair): "))

#while numero != 0:
 #   soma += numero
  #  contador += 1

   # numero = int(input("Digite um número (0 para sair): "))

#if contador > 0:
 #   media = soma / contador
  #  print("Média:", media)

#else:
 #   print("Nenhum número foi digitado.")
3
#positivos = 0
#negativos = 0

#numero = int(input("Digite um número (0 para sair): "))

#while numero != 0:

   # if numero > 0:
  #      positivos += 1

 #   else:
3  #      negativos += 1

 #   numero = int(input("Digite um número (0 para sair): "))

#print("Positivos:", positivos)
#print("Negativos:", negativos)
4
#numero = int(input("Digite um número (0 para sair): "))

#if numero != 0:

    #maior = numero
    #menor = numero

   # while numero != 0:

  #           maior = numero
#
    #    if numero < menor:
   #         menor = numero

  #      numero = int(input("Digite um número (0 para sair): "))

 #   print("Maior:", maior)
#    print("Menor:", menor)

#else:
  #  print("Nenhum número foi digitado.")
5
#soma = 0
#contador = 0

#idade = int(input("Digite uma idade (-1 para sair): "))

#while idade != -1:

#    soma += idade
 #   contador += 1

 #   idade = int(input("Digite uma idade (-1 para sair): "))

#if contador > 0:
 #   print("Média:", soma / contador)

#else:
#    print("Nenhuma idade foi informada.")
6
#contador = 0

#idade = int(input("Digite uma idade (-1 para sair): "))

#while idade != -1:

 #   if idade >= 18:
  #      contador += 1

   # idade = int(input("Digite uma idade (-1 para sair): "))

#print("Maiores de idade:", contador)
7
#total = 0
#quantidade = 0

#valor = float(input("Digite o valor da compra (0 para sair): "))

#while valor != 0:

 #   total += valor
  #  quantidade += 1

   # valor = float(input("Digite o valor da compra (0 para sair): "))

#print("Total das compras:", total)
#print("Quantidade:", quantidade)
8
#nota = float(input("Digite uma nota (-1 para sair): "))

#if nota != -1:

 #   maior = nota
  #  menor = nota

   # while nota != -1:
#
 #       if nota > maior:
  #          maior = nota
#
 #       if nota < menor:
  #          menor = nota
#
 #       nota = float(input("Digite uma nota (-1 para sair): "))

  #  print("Maior nota:", maior)
   # print("Menor nota:", menor)

#else:
 #   print("Nenhuma nota foi informada.")
9
#soma = 0

#numero = int(input("Digite um número (0 para sair): "))

#while numero != 0:

 #   if numero % 2 == 0:
  #      soma += numero

   # numero = int(input("Digite um número (0 para sair): "))

#print("Soma dos pares:", soma)
10
#soma = 0

#numero = int(input("Digite um número (0 para sair): "))

#while numero != 0:

   # if numero % 2 != 0:
  #      soma += numero

 #   numero = int(input("Digite um número (0 para sair): "))

#print("Soma dos ímpares:", soma)
11
#contador = 0

#texto = input("Digite um texto (FIM para sair): ").upper()

#while texto != "FIM":

 #   contador += 1

  #  texto = input("Digite um texto (FIM para sair): ").upper()

#print("Quantidade de textos:", contador)
12
#nome = input("Nome (FIM para sair): ").upper()

#if nome != "FIM":

 #   idade = int(input("Idade: "))

  #  menor_idade = idade
   # mais_novo = nome

   # nome = input("Nome (FIM para sair): ").upper()

    #while nome != "FIM":

     #   idade = int(input("Idade: "))

      #  if idade < menor_idade:
       #     menor_idade = idade
        #    mais_novo = nome

        #nome = input("Nome (FIM para sair): ").upper()

#    print("Pessoa mais nova:", mais_novo)

#else:
 #   print("Nenhum nome foi informado.")
13
#a = float(input("Digite o primeiro valor: "))
#b = float(input("Digite o segundo valor: "))

#while not (1 <= a <= 100 and 1 <= b <= 100):

 #   a = float(input("Digite o primeiro valor: "))
  #  b = float(input("Digite o segundo valor: "))

#print("Soma:", a + b)
14
opcao = -1

while opcao != 0:

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 0:
        break

    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))

    if opcao == 1:
        print(a + b)

    elif opcao == 2:
        print(a - b)

    elif opcao == 3:
        print(a * b)

    elif opcao == 4:
        if b != 0:
            print(a / b)
        else:
            print("Não é possível dividir por zero.")
15
positivos = 0
negativos = 0

numero = int(input("Digite um número (0 para sair): "))

while numero != 0:

    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    numero = int(input("Digite um número (0 para sair): "))

total = positivos + negativos

if total > 0:

    print("Positivos:", positivos * 100 / total, "%")
    print("Negativos:", negativos * 100 / total, "%")

else:
    print("Nenhum número informado.")
16
soma_salarios = 0
soma_filhos = 0
contador = 0

salario = float(input("Salário (-1 para sair): "))

maior_salario = salario

while salario >= 0:

    filhos = int(input("Número de filhos: "))

    soma_salarios += salario
    soma_filhos += filhos
    contador += 1

    if salario > maior_salario:
        maior_salario = salario

    salario = float(input("Salário (-1 para sair): "))

if contador > 0:

    print("Média salarial:", soma_salarios / contador)
    print("Média de filhos:", soma_filhos / contador)
    print("Maior salário:", maior_salario)

else:
    print("Nenhum dado informado.")