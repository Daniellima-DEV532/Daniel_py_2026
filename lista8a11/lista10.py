1
#texto = input("Digite a mensagem: ")

#original = texto

#texto = texto.replace(" vc ", " você ")
#texto = texto.replace(" pq ", " porque ")
#texto = texto.replace(" tb ", " também ")
#texto = texto.replace(" q ", " que ")

#print("Original:")
#print(original)

#print("\nFormal:")
#print(texto)
2
#titulo = input("Digite o título: ")

#print(f"{titulo} — saiba mais!")

#print("#educacao #tecnologia #carreira")
3
#nome = input('Digite o nome:').lower()

#partes = nome.split()

#primeiro = partes[0]

#if len(partes) == 1:
 #   ultimo = primeiro

#else:
 #   ultimo = partes[-1]

#print(f'{primeiro}.{ultimo}@gmail.com')
4
#nome = input('Nome:')

#codigo = nome[:3].upper()

#print(f"{codigo}-2026-001")
5
#descricao = input("Descrição: ").lower()

#if "erro" in descricao or "bug" in descricao or "falha" in descricao:

 #   print("INCIDENTE")

#else:

 #   print("SOLICITAÇÃO")
6
#titulo = input("Título: ")

#titulo = titulo.lower()

#titulo = titulo.replace(" ", "")
#titulo = titulo.replace(".", "")
#titulo = titulo.replace(",", "")

#print(titulo)
#7
#texto = input("Digite o currículo: ").lower()

#print("Python:", texto.count("python"))
#print("Java:", texto.count("java"))
#print("SQL:", texto.count("sql"))
8
#frase = input('Digite uma frase:')

#if frase.endswith('?'):
 #   print('PERGUNTA')

#else:
    #print('AFIRMAÇAO')
9
#senha = input("Senha: ")

#tem_numero = False
#tem_maiuscula = False

#for caractere in senha:

 #   if caractere.isdigit():
  #      tem_numero = True

  #  if caractere.isupper():
   #     tem_maiuscula = True

#if len(senha) < 8:

 #   print("FRACA")

#elif tem_numero and tem_maiuscula:

 #   print("FORTE")

#else:

 #   print("MÉDIA")
10
#arquivo = input("Arquivo: ").lower()

#if arquivo.endswith(".pdf") or arquivo.endswith(".docx") or arquivo.endswith(".txt"):

 #   print("PERMITIDO")

#else:

 #   print("NÃO PERMITIDO")
11
#descriçao = input('Digite a descrição:')

#if len(descriçao) > 60:
 #   descriçao = descriçao[:57] + '...'

#print(descriçao)
12
#nomes = input("Digite os nomes: ")

#lista = nomes.split(",")

#print("Quantidade:", len(lista))
13
#texto = input("Digite o texto: ")

#frases = texto.split(".")

#contador = 0

#for frase in frases:

 #   if frase.strip() != "":
  #      contador += 1

#print("Quantidade de frases:", contador)
14
#texto = input("Digite o texto: ")

#contador = 0

#for caractere in texto:

#    if caractere.isdigit():

     #   contador += 1

     #   if contador == 8 or contador == 9:
    #        print("POSSÍVEL TELEFONE ENCONTRADO")
   #         break

  #  else:

 #       contador = 0
15
#nome = input("Digite o nome: ")

#while "  " in nome:
 #   nome = nome.replace("  ", " ")

#print(nome.title())
16
#assunto = input("Assunto: ").lower()

#if "pagamento" in assunto or "boleto" in assunto:

 #   print("FINANCEIRO")

#elif "matrícula" in assunto or "turma" in assunto:

 #   print("ACADÊMICO")

#elif "senha" in assunto or "erro" in assunto:

 #   print("TI")

#else:

  #  print("OUTROS")
17#
#log = input("Digite o log: ")

#partes = log.split(":")

#if len(partes) >= 2:
 #   print("Nível:", partes[0].strip())
 #   print("Mensagem:", partes[1].strip())
#else:
 #   print("Formato inválido! Lembre-se de usar ':' para separar o nível da mensagem.")
18
#texto = input("Digite a frase: ")

#contador = 0

#for caractere in texto:

 #   if caractere in "😀😂🔥❤️👍":
 #       contador += 1

#print("Quantidade:", contador)
19
#frase = input("Digite a frase: ")

#stopwords = ["de", "a", "o", "e", "para", "do", "da"]

#resultado = []

#for palavra in frase.split():

 #   if palavra.lower() not in stopwords:

  #      resultado.append(palavra)

#print(" ".join(resultado))
20
#nome = input("Nome: ")

#protocolo = input('Protocolo:')

#print(f"Olá, {nome}. Seu protocolo {protocolo} foi registrado e está em análise.")
21
#texto = input("Digite o texto: ")

#while "\n\n" in texto:
 #   texto = texto.replace("\n\n", "\n")

#print(texto)
22
assunto = input("Assunto: ").upper()

if "URGENTE" in assunto or "IMEDIATO" in assunto:
    print("URGENTE")
else:
    print("NORMAL")
23
intencao = input("Intenção: ").upper()

if intencao == "SAUDACAO":
    print("Olá! Como posso ajudar?")

elif intencao == "DUVIDA":
    print("Pode enviar sua dúvida.")

elif intencao == "RECLAMACAO":
    print("Lamentamos o ocorrido. Vamos ajudar.")

else:
    print("Intenção desconhecida.")




