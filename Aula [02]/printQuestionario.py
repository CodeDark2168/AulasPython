from multiprocessing.connection import wait


print("==============================")
print("Questionario")
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
cidade = input("Informe sua cidade: ")
print("==============================")
print("Processando dados...")
import time
time.sleep(3)
print("==============================")
print("Nome: " + nome)
print("Idade: " + idade)
print("Cidade: " + cidade)
print("==============================")