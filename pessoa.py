class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf        # quando colocamos __atributo estamos informando que é um atributo privado da classe sendo só possível acessar seu valor por meio de um método

    def correr(self):
        print('estou correndo!')

    def beber(self, bebida):
        if bebida == 'vinho':
            self.__apresentar_doc()
            print('bebendo')
        elif bebida == 'coca-cola' or 'cerveja':
            self.correr()
    
    def __apresentar_doc(self):
        print(self.__cpf)


diogenes = Pessoa('Diogenes', 32, '43424423422')
diogenes.beber('cerveja')
diogenes.beber('vinho')