from pessoa import Pessoa
caminho_arquivo = 'dados_clientes_financeiro.json'
import json
class Financeiro:
    def __init__(self, gasto, entrada, data):
        self.gasto = gasto
        self.entrada = entrada
        self.data = data

    def status(self):
        saldo = self.renda - self.gasto
        if saldo  <= 0:
            print('Sem saldo disponível.') 
        elif saldo > 0: 
            print(f'Você possui um saldo de {saldo} em conta. ')  
        return saldo
    
    '''def gastos(self):
        gasto = [ ]
        gasto.append(self.gasto)
        for n in gasto: 
            print(f'O valor dos seus gastos atualmente está em: {n}')
        return gasto'''

    def inf(self):
        return(f'Gastos: {self.gasto}\nData: {self.data}\nEntrada:  {self.entrada}\n')

    def salvar_inf(self):
        resultado = dados_conta(self.gasto, self.entrada, self.data)
        with open(caminho_arquivo, 'a') as arquivo:
            for pessoa in resultado:
                json.dump(vars(pessoa), arquivo, ensure_ascii= False, indent = 2)
def dados_conta(gasto, entrada, data):
    status = []
    p1 = Financeiro(gasto, entrada, data)
    status.append(p1)

    return status

