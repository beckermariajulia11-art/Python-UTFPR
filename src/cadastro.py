"""Gerenciamento do cadastro de pessoas."""

from pessoa import Pessoa

class CadastroPessoas:
    """Mantém e gerencia o conjunto de pessoas cadastradas."""

    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        return self.__pessoas

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa
