from pessoa import Pessoa

def cadastro():
    cadastradas = []
    nome  = input('informe o seu nome:\n ')
    nascimento  = input('informe a data do seu nascimento:\n ')
    profissao = input('informe a sua profissao:\n ')
    cpf  = int(input('informe o seu CPF:\n '))
    renda  = float(input('informe a sua renda:\n '))
    p1 = Pessoa(nome, nascimento, profissao, cpf, renda)

    cadastradas.append(p1.get_nome)
    cadastradas.append(p1.get_nascimento)
    cadastradas.append(p1.get_cpf)
    cadastradas.append(p1.get_profissao)
    cadastradas.append(p1.get_renda)
    print(cadastradas)
    print(p1.inf())
    return cadastradas

cadastro()
