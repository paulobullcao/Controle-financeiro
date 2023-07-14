import json
caminho_arquivo = 'dados_clientes.json'
class Pessoa: 
    def __init__(self, nome, nascimento, profissao,cpf, renda):
        self.nome = nome  
        self.nascimento = nascimento  
        self.profissao= profissao  
        self.cpf = cpf  
        self.renda = renda  

    ''' Métodos para obter e setar valores'''
    def get_cpf(self):
        return self.cpf

    def set_cpf(self, valor):
        self.cpf = valor

    def get_nome(self):
        return self.nome

    def set_nome(self, valor):
        self.nome = valor

    def get_nascimento(self):
        return self.nascimento

    def set_nascimento(self, valor):
        self.nascimento = valor

    def get_profissao(self):
        return self.profissao

    def set_profissao(self, valor):
        self.profissao =  valor

    def get_renda(self):
        return self.renda

    def set_renda(self, valor):
        self.renda = valor

    def inf(self):
        return(f'nome: {self.nome}\nData de nascimento: {self.nascimento}\nProfissão: {self.profissao}\nCPF: {self.cpf}\nRenda: {self.renda}')
    def salvar_cliente(self):
        resultado = cadastro(self.nome,self.nascimento,self.profissao,self.cpf,self.renda)
        for pessoa in resultado:
            print(pessoa.inf())
            x = ('pressione enter...')
        with open(caminho_arquivo, 'a') as arquivo:
            for pessoa in resultado:
                json.dump(vars(pessoa), arquivo, ensure_ascii= False, indent = 2)

def cadastro(nome, nascimento,profissao, cpf, renda):
    cadastradas = []
    p = Pessoa(nome, nascimento, profissao, cpf, renda)
    cadastradas.append(p)
    return cadastradas
