class financeiro:
    def __init__(self,saldo, renda, gasto, entrada):
        self.saldo = saldo 
        self.renda = renda
        self.gasto = gasto
        self.entradas = entrada

    def status(self):
        if self.saldo  <= 0:
            print('Sem saldo disponível.') 
        elif self.saldo > 0: 
            print(f'Você possui um saldo de {self.saldo} em conta. ')  
    
    def gastos(self):
        print(f'O valor dos seus gastos atualmente está em {self.gasto}')