# 1
# def busca_linear(array, valor):
#     for i in range(len(array)):
#         if array[i] == valor:
#             return i
#     return -1

# numeros = [10, 20, 30, 40]
# print(busca_linear(numeros, 30))
2
# def busca_binaria(array, valor):
#     inicio = 0
#     fim = len(array) - 1

#     while inicio <= fim:
#         meio = (inicio + fim) // 2

#         if array[meio] == valor:
#             return meio

#         elif array[meio] < valor:
#             inicio = meio + 1

#         else:
#             fim = meio - 1

#     return -1


# numeros = [10, 20, 30, 40, 50, 60]

# print(busca_binaria(numeros, 40))
3
# def bubble_sort(array):
#     n = len(array)

#     for i in range(n):
#         for j in range(0, n - i - 1):

#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]

#     return array


# numeros = [5, 2, 8, 1, 3]

# print(bubble_sort(numeros))
# 4
# def selection_sort(array):
#     n = len(array)

#     for i in range(n):
#         menor = i

#         for j in range(i + 1, n):
#             if array[j] < array[menor]:
#                 menor = j

#         array[i], array[menor] = array[menor], array[i]

#     return array


# numeros = [64, 25, 12, 22, 11]

# print(selection_sort(numeros))
# 5
# def insertion_sort(array):

#     for i in range(1, len(array)):
#         chave = array[i]
#         j = i - 1

#         while j >= 0 and array[j] > chave:
#             array[j + 1] = array[j]
#             j -= 1

#         array[j + 1] = chave

#     return array


# numeros = [5, 2, 4, 6, 1, 3]

# print(insertion_sort(numeros))
6
# def merge_sort(array):

#     if len(array) <= 1:
#         return array

#     meio = len(array) // 2

#     esquerda = merge_sort(array[:meio])
#     direita = merge_sort(array[meio:])

#     resultado = []

#     i = 0
#     j = 0

#     while i < len(esquerda) and j < len(direita):

#         if esquerda[i] < direita[j]:
#             resultado.append(esquerda[i])
#             i += 1
#         else:
#             resultado.append(direita[j])
#             j += 1

#     resultado.extend(esquerda[i:])
#     resultado.extend(direita[j:])

#     return resultado


# numeros = [38, 27, 43, 3, 9, 82, 10]

# print(merge_sort(numeros))
7
# def quick_sort(array):

#     if len(array) <= 1:
#         return array

#     pivo = array[len(array) // 2]
#     esquerda = [x for x in array if x < pivo]
#     meio = [x for x in array if x == pivo]
#     direita = [x for x in array if x > pivo]

#     return quick_sort(esquerda) + meio + quick_sort(direita)


# numeros = [38, 27, 43, 3, 9, 9, 82, 10]

# print(quick_sort(numeros))
8
# def counting_frequency(array):

#     frequencia = {}

#     for numero in array:

#         if numero in frequencia:
#             frequencia[numero] += 1
#         else:
#             frequencia[numero] = 1

#     return frequencia


# numeros = [38, 27, 43, 3, 9, 9, 82, 10]

# print(counting_frequency(numeros))
# 9
# def eh_palindromo(texto):

#     inicio = 0
#     fim = len(texto) - 1

#     while inicio < fim:

#         if texto[inicio] != texto[fim]:
#             return False

#         inicio += 1
#         fim -= 1

#     return True


# print(eh_palindromo("radar"))
# print(eh_palindromo("python"))
# 10
# def mdc(a, b):

#     while b != 0:

#         resto = a % b

#         print(a, "%", b, "=", resto)

#         a = b
#         b = resto

#     return a


# resultado = mdc(48, 18)

# # print("MDC =", resultado)
# 11
# cache = {}

# def fibonacci(n):

#     if n in cache:
#         return cache[n]

#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

#     return cache[n]


# print(fibonacci(10))
# 12
# def eh_armstrong(numero):

#     digitos = str(numero)
#     quantidade = len(digitos)

#     soma = 0

#     for digito in digitos:
#         soma += int(digito) ** quantidade

#     return soma == numero


# print(eh_armstrong(153))
# print(eh_armstrong(123))
# 13
# def crivo(n):

#     primo = [True] * (n + 1)

#     primo[0] = False
#     primo[1] = False

#     p = 2

#     while p * p <= n:

#         if primo[p]:

#             for i in range(p * p, n + 1, p):
#                 primo[i] = False

#         p += 1

#     resultado = []

#     for i in range(n + 1):

#         if primo[i]:
#             resultado.append(i)

#     return resultado


# print(crivo(30))
# 14
# def decimal_binario(numero):

#     if numero == 0:
#         return "0"

#     resultado = ""

#     while numero > 0:

#         resto = numero % 2

#         resultado = str(resto) + resultado

#         numero = numero // 2

#     return resultado


# print(decimal_binario(10))
# 15
# def decimal_hexadecimal(numero):

#     simbolos = "0123456789ABCDEF"

#     if numero == 0:
#         return "0"

#     resultado = ""

#     while numero > 0:

#         resto = numero % 16

#         resultado = simbolos[resto] + resultado

#         numero = numero // 16

#     return resultado


# print(decimal_hexadecimal(255))
16
# def soma_quadrados(numero):

#     soma = 0

#     while numero > 0:

#         digito = numero % 10

#         soma += digito ** 2

#         numero //= 10

#     return soma


# def numero_feliz(numero):

#     tentativas = 0

#     while numero != 1 and tentativas < 100:

#         numero = soma_quadrados(numero)

#         tentativas += 1

#     return numero == 1


# print(numero_feliz(19))
# print(numero_feliz(20))
17
# def numero_perfeito(numero):

#     soma = 0

#     for i in range(1, numero):

#         if numero % i == 0:
#             soma += i

#     return soma == numero


# print(numero_perfeito(6))
# print(numero_perfeito(28))
18
# def validar_senha(senha):

#     erros = []

#     if len(senha) < 8:
#         erros.append("A senha deve ter pelo menos 8 caracteres.")

#     if not any(c.isupper() for c in senha):
#         erros.append("A senha deve ter uma letra maiúscula.")

#     if not any(c.islower() for c in senha):
#         erros.append("A senha deve ter uma letra minúscula.")

#     if not any(c.isdigit() for c in senha):
#         erros.append("A senha deve ter um número.")

#     especiais = "!@#$%^&*"

#     if not any(c in especiais for c in senha):
#         erros.append("A senha deve ter um caractere especial.")

#     return erros


# senha = "igd182324"

# erros = validar_senha(senha)

# if len(erros) == 0:
#     print("Senha válida!")
# else:
#     for erro in erros:
#         print(erro)
19
# def remover_duplicados(array):

#     resultado = []

#     for elemento in array:

#         if elemento not in resultado:
#             resultado.append(elemento)

#     return resultado


# numeros = [3, 5, 3, 2, 5, 8, 2]

# print(remover_duplicados(numeros))
# 20
# def rotacionar(array, k):

#     n = len(array)

#     k = k % n

#     resultado = [0] * n

#     for i in range(n):
#         nova_posicao = (i + k) % n
#         resultado[nova_posicao] = array[i]

#     return resultado


# numeros = [1, 2, 3, 4, 5]

# print(rotacionar(numeros, 2))
21
# def merge_arrays(a, b):

#     resultado = []

#     i = 0
#     j = 0

#     while i < len(a) and j < len(b):

#         if a[i] < b[j]:
#             resultado.append(a[i])
#             i += 1
#         else:
#             resultado.append(b[j])
#             j += 1

#     while i < len(a):
#         resultado.append(a[i])
#         i += 1

#     while j < len(b):
#         resultado.append(b[j])
#         j += 1

#     return resultado


# a = [1, 4, 7]
# b = [2, 3, 8]

# print(merge_arrays(a, b))
# 22
# def contar_inversoes(array):

#     contador = 0

#     for i in range(len(array)):

#         for j in range(i + 1, len(array)):

#             if array[i] > array[j]:
#                 contador += 1

#     return contador


# numeros = [2, 4, 1, 3]

# print(contar_inversoes(numeros))
# 23
# def verificar_ordem(array):

#     crescente = True
#     decrescente = True

#     for i in range(len(array) - 1):

#         if array[i] > array[i + 1]:
#             crescente = False

#         if array[i] < array[i + 1]:
#             decrescente = False

#     if crescente:
#         return "Crescente"

#     elif decrescente:
#         return "Decrescente"

#     else:
#         return "Não ordenado"


# print(verificar_ordem([1, 2, 3, 4]))
# print(verificar_ordem([4, 3, 2, 1]))
# print(verificar_ordem([1, 4, 2, 3]))
24
# def mediana(array):

#     array = sorted(array)

#     n = len(array)

#     meio = n // 2

#     if n % 2 == 1:
#         return array[meio]

#     else:
#         return (array[meio - 1] + array[meio]) / 2


# print(mediana([1, 3, 5]))
# print(mediana([1, 3, 5, 7]))
# 25
# def moda(array):

#     frequencia = {}

#     for numero in array:

#         frequencia[numero] = frequencia.get(numero, 0) + 1

#     maior_frequencia = max(frequencia.values())

#     candidatos = []

#     for numero in frequencia:

#         if frequencia[numero] == maior_frequencia:
#             candidatos.append(numero)

#     return min(candidatos)


# print(moda([2, 2, 3, 3, 5]))
# 26
# def maior_soma(array):

#     atual = array[0]
#     maior = array[0]

#     for i in range(1, len(array)):

#         atual = max(array[i], atual + array[i])

#         maior = max(maior, atual)

#     return maior


# numeros = [-2, 1, -3, 4, -1, 2, 1, -5]

# print(maior_soma(numeros))
# 27
# def sao_anagramas(texto1, texto2):

#     texto1 = texto1.replace(" ", "").lower()
#     texto2 = texto2.replace(" ", "").lower()

#     return sorted(texto1) == sorted(texto2)


# print(sao_anagramas("Roma", "Amor"))
# print(sao_anagramas("Python", "Java"))
# 28
# def comprimir(texto):

#     resultado = ""

#     contador = 1

#     for i in range(len(texto)):

#         if i + 1 < len(texto) and texto[i] == texto[i + 1]:
#             contador += 1

#         else:
#             resultado += texto[i] + str(contador)
#             contador = 1

#     return resultado


# print(comprimir("aaabb"))
29
def descomprimir(texto):

    resultado = ""

    i = 0

    while i < len(texto):

        caractere = texto[i]

        i += 1

        numero = ""

        while i < len(texto) and texto[i].isdigit():

            numero += texto[i]

            i += 1

        resultado += caractere * int(numero)

    return resultado


print(descomprimir("a3b2"))
30
class Pilha:

    def __init__(self):
        self.itens = []

    def push(self, valor):
        self.itens.append(valor)

    def pop(self):

        if len(self.itens) == 0:
            return None

        return self.itens.pop()

    def top(self):

        if len(self.itens) == 0:
            return None

        return self.itens[-1]

    def is_empty(self):
        return len(self.itens) == 0


pilha = Pilha()

pilha.push(10)
pilha.push(20)
pilha.push(30)

print(pilha.itens)

print("Saiu:", pilha.pop())

print("Topo:", pilha.top())

print(pilha.itens)