from pessoa import  Pessoa
from financeiro import  Financeiro
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
        try: 
            escolha = int(input('Informe uma opção:\n1 - Cadastrar cliente \n2 - cadastar gastos e entradas\n3 - Listar informações da sua conta\n'))
        except:
            os.system('cls')
            print( 'Escolha uma das opções listadas')
            menu()
        if escolha == 1:
            try: 
                os.system('cls')
                nome = input('Informe o seu nome: ').strip()
                nascimento = input('Informe a data do seu nascimento: ').strip()
                profissao = input('Informe a sua profissão: ').strip()
                cpf = input('Informe o seu CPF: ')
                if len(cpf) != 11:
                    while True:
                        os.system('cls')
                        print('O CPF informado é inválido!\nInforme corretamente o seu CPF') 
                        cpf = input('Informe o seu CPF: ')
                        os.system('cls')
                        if len(cpf) == 11: 
                            break
                renda = float(input('Informe a sua renda: '))
                p = Pessoa(nome, nascimento, profissao, int(cpf), renda)
                p.salvar_cliente()
                os.system('cls')
            except:
                print('o cliente não pode ser cadastrado!')
                continue
        elif escolha == 2: 
            try: 
                os.system('cls')
                gasto = float(input('Informe os seus gastos:  ')) 
                data = input('informe a data: ')
                os.system('cls')
                print('Deseja inserir algum valor a sua conta?  ')
                escolha = input('S/sim ou N/não: ').startswith('s')
                if escolha == True: 
                    entrada = float(input('informe o valor a ser creditado: '))
                else: 
                    entrada = 0 
                f = Financeiro(gasto, entrada, data)
                f.salvar_inf()
                os.system('cls')
            except:
                print('seus gastos não  podem  ser cadastrado!')
                continue
        elif escolha == 3:
            os.system('cls')
            leitura_dados() 
            print('')
            x  = input('pressione enter para continuar....')
            os.system('cls')

            continue
menu()

            
            