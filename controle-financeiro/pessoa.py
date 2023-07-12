class Pessoa: 
    def __init__(self, nome, nascimento, profissao,cpf, renda):
        self.nome = nome  
        self.nascimento = nascimento  
        self.profissao= profissao  
        self.cpf = cpf  
        self.renda = renda  


    def inf(self):

        return(f'nome: {self.nome}\nData de nascimento: {self.nascimento}\nProfissão: {self.profissao}\nCPF: {self.cpf}Renda: {self.renda}')

#pessoa teste
p1 = Pessoa('carlos sergio','1987-05-21','auxiliar de motorista','04852845530','1.450')

print(p1.inf())