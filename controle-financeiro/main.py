from pessoa import Pessoa, cadastro

caminho_arquivo = 'dados_clientes.txt'
while True:
    escolha = int(input('Informe uma opção:\n1 - Cadastrar\n2 - Listar informações do seu cadastro\n3 -exibir seus gastos '))
    if escolha == 1:
        nome = input('Informe o seu nome: ').strip()
        nascimento = input('Informe a data do seu nascimento: ').strip()
        profissao = input('Informe a sua profissão: ').strip()
        cpf = int(input('Informe o seu CPF: '))
        renda = float(input('Informe a sua renda: '))
        cadastro(nome, nascimento,profissao, cpf, renda)
        resultado = cadastro(nome, nascimento,profissao, cpf, renda)
        for pessoa in resultado:
            print(pessoa.inf())
        with open(caminho_arquivo, 'a') as arquivo:
            for pessoa in resultado:
                arquivo.write(pessoa.inf() + '\n')
            arquivo.write(' ') 