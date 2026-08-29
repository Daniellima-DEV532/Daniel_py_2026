# 1
# def soma(a, b):
#     return a + b


# resultado = soma(20, 5)

# print(resultado)
# 2
# def sub(a, b):
#     return a - b


# resultado = sub(35, 5)

# print(resultado)
# 3
# def mult(a, b):
#     return a * b


# resultado = mult(25, 3)

# print(resultado)
# 4
# def div(a, b):
#     return a / b

# resultado = div(25, 5)
# print(resultado)
# 5
# def ehPar(n):

#     if n % 2 == 0:
#         return True

#     return False


# print(ehPar(10))
# print(ehPar(7))
6
# def ehPrimo(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# print(ehPrimo(10))
# print(ehPrimo(7))
# 7
# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1

#     resultado = 1
#     for i in range(2, n + 1):
#         resultado *= i

#     return resultado

# print(fatorial(5))
# print(fatorial(0))
# 8
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))
# print(fibonacci(0))
# 9
# def maior(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(maior(10, 5))
# print(maior(3, 7))
10
# def menor(a, b):

#     if a < b:
#         return a

#     return b


# print(menor(10, 20))
# 11
# def media3(a, b, c):

#     return (a + b + c) / 3  

# print(media3(15, 60, 30))
12
# def cToF(c):
#     return c * 9 / 5 + 32


# def fToC(f):
#     return 5 / 9 * (f - 32)


# print(cToF(30))
# print(fToC(86))
13
# def areaRet(base, altura):
#     return base * altura


# print(areaRet(10, 5))
14
# def areaCirc(raio):
#     return 3.14 * raio ** 2

# print(areaCirc(3))
15
# def contarVogais(texto):

#     contador = 0

#     for letra in texto.lower():

#         if letra in "aeiou":
#             contador += 1

#     return contador


# print(contarVogais("DANIEL"))
16
# def inverter(texto):

#     return texto[::-1]


# print(inverter("Python"))
# 17
# def ehPalindromo(texto):

#     texto = texto.lower()

#     if texto == texto[::-1]:
#         return True

#     return False


# print(ehPalindromo("Arara"))
# print(ehPalindromo("Python"))
# 18
# def somaArray(arr):

#     soma = 0

#     for numero in arr:

#         soma += numero

#     return soma


# numeros = [10, 20, 30]

# print(somaArray(numeros))
# 19
# def mediaArray(arr):

#     soma = 0

#     for numero in arr:

#         soma += numero

#     return soma / len(arr)


# numeros = [10, 20, 30]

# print(mediaArray(numeros))
20
# def maxArray(arr):

#     maior = arr[0]

#     for numero in arr:

#         if numero > maior:
#             maior = numero

#     return maior


# def minArray(arr):

#     menor = arr[0]

#     for numero in arr:

#         if numero < menor:
#             menor = numero

#     return menor


# numeros = [10, 50, 20, 5, 30]

# print("Maior:", maxArray(numeros))
# print("Menor:", minArray(numeros))
21
# def removerDuplicados(arr):

#     novo = []

#     for numero in arr:

#         if numero not in novo:
#             novo.append(numero)

#     return novo


# numeros = [1, 2, 2, 3, 1, 4]

# print(removerDuplicados(numeros))
# 22
# def frequencias(arr):

#     frequencia = {}

#     for numero in arr:

#         if numero in frequencia:
#             frequencia[numero] += 1
#         else:
#             frequencia[numero] = 1

#     return frequencia


# numeros = [2, 3, 2, 5, 3, 2]

# print(frequencias(numeros))
23
# def ordenarCresc(arr):

#     novo = arr.copy()

#     novo.sort()

#     return novo


# numeros = [8, 2, 5, 1, 9]

# print(ordenarCresc(numeros))
# 24
# def buscarLinear(arr, x):

#     for i in range(len(arr)):

#         if arr[i] == x:
#             return i

#     return -1


# numeros = [10, 20, 30, 40]

# print(buscarLinear(numeros, 30))
# print(buscarLinear(numeros, 50))
25
# def mdc(a, b):

#     while b != 0:

#         resto = a % b

#         a = b
#         b = resto

#     return a


# print(mdc(12, 8))
# 26
# def mdc(a, b):

#     while b != 0:

#         resto = a % b

#         a = b
#         b = resto

#     return a


# def mmc(a, b):

#     if a == 0 or b == 0:
#         return 0

#     return abs(a * b) // mdc(a, b)


# print(mmc(12, 8))
27
# def validarEmailSimples(email):

#     if "@" not in email:
#         return False

#     posicao_arroba = email.index("@")

#     if "." not in email[posicao_arroba:]:
#         return False

#     return True


# print(validarEmailSimples("teste@gmail.com"))
# print(validarEmailSimples("testegmail.com"))
28
def aplicarDesconto(valor, percentual):

    desconto = valor * percentual / 100

    valor_final = valor - desconto

    return valor_final


print(aplicarDesconto(100, 10))
29
def classificarNota(nota):

    if nota >= 7:

        return "Aprovado"

    elif nota >= 5:

        return "Recuperação"

    else:

        return "Reprovado"


print(classificarNota(8))
print(classificarNota(6))
print(classificarNota(3))
30
def resumoNumeros(arr):

    soma = 0
    maior = arr[0]
    menor = arr[0]

    for numero in arr:

        soma += numero

        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    media = soma / len(arr)

    resumo = {
        "soma": soma,
        "media": media,
        "max": maior,
        "min": menor,
        "contagem": len(arr)
    }

    return resumo


numeros = [10, 20, 5, 30, 15]

resultado = resumoNumeros(numeros)

print(resultado)


