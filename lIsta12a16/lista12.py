# 1
# #n = int(input("Quantidade de alunos: "))

# #soma = 0

# #for i in range(n):

#   #  nota = float(input("Nota: "))

#  #   soma += nota

# #media = soma / n

# #print(f"Média da turma: {media:.2f}")
# 2
# n = int(input("Quantidade de alunos: "))

# aprovados = 0
# recuperacao = 0
# reprovados = 0


# for i in range(n):

#     nota = float(input("Média: "))

#     if nota >= 7:
#         aprovados += 1

#     elif nota >= 5:
#         recuperacao += 1

#     else:
#         reprovados += 1


# print("Aprovados:", aprovados)
# print("Recuperação:", recuperacao)
# print("Reprovados:", reprovados)
# 3
# total = 0
# maior = 0
# dia_maior = 0


# for dia in range(1, 8):

#     venda = float(input(f"Venda do dia {dia}: "))

#     total += venda

#     if venda > maior:

#         maior = venda
#         dia_maior = dia


# print("Total:", total)
# print("Maior venda:", maior)
# print("Dia:", dia_maior)
# 4
# n = int(input("Quantidade: "))

# vendas = []


# for i in range(n):

#     valor = float(input("Venda: "))

#     vendas.append(valor)


# vendas.sort(reverse=True)


# print(vendas)
# 5
# for i in range(10):

#     quantidade = int(input(f"Produto {i+1}: "))

#     if quantidade < 5:

#         print("Produto abaixo do mínimo:", i+1)
# 6
# total = 0

# for i in range(10):

#     preço = float(input("Preço: "))

#     quantidade = int(input("Quantidade: "))

#     valor = preço * quantidade

#     total += valor

#     print('Valor do produto:', valor)

# print('Total:', total)
# 7
# presentes = 0

# for i in range(30):

#      presenca = int(input("Presença: "))
     
#      if presenca == 1:
#          presentes += 1

# percentual = (presentes / 30) * 100

# print(f"Percentual de presença: {percentual:.2f}%")

# if percentual >= 75:
#     print("REGULAR")
# else:
#     print("EM REISCO")
8
# n = int(input("Quantidade: "))


# faixa1 = 0
# faixa2 = 0
# faixa3 = 0
# faixa4 = 0
# faixa5 = 0


# for i in range(n):

#     idade = int(input("Idade: "))


#     if idade <= 17:
#         faixa1 += 1

#     elif idade <= 35:
#         faixa2 += 1

#     elif idade <= 50:
#         faixa3 += 1

#     elif idade <= 65:
#         faixa4 += 1

#     else:
#         faixa5 += 1


# print("0-17:", faixa1)
# print("18-35:", faixa2)
# print("36-50:", faixa3)
# print("51-65:", faixa4)
# print(">65:", faixa5)
# 9
# n = int(input("Quantidade: "))

# salarios = []


# for i in range(n):

#     salario = float(input("Salário: "))

#     salarios.append(salario)


# media = sum(salarios) / n

# maior = max(salarios)

# menor = min(salarios)


# print("Média:", media)
# print("Maior:", maior)
# print("Menor:", menor)
# 10
# salarios = [1500, 2000, 3000, 5000]

# media = sum(salarios) / len(salarios)


# contador = 0


# for salario in salarios:

#     if salario > media:

#         contador += 1


# print("Acima da média:", contador)
11
# n = int(input("Quantidade de pessoas : "))

# imcs = []

# for i in range(n):
#     peso = float(input("Peso: "))
#     altura = float(input("Altura: "))

#     imc = peso / (altura ** 2)

#     imcs.append(imc)

# media = sum(imcs) / n

# print("Média do IMC:", media)
12
# n = int(input("Quantidade de alunos: "))

# maior_nota = -1
# aluno_maior_nota = ""

# for i in range(n):

#     nome = input("Nome: ")
#     nota = float(input("Nota: "))

#     if nota > maior_nota:
#         maior_nota = nota
#         aluno_maior_nota = nome

# print("Aluno com maior nota:", aluno_maior_nota)
# print("Maior nota:", maior_nota)
13
# n = int(input("Quantidade de alunos: "))

# for i in range(n):

#     nome = input("Nome: ")
#     nota = float(input("Nota: "))

#     if nota >= 7:

#         print(f"{nome} - {nota}")
14
# n = int(input("Quantidade de atendimentos: "))

# tempos = []

# for i in range(n):

#     tempo = float(input("Tempo em minutos: "))

#     tempos.append(tempo)

# media = sum(tempos) / len(tempos)

# maior = max(tempos)
# menor = min(tempos)

# print(f"Média: {media:.2f}")
# print(f"Maior tempo: {maior}")
# print(f"Menor tempo: {menor}")
15
# n = int(input("Quantidade de corridas: "))

# tarifa = float(input("Tarifa por km: "))

# distancias = []

# total = 0

# for i in range(n):

#     distancia = float(input("Distância: "))

#     distancias.append(distancia)

#     total += distancia * tarifa

# maior = max(distancias)

# print(f"Faturamento total: R$ {total:.2f}")
# print(f"Maior distância: {maior:.2f} km")
16
# n = int(input("Quantidade de pessoas: "))

# total = 0

# for i in range(n):
#     dias = int(input("Dias de atraso: "))
#     total += dias

# print(f"Total de dias de atraso: {total}")
# 17
# n = int(input("Quantidade de produtos: "))

# precos = []

# for i in range(n):

#     preco = float(input("Preço: "))

#     precos.append(preco)

# precos.sort(reverse=True)

# total = 0

# for i in range(len(precos)):

#     if i < 3:

#         preco_final = precos[i] * 0.90

#     else:

#         preco_final = precos[i]

#     total += preco_final

# print(f"Total final: R$ {total:.2f}")
18
# n = int(input("Quantidade de tentativas: "))

# falhas = 0

# for i in range(n):
#     resultado = int(input("Resultado (1=sucesso, 0=falha): "))

#     if resultado == 0:

#         falhas += 1

# taxa = (falhas / n) * 100

# print(f"Quantidade de falhas: {falhas}")
19
# curtidas = []

# for i in range(10):

#     quantidade = int(input(f"Quantidade de curtidas do post {i+1}: "))

#     curtidas.append(quantidade)

# curtidas.sort(reverse=True)

# print("Top 3:")

# print(curtidas[0])
# print(curtidas[1])
# print(curtidas[2])
20
# n = int(input("Quantidade de notas: "))

# notas = []

# for i in range(n):

#     nota = float(input("Nota: "))

#     notas.append(nota)

# maior = max(notas)
# menor = min(notas)

# amplitude = maior - menor

# print(f"Amplitude: {amplitude:.2f}")
21
#  n = int(input("Quantidade de pacotes: "))

# caixas = 1
# peso_atual = 0

# for i in range(n):

#     peso = float(input("Peso do pacote: "))

#     if peso_atual + peso <= 10:
#         peso_atual += peso
#     else:
#         caixas += 1
#         peso_atual = peso

# print("Caixas utilizadas:", caixas)
# 22
# n = int(input("Quantidade de participantes: "))

# pontuacoes = []

# for i in range(n):
#     pontos = float(input("Pontuação: "))
#     pontuacoes.append(pontos)

# pontuacoes.sort(reverse=True)

# print("OURO:", pontuacoes[0])
# print("PRATA:", pontuacoes[1])
# print("BRONZE:", pontuacoes[2])
# 23
# n = int(input("Quantidade de dias: "))
# limite = int(input("Limite de defeitos: "))

# for i in range(n):

#     defeitos = int(input(f"Defeitos do dia {i + 1}: "))

#     if defeitos > limite:
#         print("Dia", i + 1, "acima do limite")
24
# n = int(input("Quantidade de tarefas: "))

# pendentes = []

# for i in range(n):

#     tarefa = input("Tarefa: ")
#     concluida = input("Concluída? (S/N): ").upper()

#     if concluida == "N":
#         pendentes.append(tarefa)

# print("Tarefas pendentes:")

# for tarefa in pendentes:
#     print(tarefa)
# 25
# n = int(input("Quantidade de palavras: "))

# frequencia = {}

# for i in range(n):

#     palavra = input("Palavra: ").lower()

#     if palavra in frequencia:
#         frequencia[palavra] += 1
#     else:
#         frequencia[palavra] = 1

# for palavra, quantidade in frequencia.items():

#     print(palavra, "->", quantidade)
# 26
# receitas = []
# despesas = []

# for i in range(12):

#     receita = float(input(f"Receita do mês {i + 1}: "))
#     receitas.append(receita)

# for i in range(12):

#     despesa = float(input(f"Despesa do mês {i + 1}: "))
#     despesas.append(despesa)

# melhor_saldo = receitas[0] - despesas[0]
# melhor_mes = 1

# for i in range(12):

#     saldo = receitas[i] - despesas[i]

#     if saldo > melhor_saldo:

#         melhor_saldo = saldo
#         melhor_mes = i + 1

# print("Melhor mês:", melhor_mes)
# print("Melhor saldo:", melhor_saldo)
# 27
# n = int(input("Quantidade de números: "))

# numeros = []

# for i in range(n):

#     numero = float(input("Número: "))
#     numeros.append(numero)

# soma = sum(numeros)

# media = soma / len(numeros)

# numeros.sort()

# meio = len(numeros) // 2

# if len(numeros) % 2 == 0:

#     mediana = (numeros[meio - 1] + numeros[meio]) / 2

# else:

#     mediana = numeros[meio]


# frequencia = {}

# for numero in numeros:

#     if numero in frequencia:
#         frequencia[numero] += 1
#     else:
#         frequencia[numero] = 1


# maior_frequencia = 0
# moda = None

# for numero, quantidade in frequencia.items():

#     if quantidade > maior_frequencia:

#         maior_frequencia = quantidade
#         moda = numero


# print("Soma:", soma)
# print("Média:", media)
# print("Mediana:", mediana)

# if maior_frequencia > 1:
#     print("Moda:", moda)
# else:
#     print("Não existe moda")
# 28
# n = int(input("Quantidade de valores: "))

# valores = []

# for i in range(n):

#     valor = float(input("Valor: "))
#     valores.append(valor)

# media = sum(valores) / len(valores)

# limite = media * 2

# print("Média:", media)
# print("Valores fora do padrão:")

# for valor in valores:

#     if valor > limite:
#         print(valor)
29
n = int(input("Quantidade de alunos: "))

notas = []

for i in range(n):

    nota = float(input("Nota: "))
    notas.append(nota)

notas.sort(reverse=True)

quantidade = int(n * 0.20)

if quantidade < 1:
    quantidade = 1

nota_corte = notas[quantidade - 1]

print("Nota de corte:", nota_corte)

print("Classificados:")

for i in range(quantidade):

    print(notas[i])
30
n = int(input("Quantidade de pessoas: "))

destinos = {}

for i in range(n):

    destino = input("Destino: ").strip().lower()

    if destino in destinos:

        destinos[destino] += 1

    else:

        destinos[destino] = 1


for destino, quantidade in destinos.items():

    print(destino, "->", quantidade)

''

