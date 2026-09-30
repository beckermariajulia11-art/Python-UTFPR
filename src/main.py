"""Sistema de cadastro de pessoas."""

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

def cadastrar_pessoa(nomes, idades, emails):
    """ Recebe os dados da pessoa e armazena nas listas """
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    nomes.append(nome)
    idades.append(idade)
    emails.append(email)
    print("Pessoa cadastrada!")
    print("Nome: " + nome)
    print("Idade: " + str(idade))
    print("E-mail: " + email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(nomes, idades, emails, pos):
    """ Recebe a posição da pessoa e exibe os dados armazenados nas listas """
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def buscar_pessoa(nomes, buscar_nome):
    """ Recebe o nome a ser buscado e retorna a posição da pessoa na lista """
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == buscar_nome:
            return pos
        pos += 1
    return -1

def consultar_pessoa(nomes, idades, emails):
    """ Recebe o nome a ser consultado e exibe os dados da pessoa """
    buscar = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, buscar)
    if pos != -1:
        exibir_pessoa(nomes, idades, emails, pos)
    else:
        print("Nao encontrado")

def alterar_pessoa(nomes, idades, emails):
    """ Recebe o nome a ser alterado e solicita os novos dados da pessoa """
    b = input("Nome para alterar: ")
    buscar = buscar_pessoa(nomes, b)
    if buscar != -1:
        print("Dados atuais:")
        exibir_pessoa(nomes, idades, emails, buscar)
        nomes[buscar] = input("Novo nome: ")
        idades[buscar] = int(input("Nova idade: "))
        emails[buscar] = input("Novo e-mail: ")
        print("Alterado!")
    else:
        print("Nao encontrado")

def listar_pessoas(nomes, idades, emails):
    """ Exibe os dados de todas as pessoas cadastradas """
    pos = 0
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")

    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        pos += 1

def classificar_faixa_etaria(idade):
    """ Classifica a faixa etária da pessoa com base na idade """
    if idade < 12:
        return "Crianca"
    if idade < 18:
        return "Adolescente"
    if idade < 30:
        return "Adulto jovem"
    if idade < 60:
        return "Adulto"
    return "Idoso"

def analisar_email(email):
    """ Analisa se o e-mail é válido com base na presença de "@" e "." ou se está ausente """
    if email == "":
        return "E-mail ausente"
    if "@" not in email or "." not in email:
        return "E-mail invalido"
    return "OK"

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

def analisar_pessoa(nomes, idades, emails):
    """ Recebe o nome da pessoa a ser analisada e exibe seus dados """
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Pessoa não encontrada")
        return

    idade = idades[pos]
    email = emails[pos]

    print(f"Faixa etaria: {classificar_faixa_etaria(idade)}")

    status_email = analisar_email(email)
    if status_email != "OK":
        print(status_email)
    else:
        provedor = obter_provedor_email(email)
        print(f"Provedor: {provedor}")

    condicao_contato = definir_condicao_contato(idade, email)
    print(f"Condicao de contato: {condicao_contato}")

lista_nomes = []
lista_idades = []
lista_emails = []

opcao = 0

while opcao != 6:

    opcao = exibir_menu()

    if opcao == 1:
        cadastrar_pessoa(lista_nomes, lista_idades, lista_emails)

    elif opcao == 2:
        consultar_pessoa(lista_nomes, lista_idades, lista_emails)

    elif opcao == 3:
        alterar_pessoa(lista_nomes, lista_idades, lista_emails)

    elif opcao == 4:
        listar_pessoas(lista_nomes, lista_idades, lista_emails)

    elif opcao == 5:
        analisar_pessoa(lista_nomes, lista_idades, lista_emails)

    elif opcao == 6:
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")
