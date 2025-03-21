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

         