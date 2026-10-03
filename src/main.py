"""Sistema de cadastro de pessoas."""

from cadastro import CadastroPessoas

def exibir_menu():
    """ Função para exibir o menu de opções """
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar pessoas")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrar_pessoa(cadastro_pessoas):
    """ Recebe os dados da pessoa e armazena nas listas """
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")

    cadastro_pessoas.cadastrar(nome, idade, email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(pessoa):
    """ Recebe a posição da pessoa e exibe os dados armazenados nas listas """
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    if pessoa.getIdade() >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

# def buscar_pessoa(nomes, buscar_nome):
#     """ Recebe o nome a ser buscado e retorna a posição da pessoa na lista """
#     pos = 0
#     while pos < len(nomes):
#         if nomes[pos] == buscar_nome:
#             return pos
#         pos += 1
#     return -1

def consultar_pessoa(cadastro_pessoas):
    """ Recebe o nome a ser consultado e exibe os dados da pessoa """
    buscar = input("Nome para consultar: ")
    pessoa = cadastro_pessoas.buscarPorNome(buscar)
    if pessoa is None:
        print("Nao encontrado")
    else:
        exibir_pessoa(pessoa)

def alterar_pessoa(cadastro_pessoas):
    """ Recebe o nome a ser alterado e solicita os novos dados da pessoa """
    buscar = input("Nome para alterar: ")
    pessoa = cadastro_pessoas.buscarPorNome(buscar)
    if pessoa is None:
        print("Nao encontrado")
    else:
        print("Dados atuais:")
        exibir_pessoa(pessoa)
        novo_nome = input("Novo nome: ")
        nova_idade = int(input("Nova idade: "))
        novo_email = input("Novo e-mail: ")
        cadastro_pessoas.alterar(buscar, novo_nome, nova_idade, novo_email)
        print("Alterado!")
        exibir_pessoa(pessoa)

def listar_pessoas(cadastro_pessoas):
    """ Exibe os dados de todas as pessoas cadastradas """
    pessoas = cadastro_pessoas.listar()
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
    else:
        for pessoa in pessoas:
            exibir_pessoa(pessoa)
            print("--------------------")
        print("Total de pessoas cadastradas: " + str(len(pessoas)))

def classificar_faixa_etaria(idade):
    """ Classifica a faixa etária da pessoa com base na idade """
    if idade < 12:
        print("Faixa etaria: Crianca")
    if idade < 18:
        print("Faixa etaria: Adolescente")
    if idade < 30:
        print("Faixa etaria: Adulto jovem")
    if idade < 60:
        print("Faixa etaria: Adulto")
    return "Idoso"

def analisar_email(email):
    """ Analisa se o e-mail é válido com base na presença de "@" e "." ou se está ausente """
    if email == "":
        print("E-mail ausente")
    if "@" not in email or "." not in email:
        print("E-mail invalido")
    else:
        print("E-mail valido")
        provedor = obter_provedor_email(email)
        print("Provedor de e-mail: " + provedor)

def obter_provedor_email(email):
    """ Identifica o provedor do e-mail com base no domínio """
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    if email.endswith("@hotmail.com"):
        return "Hotmail"
    if email.endswith("@utfpr.edu.br"):
        return "UTFPR"
    return "Outro"

def definir_condicao_contato(idade, email):
    """ Define a condição de contato com base na idade e na presença de e-mail """
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    if idade >= 18 and email == "":
        return "Maior de idade sem contato"
    if idade < 18 and email != "":
        return "Menor de idade com contato"
    return "Menor de idade sem contato"

def analisar_pessoa(cadastro_pessoas):
    """ Recebe o nome da pessoa a ser analisada e exibe seus dados """
    buscar = input("Nome para analisar: ")
    pessoa = cadastro_pessoas.buscarPorNome(buscar)

    if pessoa is None:
        print("Nao encontrado")
    else:
        classificar_faixa_etaria(pessoa.getIdade())
        analisar_email(pessoa.getEmail())
        definir_condicao_contato(pessoa.getIdade(), pessoa.getEmail())

def executar():
    """ Função principal para executar o sistema de cadastro de pessoas """
    cadastro = CadastroPessoas()
    opcao = 0

    while opcao != 6:

        opcao = exibir_menu()

        if opcao == 1:
            cadastrar_pessoa(cadastro)

        elif opcao == 2:
            consultar_pessoa(cadastro)

        elif opcao == 3:
            alterar_pessoa(cadastro)

        elif opcao == 4:
            listar_pessoas(cadastro)

        elif opcao == 5:
            analisar_pessoa(cadastro)

        elif opcao == 6:
            print("Saindo...")

        else:
            print("Opcao invalida")
    print("Fim do programa")

if __name__ == "__main__":
    executar()
