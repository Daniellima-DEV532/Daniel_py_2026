1
#valor = float(input("Digite o valor: "))
#cliente = input("Digite o tipo de cliente (COMUM/PREMIUM): ").upper()

#desconto = 0

#if cliente == 'PREMIUM':
 #   desconto += valor * 0.08

#else:
 #   desconto += valor * 0.03

#if valor >= 300:
 #   desconto += valor * 0.05

#valor_final = valor - desconto

#print("Valor final:", valor_final)
#print("Desconto aplicado:", desconto)
#print("Valor original:", valor)
2
#valor = float(input("Digite o valor: "))
#pagamento = input("Digite a forma de pagamento (DINHEIRO/CARTÃO/PIX): ").upper()

#desconto = 0

#if pagamento == 'DINHEIRO':
 #   desconto += valor * 0.03
#elif pagamento == 'PIX':
 #   desconto += valor * 0.05

#else:
 #   desconto == 0

#valor_final = valor - desconto

#print("Valor final:", valor_final)
#print("Desconto aplicado:", desconto)
#print("Valor original:", valor)
3
#media = float(input("Digite a média: "))
#faltas = int(input("Digite o número de faltas: "))
#aulas = int(input("Digite o número total de aulas: "))

#percentual_faltas = (faltas / aulas) * 100

#if media >= 7 and percentual_faltas <= 25:
#    situacao = "Aprovado"
#else:
 #   situacao = "Reprovado"

#print("precentual de faltas:", percentual_faltas)
#print("Situação:", situacao)
4
#salario = float(input("Digite o salário: "))
#nota = int(input("Digite a nota (1 a 5): "))

#if nota == 5:
#    aumento = salario * 0.10
#elif nota == 4:
 #   aumento = salario * 0.07
#elif nota == 3:
 #   aumento = salario * 0.05
#else:
 #   aumento = 0

#novo_salario = salario + salario * aumento

#print("Novo salário:", novo_salario)
#print('salario antigo:', salario)
5
#saldo = float(input("Digite o saldo: "))
#saque = float(input("Digite o valor do saque: "))

#if saque >= saldo:
  #  saldo -= saque
  #  print("Saque realizado com sucesso.")
 #   print("Saldo atual:", saldo)

#else:
  #  print("Saldo insuficiente.")
  #  print('Faltam:', saque - saldo)
6
#distancia = float(input("Distância: "))
#tipo = input("Tipo (MOTO/CARRO/VAN): ").upper()

#if tipo == "MOTO":
 #   tarifa = 1.5

#elif tipo == "CARRO":
 #   tarifa = 2.5

#else:
 #   tarifa = 3.5

#total = distancia * tarifa

#if distancia > 20:
 #   total *= 0.90

#print("Valor final:", total)
7
#peso = float(input("digite o peso: "))
#valor = float(input("digite o valor: "))
 
#if valor >= 200
#    frete = 0
#elif peso <= 1;
#    frete = 10
#elif peso <= 5:
#    frete = 20
#else:
#    frete = 35
 
#print("Valor do frete:", frete)
#print("Valor total:", valor + frete)
8
#idade = int(input("Digite a idade: "))
#prioridade = int(input("prioridade: "))

#if prioridade >= 4 or idade >= 65:
   # print("Atendimento prioritário")
#else:
 #   print("Atendimento normal") 
9
#idade = int(input("Digite a idade: "))
#estudante = input("É estudante? (S/N): ").upper()
#dia = input("Dia da semana: ").lower()

#if dia == 'segunda-feira' and idade < 12:
 #   print("Entrada gratuita")
#elif estudante == 's':
 #   print('MEIA')
#else:
 #   print('INTEIRA')
10
#horas = int(input("Horas: "))
#eletrico = input("É elétrico (S/N): ").upper()

#if horas <= 2:
 #   valor = 8

#elif horas <= 5:
 #   valor = 15

#else:
#    valor = 25

#if eletrico == "S":
#    valor *= 0.80

#print("Valor:", valor)
11
#noites = int(input("Digite o número de noites: "))
#categoria = input("Categoria (STANDARD/LUXO): ").upper()

#if categoria == "STANDARD":
#    diaria = 150
#else:
#    diaria = 280

#total = noites * diaria

#if noites >= 5:
#    total *= 0.88

#print("Valor final:", total)
12
#consumo = float(input("Consumo (GB): "))
#fidelidade = input("Possui fidelidade? (S/N): ").upper()

#if consumo <= 5:
#    valor = 50

#elif consumo <= 15:
#    valor = 80

#else:
 #   valor = 120

#if fidelidade == "S":
#    valor *= 0.95

#print("Valor:", valor)
13
#consumo = int(input("Consumo em kWh: "))

#if consumo <= 100:
 #   faixa1 = consumo * 0.60
  #  faixa2 = 0
   # faixa3 = 0

#elif consumo <= 300:
 #   faixa1 = 100 * 0.60
  #  faixa2 = (consumo - 100) * 0.75
   # faixa3 = 0

#else:
 #   faixa1 = 100 * 0.60
  #  faixa2 = 200 * 0.75
   # faixa3 = (consumo - 300) * 0.90

#total = faixa1 + faixa2 + faixa3

#print("Faixa 1:", faixa1)
#print("Faixa 2:", faixa2)
#print("Faixa 3:", faixa3)
#print("Total:", total)
14
#consumo = int(input("Consumo em m³: "))

#total = 30

#if consumo > 10 and consumo <= 20:
 #   total += (consumo - 10) * 3

#elif consumo > 20:
 #   total += 10 * 3
  #  total += (consumo - 20) * 5

#print("Conta:", total)
15
#dias = int(input("Dias de atraso: "))
#olsista = input("É bolsista? (S/N): ").upper()

#if dias <= 7:
 #   multa = dias

#else:
#    multa = 7 + (dias - 7) * 2

#if bolsista == "S":
 #   multa *= 0.50

#print("Multa:", multa)
16
#plano = input("Plano: ").upper()
#aluno = input("É aluno? (S/N): ").upper()

#if plano == "MENSAL":
 #   valor = 120

#elif plano == "TRIMESTRAL":
#    valor = 320

#else:
 #   valor = 1100

#if aluno == "S":
 #   valor *= 0.90

#  print("Valor final:", valor)
17
#fatura = float(input("Valor da fatura: "))
#dias = int(input("Dias de atraso: "))

#juros = 0

#if dias > 0:
 #   juros = fatura * 0.003 * dias

#total = fatura + juros

#print("Juros:", juros)
#print("Total:", total)
18
#idade = int(input("Idade: "))
#veiculo = float(input("Valor do veículo: "))

#if idade < 25:
 #   taxa = 0.06

#else:
 #   taxa = 0.04

#if veiculo > 100000:
 #   taxa += 0.01

#seguro = veiculo * taxa

#print("Valor do seguro:", seguro)
19
#avaliacao = float(input("Avaliação: "))
#venda = float(input("Valor da venda: "))

#if avaliacao < 3:
 #   taxa = 0.15

#elif avaliacao < 4.5:
#    taxa = 0.10

#else:
 #   taxa = 0.07

#valor_taxa = venda * taxa
#liquido = venda - valor_taxa

#print("Taxa:", valor_taxa)
#print("Valor líquido:", liquido)
20
#tipo= input("Tipo (INTEIRA/MEIA): ").upper()
#lote = int(input("Lote: "))

#if lote <= 100:
 #   preco = 80
#elif lote <= 2:
 #   preco = 100
#else:
 #   preco = 120

#if tipo == "MEIA":
 #   preco /=2

#print('preço final:', preco)
21
#bairro = input("Digite o bairro (A/B/C): ").upper()
#pedido = float(input("Digite o valor do pedido: "))

#if  pedido >= 80:
#    frete = 0
#elif bairro == "A":
 #   frete = 5
#elif bairro == "B":
#    frete = 8
#else:
 #   frete = 12

#total = pedido + frete

#print("Valor do frete:", frete)
#print("Valor total:", total)
22
#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#trabalho = float(input("Digite a nota do trabalho: "))

#if trabalho >= 0:
 #   print('Reprovado')
#else:
    #media = (nota1 + nota2 + trabalho) / 3

   # if media >= 7:
    #    print('Aprovado')
   # elif media >= 5:
  #      print('Recuperação')
 #   else:
 #       print('Reprovado')
#23
#valor = float(input("Valor da consulta: "))
#tipo = input("Tipo (NORMAL/URGENCIA): ").upper()
#convenio = input("Possui convênio? (S/N): ").upper()

#if tipo == "URGENCIA":
 #   valor *= 1.30

#if convenio == "N":
 #   valor *= 1.50

#print("Valor final:", valor)
24
#preco = float(input("Preço: "))
#peca = input("Peça: ").upper()

#if peca == "CAMISA":
 #   imposto = preco * 0.08

#elif peca == "CALCA":
 #   imposto = preco * 0.12

#else:
 #   imposto = preco * 0.18

#print("Imposto:", imposto)
#print("Preço final:", preco + imposto)
25
#feitas = int(input("Horas realizadas: "))
#minimas = int(input("Horas mínimas: "))

#if feitas >= minimas:
 #   print("APTO")

#else:
  #  print("INAPTO")
  #  print("Faltam", minimas - feitas, "horas.")
26
#nome1 = input("Nome do candidato A: ")
#nota1 = float(input("Nota A: "))
#idade1 = int(input("Idade A: "))

#nome2 = input("Nome do candidato B: ")
#nota2 = float(input("Nota B: "))
#idade2 = int(input("Idade B: "))

#if nota1 > nota2:
 #   print("Vencedor:", nome1)

#elif nota2 > nota1:
 #   print("Vencedor:", nome2)

#else:
 #   if idade1 > idade2:
 #       print("Vencedor:", nome1)
 #   else:
#        print("Vencedor:", nome2)
27
#viagens = int(input("Número de viagens: "))
#valor = float(input("Valor da passagem: "))

#total = viagens * valor

#if viagens > 40:
 #   total *= 0.80
     
#print("Valor total:", total)
28
lista = input("Está na lista? (S/N): ").upper()
idade = int(input("Idade: "))

if lista == "S" and idade >= 21:
    print("ENTRADA LIBERADA")

else:
    print("ENTRADA NEGADA")
29
compra = float(input("Valor da compra: "))
pago = float(input("Valor pago: "))

if pago >= compra:
    print("Troco:", pago - compra)

else:
    print("Faltam:", compra - pago)
30
renda = float(input("Renda: "))
gastos = float(input("Gastos: "))

if gastos > renda:
    print("DÉFICIT")
    print("Valor:", gastos - renda)

else:
    print("SUPERÁVIT")
    print("Valor:", renda - gastos)