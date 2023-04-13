#Exercício 02 - Fibonacci

#Input do número  inteiro e  criação da lista
num = int(input("Insira um número inteiro: "))
fibonacci = [0, 1]

#Enquanto a variável Fibonacci[-1] for menor que a variável num
while fibonacci[-1] < num:
#Realiza a adição do valor baseado na variavel e o indice dentro dela (-1 e -2)
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

#Se a variável num estiver em fibonacci, será exibido um print de o número pertence ou não à sequência.
if num in fibonacci:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")