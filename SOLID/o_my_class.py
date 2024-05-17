class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Marabalista:

    def apresentar_show(self):
        print('Marabalista no picadeiro!')


class Palhaco:

    def apresentar_show(self):
        print('Palhaco fazendo palhacada!')


circo = Circo()
palhaco = Palhaco()
marabalista = Marabalista()

circo.apresentar(marabalista)