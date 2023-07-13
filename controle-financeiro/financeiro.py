from pessoa import Pessoa
class Financeiro:
    def __init__(self, gasto, entrada):
        self.gasto = gasto
        self.entrada = entrada

    def status(self):
        saldo = self.renda - self.gasto
        if saldo  <= 0:
            print('Sem saldo disponível.') 
        elif saldo > 0: 
            print(f'Você possui um saldo de {saldo} em conta. ')  
        return saldo
    
    def gastos(self):
        gasto = [ ]
        gasto.append(self.gasto)
        for n in gasto: 
            print(f'O valor dos seus gastos atualmente está em: {n}')
        return gasto

    def inf(self):
        return(f'Gastos: {self.gasto}\nEntrada:  {self.entrada}\n')

def dados_conta(gasto, entrada):
    status = []
    p1 = Financeiro(gasto, entrada)
    status.append(p1)

    return status

