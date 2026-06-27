1
#while True:
  #  try:
     #   numero = float(input("Digite um número: "))
      #  break
   # except:
   #     print("Entrada inválida. Tente novamente.")

#print("Número digitado:", numero)
2
#while True:
 #   numero = int(input("Digite um número entre 1 e 10: "))

    #if 1 <= numero <= 10:
     #   break

    #print("Número inválido.")

#print("Número aceito:", numero)
3
#while True:
    #texto = input("Digite um texto: ")

   # if texto.strip() != "":
  #      break

 #   print("Texto inválido.")

#print("Texto aceito:", texto)
5
#while True:
    #email = input("Digite um e-mail: ")

    #if "@" in email:
    #    posicao = email.find("@")

   #     if "." in email[posicao:]:
  #          break

 #   print("E-mail inválido.")

#print("E-mail válido.")
6
#while True:
  #  senha = input("Digite uma senha: ")

   # tem_numero = False

  #  for caractere in senha:
  #      if caractere.isdigit():
    #        tem_numero = True

   # if len(senha) >= 8 and tem_numero:
    #    break

   # print("Senha inválida.")

#print("Senha aceita.")
7
#num1 = float(input("Digite o primeiro número: "))

#while True:
    #num2 = float(input("Digite o segundo número: "))

   # if num2 != 0:
  #      break

 #   print("O segundo número não pode ser zero.")

#print("Resultado:", num1 / num2)
8
#while True:
    #print("1 - Somar")
    #print("2 - Subtrair")
    #print("3 - Sair")

    #opcao = int(input("Escolha: "))

   # if 1 <= opcao <= 3:
  #      break

 #   print("Opção inválida.")

#print("Opção escolhida:", opcao)
9
#while True:
    #numero = int(input("Digite um número positivo: "))

   # if numero > 0:
  #      break

 #   print("Número inválido.")

#print("Número aceito:", numero)
10
#while True:
#    valor = float(input("Digite um valor: "))

   # if valor >= 0:
   #     break

  #  print("Valor inválido.")

#print("Valor aceito:", valor)
11
#notas = []

#for i in range(3):
   # while True:
     #   nota = float(input(f"Digite a nota {i+1}: "))

       # if 0 <= nota <= 10:
          #  notas.append(nota)
          #  break

        #print("Nota inválida.")

#media = sum(notas) / 3

#print("Média:", media)
12
#while True:
  #  nome = input("Digite nome e sobrenome: ")

  #  palavras = nome.split()

   # if len(palavras) >= 2:
    #    break

   # print("Digite nome e sobrenome.")

#print("Nome válido.")
13
#while True:
    #cpf = input("Digite o CPF: ")

   # if len(cpf) == 11 and cpf.isdigit():
  #      break

 #   print("CPF inválido.")

#print("CPF aceito.")
14
#while True:
    #data = input("Digite a data (DD/MM): ")

    #partes = data.split("/")

 #   if len(partes) == 2:
     #    mes = int(partes[1])

   #     if 1 <= dia <= 30 and 1 <= mes <= 12:
  #          break

 #   print("Data inválida.")

#print("Data válida.")
15
#while True:
    #opcao = input("Digite S ou N: ").upper()

   # if opcao == "S" or opcao == "N":
  #      break

 #   print("Opção inválida.")

#print("Resposta:", opcao)
16
#while True:
   # altura = float(input("Digite a altura: "))

   # if 0.5 <= altura <= 2.5:
   #     break

   # print("Altura inválida.")

#print("Altura registrada.")
17
#while True:
   # texto = input("Digite um texto: ")

   # possui_numero = False

  #  for letra in texto:
   #     if letra.isdigit():
   #         possui_numero = True

  #  if not possui_numero:
     #   break

  #  print("O texto contém números.")

#print("Texto aceito.")
18
#while True:
 #   try:
  #      numero = int(input("Digite um número inteiro: "))
   #     break

   # except:
    #    print("Digite um número inteiro.")

#print("Número aceito:", numero)
19
#while True:
 #   n = int(input("Digite a quantidade: "))

  #  if n >= 1:
   #     break

   # print("Quantidade inválida.")

#numeros = []

#for i in range(n):
 #   numero = float(input("Digite um número: "))
  #  numeros.append(numero)

#print(numeros)
20
#while True:
 #   preco = float(input("Digite o preço: "))

  #  if preco >= 0:
   #     break

    #print("Preço inválido.")

#while True:
 #   quantidade = int(input("Digite a quantidade: "))

  #  if quantidade > 0:
   #     break

    #print("Quantidade inválida.")

#total = preco * quantidade

#print("Total:", total)
21
#while True:
 #   login = input("Digite o login: ")
  #  senha = input("Digite a senha: ")

  #  if len(login) >= 4 and len(senha) >= 4:
   #     break

   # print("Login ou senha inválidos.")

#print("Login e senha aceitos.")
22
#while True:
 #   texto = input("Digite um texto: ")

   # if len(texto) >= 10:
  #      break

 #   print("O texto deve ter pelo menos 10 caracteres.")

#print("Texto aceito.")
23
#while True:
 #   numero = int(input("Digite um número: "))

   # if numero % 5 == 0:
  #      break

 #   print("O número não é múltiplo de 5.")

#print("Número aceito.")
24
#while True:
    #numero = float(input("Digite um número: "))

   # if -100 <= numero <= 100:
  #      break

 #   print("Número fora do intervalo.")

#print("Número aceito.")
25
#while True:
   # nota = float(input("Digite a nota: "))

  #  if 0 <= nota <= 10:
  #      break

 #   print("Nota inválida.")

#print(f"Nota registrada: {nota}")
26
while True:
    palavra = input("Digite uma palavra: ")

    if " " not in palavra:
        break

    print("Digite apenas uma palavra.")

print("Palavra aceita.")
27
while True:
    texto = input("Digite um texto: ")

    if texto and texto[0] == texto[0].upper():
        break

    print("O texto deve começar com letra maiúscula.")

print("Texto aceito.")
28
while True:
    codigo = input("Digite o código: ")

    if len(codigo) == 6:
        letras = codigo[:3]
        numeros = codigo[3:]

        if letras.isalpha() and numeros.isdigit():
            break

    print("Código inválido.")

print("Código aceito.")
29
while True:
    try:
        numero = float(input("Digite um número: "))

        if numero == numero:
            break

        print("Número inválido.")

    except:
        print("Entrada inválida.")

print("Número aceito.")
30
while True:
    numero = int(input("Digite um número par: "))

    if numero % 2 == 0:
        break

    print("O número é ímpar. Tente novamente.")

print("Número aceito.")