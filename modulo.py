def primeiraquest():

 nome = input("Digite seu nome: ")
 n1 = float(input("Digite sua nota: "))
 n2 = float(input("Digite sua nota: "))
 n3 = float(input("Digite sua nota: "))
 n4 = float(input("Digite sua nota: "))

 mediaarit = (n1+n2+n3+n4) / 4
 print(f"A Média Aritmética do Aluno(a): {nome} foi {mediaarit}")

def segundaquest():
 n1 = float(input("Digite um número: "))
 dobro = pow(n1, 2)
 triplo = pow(n1, 3)
 print(f"O dobro do número é: {dobro}")
 print(f"O triplo do número é: {triplo}")

def terceiraquest():
 salario = float(input("Digite seu salário inicial:"))
 salariofinal = salario * 0.25 + salario
 print(f"Este é o seu Salário Final: {salariofinal}")

def quartaquest():
 print("Informe os valores para analise abaixo")
 print("-+" * 20)
 n1 = int(input("Informe o Primeiro valor: "))
 n2 = int(input("Informe o Segundo valor: "))
 n3 = int(input("Informe o Terceiro valor: "))
 n4 = int(input("Informe o Quarto valor: "))
 n5 = int(input("Informe o Quinto valor: "))
 n6 = int(input("Informe o Sexto valor: "))
 n7 = int(input("Informe o Setimo valor: "))
 n8 = int(input("Informe o Oitavo valor: "))
 n9 = int(input("Informe o Nono valor: "))
 n10 = int(input("Informe o Décimo valor: "))

 lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
 media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10

 print(f"O maior número informardo foi: {max(lista)}")
 print(f"O menor número informardo foi: {min(lista)}")
 print(f"A média dos números informados é: {media}")

def quintaquest():
 print("Os impares são: ")
 for i in range(100, 300):
  if i % 2 == 1:
   print({i})

def sextaquest():
 numero = int(input("Informe o fatorial de: "))
 fatorial = 1
 contador = numero
 while contador >= 1:
  fatorial= fatorial * contador
  contador = contador - 1
  print(f"O fatorial de {numero} é = {fatorial}")
  print(f"{contador} x {numero}  = {fatorial} ")

def setimaquest():
 contador = 1
 maior = menor = igual = 0
 while contador <= 10:
  print(contador, "ª valor: ")
  valor = float(input())
  if valor < 0:
   menor += 1
  if valor > 0:
   maior += 1
  if valor == 0:
   igual += 1
   contador += 1
  print(f"Menor que zero: {menor}",f"Maior que zero: {maior}",f"Iguais a zero:{igual}")

def oitavaquest():
 listaA = []
 soma = 0
 for numero in range(0,10):
  listaA.append(int(input("Informe uma número: ")))

  soma += (listaA[len(listaA)- 1] ** 2)
  print(f"A soma dos quadrados dos elementos da lista é:{soma}")