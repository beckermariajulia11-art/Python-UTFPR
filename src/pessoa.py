class Pessoa:
    """definição da classe"""
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getEmail(self):
        return self.__email

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setEmail(self, email):
        self.__email = email
