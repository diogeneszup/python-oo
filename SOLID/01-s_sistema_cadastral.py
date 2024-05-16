class SistemaCadastral:

## Exemplo de como NÃO fazer: O método cadastrar tem várias responsabilidades
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('acessando o banco de dados...')
            print('Cadastrar o Usuario {}, Idade {}'.format(nome, idade))
        else:
            print('dados inválidos!')

