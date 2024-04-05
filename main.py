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


## EXERCICIOS AULA07

# 005. FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.

"""
valor = int(input('digite um numero inteiro: '))
antecessor = valor - 1
sucessor = valor + 1

print('O antecessor do numero digitado é: {} e o sucessor é: {}'.format(antecessor, sucessor))
"""

# 006.  CRIE UM ALGORITIMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.
"""
num = int(input('digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)

print('o dobro do numeoro digitado é: {}, o triplo é: {} e a raiz quadrada é: {:.2f}'.format(dobro, triplo, raiz_quadrada))
"""

# 007. DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA.
"""

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('Com a primeira nota sendo {:.1f} e a segunda nota sendo {:.1f}, a média do aluno é: {:.2f}'.format(nota1, nota2, media))
"""

# 008. ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS.

# 009. FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA SUA TABUADA.

# 010. CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR. CONSIDE US$1,00 = R$3,27

# 011. FAÇA UM PROGRAMA QUE LEIA A LARGURA E A AUTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA AREA DE 2m².

# 012. FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

# 013. FAÇA UM ALGORITIMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTR SEU NOVO SALARIO, COM 15% DE AUMENTO.


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