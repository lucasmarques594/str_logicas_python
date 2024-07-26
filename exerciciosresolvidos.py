'1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.'
print('-------------------')
print(('Exercicio 1'))
numero1: int = int(input("Informe seu primeiro numero: "))
numero2: int = int(input("Informe seu segundo numero: "))

if numero1 > numero2:
    print(f'Seu primeiro numero e maior que o segundo')
elif numero1 == numero2:
    print(f'Os numeros sao iguais :)')
else: 
    print(f'Seu segundo numero e maior que o primeiro')

'2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule'
'a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.'
print('-------------------')
print(('Exercicio 2'))

numb1: int = int(input('Informe um número: '))

if numb1 >0 :
    raiznumb = numb1 * numb1
    print(f'A raiz quadrada do número selecionada é {raiznumb}')
elif numb1 == 0:
    print('0 é neutro :/')
else:
    print('O numero é negativo')


print('-------------------')
print(('Exercicio 3'))
'3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.'


number1: int = int(input('Informe um número: '))

if number1 % 2 == 0:
    print(f'o número{number1} é par')
else: 
    print(f'o número {number1} é impar')