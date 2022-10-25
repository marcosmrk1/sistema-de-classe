class Cachorros:
    def __init__(self):
        self.tipo = "cachorros"

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setIdade(self,idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def setComprimento_dos_pelos(self,comprimento_dos_pelos):
        self.comprimento_dos_pelos = comprimento_dos_pelos

    def getComprimento_dos_pelos(self):
        return self.comprimento_dos_pelos

    def setCor_dos_pêlos(self,cor_dos_pêlos):
        self.cor_dos_pêlos=cor_dos_pêlos

    def getCor_dos_pêlos(self):
        return self.cor_dos_pêlos

    def setCor_dos_olhos(self,cor_dos_olhos):
        self.cor_dos_olhos = cor_dos_olhos

    def getCor_dos_olhos(self):
        return self.cor_dos_olhos

cachorros=Cachorros()
cachorros.setNome("pluto")
print(cachorros.getNome())


cachorros.setIdade('2 anos')
print(cachorros.getIdade())


cachorros.setComprimento_dos_pelos("curto")
print(cachorros.getComprimento_dos_pelos())

cachorros.setCor_dos_pêlos("bege")
print(cachorros.getCor_dos_pêlos())

cachorros.setCor_dos_olhos("castanho")
print(cachorros.getCor_dos_olhos())