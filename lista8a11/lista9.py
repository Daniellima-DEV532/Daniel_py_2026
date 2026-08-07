#frase = input("Digite uma frase: ").lower()

#contador = 0

#for letra in frase:

 #   if letra in "aeiou":
  #      contador += 1

#print("Quantidade de vogais:", contador)
2
#frase = input('Digite uma frase:').lower()

#contador = 0

#for  letra in frase:

 #   if letra.isalpha() and letra not in 'aeiou':
  #      contador += 1

#print('Quantidade de consoantes:', contador)
3
#frase = input('Digite uma frase:')

#palavras = frase.split()

#print('Quantidade de palavras:',len(palavras))
4
#frase = input('Digite uma frase:')

#print(frase[::-1])
5
#palavra = input('Digite uma palavra:').lower()

#if palavra == palavra[::-1]:
  #  print('É palíndromo')
#else:
  #  print('Não é palíndromo')
6
#frase = input('Digite uma frase:').lower()

#frase = frase.replace('','')
#frase = frase.replace('.','')
#frase = frase.replace(',','')

#if frase == frase[::-1]:
 #   print('É É palíndromo')

#else:
  #  print("Não é palíndromo")
7
#frase = input("Digite uma frase: ")

#resultado = ""

#for letra in frase:

  #  if letra.isalpha() or letra == " ":
 #       resultado += letra

#print(resultado)
8
#frase = input("Digite uma frase: ")

#print(frase.replace(" ", "-"))
9
#email = input("Digite o e-mail: ")

#if "@" in email:

   # posicao = email.find("@")

    #if "." in email[posicao:]:

   #     print("E-mail válido")

  #  else:

 #       print("E-mail inválido")

#else:

 #   print("E-mail inválido")
10
#senha = input("Digite uma senha: ")

#tem_letra = False
#tem_numero = False

#for caractere in senha:

    #if caractere.isalpha():
   #     tem_letra = True

  #  if caractere.isdigit():
 #       tem_numero = True

#if len(senha) >= 8 and tem_letra and tem_numero:

 #   print("Senha válida")

#else:

   # print("Senha inválida")
11
#frase = input("Digite uma frase: ").lower()

#palavras = frase.split()

#contagem = {}

#for palavra in palavras: 
    
 #   if palavra in contagem:
  #      contagem[palavra]+=1
   # else:
   #     contagem[palavra]=1 

#for palavra, quantidade in contagem.items():
 #   print(palavra, '->',quantidade)
12
#frase = input("Digite uma frase: ").lower()

#palavras = frase.split()

#contagem = {}

#for palavra in palavras:

 #   if palavra in contagem:
  #      contagem[palavra] += 1
#
 #   else:
  #      contagem[palavra] = 1

#mais_frequente = ""
#maior = 0

#for palavra in contagem:

 #   if contagem[palavra] > maior:
  #      maior = contagem[palavra]
   #     mais_frequente = palavra

#print("Mais frequente:", mais_frequente)
13
#frase = input("Digite uma frase: ")

#palavras = frase.split()

#maior = palavras[0]
#menor = palavras[0]

#for palavra in palavras:

 #   if len(palavra) > len(maior):
  #      maior = palavra

   # if len(palavra) < len(menor):
    #    menor = palavra

#print("Maior palavra:", maior)
#print("Menor palavra:", menor)
14
#nome = input("Digite o nome completo: ")

#partes = nome.split()

#resultado = partes[0]

#for i in range(1, len(partes)-1):
 #   resultado += " " + partes[i][0] + "."

#resultado += " " + partes[-1]

#print(resultado)
15
#texto = input("Digite um texto: ").lower()

#termo = input("Digite o termo: ").lower()

#print(texto.count(termo))
16
#texto = input("Digite um texto: ")

#while "  " in texto:

 #   texto = texto.replace("  ", " ")

#print(texto)
17
#frase = input("Digite uma frase: ")

#print(frase.title())
18
#texto = input("Digite um texto: ")

#palavras = texto.split()

#iniciais = ""

#for palavra in palavras:

 #   iniciais += palavra[0].upper()

#print(iniciais)
19
#texto = input("Digite um texto: ")

#valido = True

#for caractere in texto:

 #   if not (caractere.isalpha() or caractere == " "):
  #      valido = False

#if valido:
 #   print("Texto válido")

#else:
 #   print("Texto inválido")
20
#texto = input("Digite um texto: ")

#contador = 0

#for caractere in texto:

 #   if caractere.isdigit():
  #      contador += 1

#print("Quantidade de números:", contador)
21
#frase = input('Digite uma frase: ')

#resultado = ""

#for letra in frase:
    
 #   if letra.lower() in "aieou":
  #      resultado += letra

#else:
 #   resultado += letra

#print(resultado)
22
#texto = input('Digite um texto: ')
 
#prefixo = input('Digite o prefixo:')

#if texto.startswith(prefixo):
 #   print('O texto começa com esse prefixo.')

#else:
 #   print('O texto não começa com esse prefixo.')
23
#texto = input("Digite um texto: ")

#sufixo = input("Digite o sufixo: ")

#if texto.endswith(sufixo):

 #   print("O texto termina com esse sufixo.")

#else:

 #   print("O texto não termina com esse sufixo.")
24
#texto = input("Digite um texto: ")

#if len(texto) < 3:

 #   print(texto)

#else:

#    print(texto[:3])
25
#texto = input("Digite um texto: ")

#if len(texto) < 3:

 #   print(texto)

#else:

 #   print(texto[-3:])
26
#texto = input("Digite um texto: ")

#palavra_a = input("Palavra que será substituída: ")

#palavra_b = input("Nova palavra: ")

#print(texto.replace(palavra_a, palavra_b))
27
texto = input("Digite um texto: ")

letra = input("Digite uma letra: ")

for i in range(len(texto)):

    if texto[i] == letra:

        print(i)
28
texto = input("Digite um texto: ")

texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace(";", "")
texto = texto.replace(":", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")

print(texto)




