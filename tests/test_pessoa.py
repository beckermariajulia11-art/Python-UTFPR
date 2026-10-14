from pessoa import Pessoa


def test_alterar_idade():
    pessoa = Pessoa("Ana", 20, "ana@example.com")

    pessoa.setIdade(21)

    assert pessoa.getIdade() == 21
