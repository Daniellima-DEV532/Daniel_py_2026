1
# alunos = [
#     ("João", 8.5),
#     ("Maria", 9.5),
#     ("Pedro", 7.0),
#     ("Ana", 10.0)
# ]

# alunos.sort(key=lambda aluno: aluno[1], reverse=True)

# for i, aluno in enumerate(alunos, start=1):
#     print(f"{i}º - {aluno[0]}: {aluno[1]}")
2
# produtos = [
#     ("Arroz", 50),
#     ("Feijão", 80),
#     ("Macarrão", 50),
#     ("Açúcar", 20)
# ]

# produtos.sort(key=lambda produto: produto[1], reverse=True)

# print("Mais vendidos:")
# print(produtos[0])

# print("\nTop 3:")
# for produto in produtos[:3]:
#     print(produto[0], "-", produto[1])
# 3
# emprestimos = [
#     ("Emprestimo 1", "10/08/2026"),
#     ("Emprestimo 2", "25/08/2026"),
#     ("Emprestimo 3", "05/07/2026")
# ]

# def converter_data(data):
#     dia, mes, ano = data.split("/")
#     return (int(ano), int(mes), int(dia))


# emprestimos.sort(
#     key=lambda x: converter_data(x[1]),
#     reverse=True
# )

# for titulo, data in emprestimos:
#     print(titulo, "-", data)
# 4
# tempos = [15, 8, 23, 10, 5, 30]

# menor = min(tempos)
# maior = max(tempos)

# print("Menor tempo:", menor)
# print("Maior tempo:", maior)
# 5
# precos = [50, 120, 80, 200, 35, 150]

# alvo = 100

# for i in range(len(precos)):

#     if precos[i] > alvo:
#         print(f"Índice {i}: R$ {precos[i]}")

# 6
# clientes = [
#     ("Daniel", 850),
#     ("Maria", 920),
#     ("João", 700),
#     ("Ana", 980)
# ]

# nome_busca = "Maria"

# encontrado = False

# for nome, pontuacao in clientes:

#     if nome.lower() == nome_busca.lower():
#         print("Cliente encontrado!")
#         print("Nome:", nome)
#         print("Pontuação:", pontuacao)

#         encontrado = True
#         break

# if not encontrado:
#     print("Não encontrado")
# 7
# contatos = [
#     ("Daniel", "99999-1111"),
#     ("Davi", "99999-2222"),
#     ("Maria", "99999-3333"),
#     ("Ana", "99999-4444")
# ]

# prefixo = "Da"

# for nome, telefone in contatos:

#     if nome.lower().startswith(prefixo.lower()):
#         print(nome, "-", telefone)
# 8
# def busca_binaria(array, valor):

#     inicio = 0
#     fim = len(array) - 1

#     while inicio <= fim:

#         meio = (inicio + fim) // 2

#         if array[meio] == valor:
#             return True

#         elif array[meio] < valor:
#             inicio = meio + 1

#         else:
#             fim = meio - 1

#     return False


# codigos = [50, 10, 80, 30, 20, 90]

# codigos.sort()

# print("Códigos:", codigos)

# x = 30

# if busca_binaria(codigos, x):
#     print("Código encontrado")
# else:
#     print("Código não encontrado")
# 9
# ids = [101, 102, 103, 101, 104, 102, 101]

# frequencia = {}

# for id in ids:
#     frequencia[id] = frequencia.get(id, 0) + 1

# for id, quantidade in frequencia.items():

#     if quantidade > 1:
#         print(id, "-", quantidade, "vezes")
# 10
# distancias = [10, 50, 30, 90, 20, 100, 70, 60]

# distancias.sort(reverse=True)

# print("5 maiores:")

# for distancia in distancias[:5]:
# #     print(distancia)
# 11
# from statistics import median

# n = int(input("Quantos salários serão informados? "))

# salarios = []

# for i in range(n):
#     salario = float(input(f"Digite o {i + 1}º salário: R$ "))
#     salarios.append(salario)

# media = sum(salarios) / n
# mediana = median(salarios)

# print(f"\nMédia salarial: R$ {media:.2f}")
# print(f"Mediana salarial: R$ {mediana:.2f}")

# if media > mediana:
#     print("A média é maior que a mediana.")
# elif mediana > media:
#     print("A mediana é maior que a média.")
# else:
#     print("A média e a mediana são iguais.")

# 12
# imcs = [17.5, 20.0, 22.5, 27.0, 30.5, 24.0]

# abaixo = 0
# normal = 0
# acima = 0

# for imc in imcs:

#     if imc < 18.5:
#         abaixo += 1

#     elif imc < 25:
#         normal += 1

#     else:
#         acima += 1

# print("Abaixo:", abaixo)
# print("Normal:", normal)
# print("Acima:", acima)

# 13
# gabarito = ["A", "B", "C", "D", "A"]

# alunos = [
#     ("Daniel", ["A", "B", "C", "C", "A"]),
#     ("Maria", ["A", "B", "C", "D", "A"]),
#     ("João", ["B", "B", "C", "D", "B"])
# ]

# resultado = []

# for nome, respostas in alunos:

#     nota = 0

#     for i in range(len(gabarito)):

#         if respostas[i].upper() == gabarito[i]:
#             nota += 1

#     resultado.append((nome, nota))

# resultado.sort(key=lambda x: x[1], reverse=True)

# for i, (nome, nota) in enumerate(resultado, 1):
#     print(f"{i}º - {nome}: {nota}")


# 14
# totais = [100, 200, 150, 1000, 250, 1200]

# media = sum(totais) / len(totais)

# print("Média:", media)

# print("Carrinhos acima de 2x a média:")

# for total in totais:

#     if total > 2 * media:
#         print(total)

# 15
# horarios = [
#     "14:30",
#     "08:15",
#     "12:00",
#     "07:45",
#     "18:20"
# ]

# horarios.sort()

# for horario in horarios:
#     print(horario)

# 16
# palavras = [
#     "python", "java", "python",
#     "c", "java", "python",
#     "javascript", "c"
# ]

# frequencia = {}

# for palavra in palavras:
#     frequencia[palavra] = frequencia.get(palavra, 0) + 1

# ordenadas = sorted(
#     frequencia.items(),
#     key=lambda x: x[1],
#     reverse=True
# )

# for palavra, quantidade in ordenadas[:10]:
#     print(palavra, "-", quantidade)

# 17
# presencas = [90, 60, 80, 50, 70, 95]

# alunos = []

# for i, percentual in enumerate(presencas, 1):

#     if percentual < 75:
#         alunos.append((i, percentual))

# alunos.sort(key=lambda x: x[1])

# for numero, percentual in alunos:
#     print(f"Aluno {numero}: {percentual}%")

# 18
# despesas = [
#     ("Alimentação", 100),
#     ("Transporte", 50),
#     ("Alimentação", 200),
#     ("Lazer", 150),
#     ("Transporte", 100)
# ]

# totais = {}

# for categoria, valor in despesas:

#     if categoria in totais:
#         totais[categoria] += valor
#     else:
#         totais[categoria] = valor

# ranking = sorted(
#     totais.items(),
#     key=lambda x: x[1],
#     reverse=True
# )

# for categoria, total in ranking:
#     print(categoria, "-", total)

# 19
# eventos = [
#     "login",
#     "erro",
#     "logout",
#     "login",
#     "erro",
#     "compra"
# ]

# resultado = []

# for evento in eventos:

#     if evento not in resultado:
#         resultado.append(evento)

# for evento in resultado:
#     print(evento)

20
# pesos = [10, 20, 30, 40, 50]

# k = 70

# encontrado = False

# for i in range(len(pesos)):

#     for j in range(i + 1, len(pesos)):

#         if pesos[i] + pesos[j] == k:

#             print("Par encontrado:")
#             print(pesos[i], "+", pesos[j], "=", k)

#             encontrado = True
#             break

#     if encontrado:
#         break

# if not encontrado:
#     print("Não existe")

21
# notas = [5, 4, 5, 3, 4, 5, 2, 4]

# frequencia = {}

# for nota in notas:
#     frequencia[nota] = frequencia.get(nota, 0) + 1

# maior = max(frequencia.values())

# moda = None

# for nota, quantidade in frequencia.items():

#     if quantidade == maior:

#         if moda is None or nota < moda:
#             moda = nota

# print("Moda:", moda)

22
# participantes = [
#     ("Daniel", 90),
#     ("Maria", 95),
#     ("Ana", 95),
#     ("João", 80)
# ]

# participantes.sort(
#     key=lambda x: (-x[1], x[0])
# )

# for i, (nome, pontos) in enumerate(participantes, 1):
#     print(f"{i}º - {nome}: {pontos}")

23
produtos = [
    ("Mouse", 10),
    ("Teclado", 0),
    ("Monitor", 5),
    ("Webcam", 0),
    ("Fone", 0)
]

indisponiveis = []

for nome, estoque in produtos:

    if estoque == 0:
        indisponiveis.append(nome)

indisponiveis.sort()

for produto in indisponiveis:
    print(produto)

24


25


26


27


28


29


30