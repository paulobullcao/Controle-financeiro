from pessoa import  Pessoa
from financeiro import dados_conta, Financeiro
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
        escolha = int(input('Informe uma opção:\n1 - Cadastrar cliente \n2 - cadastar gastos e entradas\n3 - Listar informações da sua conta\n'))
        if escolha == 1:
            os.system('cls')
            nome = input('Informe o seu nome: ').strip()
            nascimento = input('Informe a data do seu nascimento: ').strip()
            profissao = input('Informe a sua profissão: ').strip()
            cpf = int(input('Informe o seu CPF: '))
            renda = float(input('Informe a sua renda: '))
            p = Pessoa(nome, nascimento, profissao, cpf, renda)
            p.salvar_cliente()
            os.system('cls')
        elif escolha == 2: 
            os.system('cls')
            gasto = float(input('Informe os seus gastos:  ')) 
            data = input('informe a data: ')
            print('Deseja inserir algum valor a sua conta?  ')
            escolha = input('S/sim ou N/não: ').startswith('s')
            if escolha == True: 
                entrada = float(input('informe o valor a ser creditado: '))
            else: 
                entrada = 0 
            f = Financeiro(gasto, entrada, data)
            f.salvar_inf()
            os.system('cls')
        elif escolha == 3:
            os.system('cls')
            leitura_dados() 
            print('')
            x  = input('pressione enter para continuar....')
            os.system('cls')
            continue
menu()

            
            