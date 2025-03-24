#Exercício 1


x = float(input("Digite uma nota de 0 a 10: "))
if x >= 9:
    print("Excelente")
elif x >= 7:
    print("Bom")
elif x >= 5:
    print("Regular")
else:
    print("Reprovado")

               
#Exercício 2


x = int(input("digite um número inteiro: "))
if x % 2 == 0:
    print(f"{x} é par")
else:
    print(f"{x} é ímpar")


#Exercício 3


peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")    


#Exercício 4

print("Escolha três números aleatórios.")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é maior que {numero2} e {numero3}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} é maior que {numero1} e {numero3}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} é maior que {numero1} e {numero2}")
elif numero1 < numero2 and numero1 < numero3:
    print(f"{numero1} é menor que {numero2} e {numero3}")
elif numero2 < numero1 and numero2 < numero3:
    print(f"{numero2} é menor que {numero1} e {numero3}")
elif numero3 < numero1 and numero3 < numero2:     
    print(f"{numero3} é menor que {numero1} e {numero2}")   
 


    #Exercício 5


print("Digite a nota de três provas, tendo, assim, o resultado de sua média.")
numero1 = float(input("Primeira nota: "))
numero2 = float(input("Segunda nota: "))
numero3 = float(input("Terceira nota: "))
soma = numero1 + numero2 + numero3
media = soma /3
print("A média de suas notas é", media)


# Solicita a entrada dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
# Calcula a soma e a média
soma = numero1 + numero2
media = soma / 2
# Exibe o resultado
print("A média é:", media)


#Tipos de dados

num_inteiro = 10
num_real = 3.14
texto = "Python"
logico = True
print(type(num_inteiro)) # int
print(type(num_real)) # float
print(type(texto)) # str
print(type(logico)) # bool

print(bool(0))
print(bool(1))


#Operadores aritmeticos

a = 10
b = 3
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333
print(a // b) # 3
print(a % b) # 1
print(a ** b) # 1000


#Operadores de atribuição

x = 10
x += 5 # x = x + 5 -> 15
x *= 2 # x = x * 2 -> 30
x //= 3 # x = x // 3 -> 10
print(x) # 10


#Casting

num1 = "10"
num2 = float("3.5")
print(int(num1) + 5) # 15
print(num2 + 1.5) # 5.0
print(int(num2) + 3.5) # 6.5
print(str(100) + " reais") # "100 reais"
print(bool(0)) # False




valor = "150.34"
novo_valor = float(valor) # Complete aqui
print(type(novo_valor)) 

print("Digite três notas.")
numero1 = float(input("Primeira nota: "))
numero2 = float(input("Segunda nota: "))
numero3 = float(input("Terceira nota: "))
soma = numero1 + numero2 + numero3
media = soma / 3
print("A média das suas três notas é: ", media)
if media >= 7: 
    print("Sua média é maior que 7.")
else: 
    print("Sua média não é maior que 7.")


valor = float(input("Digite um valor: "))
desconto = valor * 0.10
valor_com_desconto = valor - desconto 
print("Valor com desconto: " , valor_com_desconto)



#Coisas aleatórias pra ver se eu entendi mesmo

idade = int(input("Qual sua idade?: "))
print(f'Você tem {idade} anos.')

nome = str(input('Qual seu nome?: '))
print(f'Seu nome é {nome}')


#nasjaksj

obsessao = str(input(f'Qual sua maior obsessão?: '))
print(f"Sua maior obsessão é {obsessao}. A minha também!")


#Exercício 7

operacao = input("Digite uma operação básica da matemática (+,-,*,/): ")
match operacao:
    case "+":
         numero1 = float(input("Escolha o primeiro número: "))
         numero2 = float(input("Escolha o segundo número: "))
         soma = numero1 + numero2
         print("Você escolheu a soma. A soma de {} + {} é {}".format(numero1, numero2, soma))
    case "-":
         numero1 = float(input("Escolha o primeiro número: "))
         numero2 = float(input("Escolha o segundo número: "))
         subtracao = numero1 - numero2
         print("Você escolheu a subtração. A subtração de {} - {} é {}".format(numero1, numero2, subtracao))
    case "*":
         numero1 = float(input("Escolha o primeiro número: "))
         numero2 = float(input("Escolha o segundo número: "))
         multiplicacao = numero1 * numero2  
         print("Você escolheu a multiplicação. A multiplicação de {} * {} é {}".format(numero1, numero2, multiplicacao))
    case "/":
         numero1 = float(input("Escolha o primeiro número: "))
         numero2 = float(input("Escolha o segundo número: "))
         divisao = numero1 / numero2 
         print("Você escolheu a divisão. A divisão de {} / {} é {}".format(numero1, numero2, divisao))
    case _:
        print("Operação não reconhecida.")


        bichinho = str(input("Qual o nome do seu bichinho de estimação?: "))
print(f"Seu bichinho de estimação se chama {bichinho}.")

ariana = str(input("Qual o nome do seu cantor(a) favorito?: "))
print(f"Seu cantor(a) favorito(a) se chama {ariana} ")

idade = int(input("Quantos anos você tem?: "))
print(f"Você tem {idade} anos.")

melhores_amigas = str(input('Qual o nome das suas melhores amigas?: '))
print(f"O nome das suas melhores amigas é: {melhores_amigas}.")


nome = str(input("Qual seu nome?: "))
idade = int(input("Qual sua idade?: "))
print('Seu nome é {} e você tem {} anos.'.format(nome, idade))

personagem = str(input("Qual seu personagem favorito?: "))
ship = str(input('Qual seu ship favorito dessa série?: '))
numero = int(input('Quantas vezes você já assistiu essa série?: '))
print('Você ama {}, seu ship favorito é {} e você assistiu a série {} vezes.'.format(personagem, ship, numero))



ingresso = float(input("Quanto você pagaria em um ingresso para show?: "))
print("Você pagaria {} em um ingresso para show".format(ingresso))
print(f"O preço formatado é: {ingresso:.1f}.")


nome = "Python"
print(f"{nome:<10}")
print(f"{nome:^10}")
print(f"{nome:>10}")


# 3) Números formatados com tamanho 5
numeros = [10, 1, 333, 4500]
for num in numeros:
 print(f'{num:5,.0f}'.replace(',', '.'))
# 4) Números float formatados com duas casas
num1 = 3.14
num2 = 5.678
num3 = 8.9
print(f'{num1:5.2f}'.replace('.', ',’)) # 3,14'))
print(f'{num2:5.2f}'.replace('.', ',’)) # 5,68'))
print(f'{num3:5.2f}'.replace('.', ',’)) # 8,90'))


numero_decimal = float(input("Digite um número decimal: "))
print(f'O número decimal que você escolheu formatado é: {numero_decimal:.2f}')

nome = str(input('Qual seu nome?: '))
idade = int(input('Qual a sua idade?: '))
print('Seu nome é {} e sua idade é {}'.format(nome, idade))

texto = str(input("Digite um texto de até 20 caracteres: "))
print(f'Seu texto formatado é: {texto:^20}')


a = 11
b = 3
print(a + b * a)
print(b * a + b)
print(a // b)
print(b % a)
print(a % b)
print(b // a)
print(b - a / b)
print(a / b - a * b)
print(10 + a % b)
print(10 - b // a)
print(b // a - 50)
print(a + b % a - a // b * 2)
print(a * (b+a) - (a-b) / 2)


x = True
y = False

print(x and y)
print(x or y)
print(x and y or x)
print(not(x or not y))


a = 5
b = 9
x = not True
y = False and True
m = "Casa"
n = "Mesa"

print(x and y == x or y)
print(a * b <= b - a)
print(not(a == b or not b != a))
print(not(m != n and b>a))
print(b + a <= a * b and y)
print(x and not y or a // b != a % b)