from pessoa import  Pessoa, cadastro
from financeiro import dados_conta
import json
caminho_arquivo = 'dados_clientes.json'
import os

'''Classe que faz a leitura do arquivo json para trazer as informações dos clientes'''
def leitura_dados():
    leitura = []
    print('Informações cadastradas:\n')
    with open(caminho_arquivo, 'r') as arquivo:
        pessoas= json.load(arquivo)
        p = Pessoa(**pessoas)
        leitura.append(p)
        print(p.inf())
    return 

def menu():
    while True:
        escolha = int(input('Informe uma opção:\n1 - Cadastrar\n2 - Listar informações do seu cadastro\n3 - exibir seus gastos \n'))
        if escolha == 1:
            os.system('cls')
            nome = input('Informe o seu nome: ').strip()
            nascimento = input('Informe a data do seu nascimento: ').strip()
            profissao = input('Informe a sua profissão: ').strip()
            cpf = int(input('Informe o seu CPF: '))
            renda = float(input('Informe a sua renda: '))
            os.system('cls')
            cadastro(nome, nascimento,profissao, cpf, renda)
            resultado = cadastro(nome, nascimento,profissao, cpf, renda)
            for pessoa in resultado:
                print(pessoa.inf())
                x = ('pressione enter...')
            with open(caminho_arquivo, 'a') as arquivo:
                for pessoa in resultado:
                    json.dump(vars(pessoa), arquivo, ensure_ascii= False, indent = 2)
        elif escolha == 2: 
            os.system('cls')
            gasto = float(input('Informe os seus gastos:  ')) 
            print('Deseja inserir algum valor a sua conta?  ')
            escolha = input('S/sim ou N/não: ').startswith('s')
            if escolha == True:
                os.system('cls')
                entrada = float(input('Informe o valor a ser creditado na sua conta: '))
            else: 
                entrada = 0 
            dados_conta(gasto, entrada)
            resultado = dados_conta(gasto, entrada)
            for status in resultado:
                os.system('cls')
                print(status.inf())
        elif escolha == 3:
            os.system('cls')
            leitura_dados() 
            print('')
            x  = input('pressione enter para continuar....')
            os.system('cls')
            menu()
menu()

            
            