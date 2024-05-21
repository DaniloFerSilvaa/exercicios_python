## AULA06 :: TIPOS PRIMITIVOS E SAIDA DE DADOS :: NOTAS
"""
entrada = input('Digite algo: ')

islnum = entrada.isalnum()

print('o que você digitou é um lnum? : {}'.format(islnum))
print(entrada.isalpha())
print(entrada.isspace())
print(entrada.istitle())
print(entrada.isnumeric())
print(entrada.isupper())
print(entrada.islower())
print(entrada.isprintable())
"""

### AULA07 :: OPERADORES ARITIMETICAS :: NOTAS
"""
menu = ' MENU '
print('{:#^20}'.format(menu)) #APRENDENDO ':' DENTRO DA VARIAVEL USADO EM REAIS EX: '{:.2f}' PEGA APENAS 2 CASAS DECIMAIS
nome = input('Digite o nome: ')
print('{}'.format(nome))
"""


### EXERCICIOS AULA07

## 005. FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.

"""
valor = int(input('digite um numero inteiro: '))
antecessor = valor - 1
sucessor = valor + 1

print('O antecessor do numero digitado é: {} e o sucessor é: {}'.format(antecessor, sucessor))
"""

## 006.  CRIE UM ALGORITIMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.
"""
num = int(input('digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)

print('o dobro do numeoro digitado é: {}, o triplo é: {} e a raiz quadrada é: {:.2f}'.format(dobro, triplo, raiz_quadrada))
"""

## 007. DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA.
"""
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('Com a primeira nota sendo {:.1f} e a segunda nota sendo {:.1f}, a média do aluno é: {:.2f}'.format(nota1, nota2, media))
"""

## 008. ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS.
"""
valor_metros = float(input('digite o valor em metros para ser convertido em centimetros e em milimetros: '))
centimetro = valor_metros * 100
milimetro = valor_metros * 1000
print('Valor de {:.2f} metros são {} em centimetros e {} em milimetros'.format(valor_metros, centimetro, milimetro))
"""

## 009. FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA SUA TABUADA.
"""
num = int(input('digite um numero inteiro: '))
numx1 = (num * 1)
numx2 = (num * 2)
numx3 = (num * 3)
numx4 = (num * 4)
numx5 = (num * 5)
numx6 = (num * 6)
numx7 = (num * 7)
numx8 = (num * 8)
numx9 = (num * 9)
numx10 = (num * 10)
print('A taboada do numero é \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(numx1, numx2, numx3, numx4, numx5, numx6, numx7, numx8, numx9, numx10))
"""

## 010. CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR. CONSIDE US$1,00 = R$3,27
"""
dinheiro = float(input('digite o valor que você tem: '))
conversao = dinheiro / 3.27

print('você consegue comprar US${:.2f}'.format(conversao))
"""

## 011. FAÇA UM PROGRAMA QUE LEIA A LARGURA E A AUTURA DE UMA PAREDE EM METROS, 
# CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA, 
# SABENDO QUE CADA LITRO DE TINTA, PINTA UMA AREA DE 2m².
"""
largura = float(input('digite a largura em metros: '))
altura = float(input('digite a altura em metros: '))

area = (largura * altura)

litros_tinta = area / 2

print('É necessario {:.2f} litros de tinta'.format(litros_tinta))
"""

## 012. FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
"""
preco = float(input('digite o valor que deja aplicar o desconto de 5%: '))

preco_com_desconto = preco - (preco * 5 / 100)

print('O valor com desconto fica {:.2f} reais'.format(preco_com_desconto))
"""

## 013. FAÇA UM ALGORITIMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO, COM 15% DE AUMENTO.
"""
salario = float(input('Qual o valor do salario que deseja aumentar? '))

salario_atualizado = salario + (salario * 15 / 100)

print('Novo salario do funcionario é {:.2f}'.format(salario_atualizado))
"""

## 014. Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
"""
temperaturaC = float(input('Qual a temperatura em °C?: '))
temperaturaF = (temperaturaC * 9/5) + 32

print('A temperatura em celsius é: {:.1f}°C, convertida para fahrenheit é: {:.1f}°F'.format(temperaturaC, temperaturaF))
"""

## 015. Escreva um programa que pergunte a quantidade de Km percorridos por 
# um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
"""
kmPercorrido = float(input('Qual o km percorrido?: '))
diasAlugados = int(input('Quantos dias o carro ficou alugado?: '))

preco = (diasAlugados * 60) + (kmPercorrido * 0.15)

print('Sabendo que o carro percorreu {:.2f}Km e foram {} dias alugados o Total a pagar é R${:.2f}'.format(kmPercorrido, diasAlugados, preco))
"""

## 016. 



### CURIOSIDADES PROPRIAS

## ARREDONDAMENTO DO ULTIMO NUMERO DECIMAL, CASO >= 5 ARREDONDA PARA CIMA, CASO < 5 ARREDONDA PARA BAIXO
"""
num = 7.64

parte_decimal = str(num).split('.')[1]  # Obtemos a parte decimal como uma string
print(parte_decimal)
print(type(parte_decimal))
terceiro_digito_decimal = int(parte_decimal[1])  # Obtém o terceiro dígito decimal

if terceiro_digito_decimal >= 5:
    decimal = float((int(parte_decimal[0]) + 1)*0.10)
    num = int(num) + decimal
elif terceiro_digito_decimal < 5:
    decimal = float((int(parte_decimal) - terceiro_digito_decimal)*0.01)
    num = int(num) + decimal
print(num)
"""
