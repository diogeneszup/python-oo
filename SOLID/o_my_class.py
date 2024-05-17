class Circo:
    ## COmo não se deve fazer
    def apresentar(self, tipo: int):
        if tipo == 1:
            self.apresentar_marabalista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_marabalista(self):
        print('Marabalista no picadeiro!')

    def apresentar_palhaco(self):
        print('Palhaco fazendo palhacada!')
