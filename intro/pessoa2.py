class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print('estou dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None:
        print('lalalala')

    def apresentar_idade(self):
        return self.idade


