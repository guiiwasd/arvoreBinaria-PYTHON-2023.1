class No:
    def __init__(self):
        self.__dados = Elemento()
        self.__filhoEsquerda = None
        self.__filhoDireita = None
    def getFilhoEsquerda(self):
        return self.__filhoEsquerda
    def setFilhoEsquerda(self, n):
        self.__filhoEsquerda = n
    def getFilhoDireita(self):
        return self.__filhoDireita
    def setFilhoDireita(self, n):
        self.__filhoDireita = n
    def getDados(self):
        return self.__dados
    def setDados(self, d):
        self.__dados = d
     

class Elemento:
	def __init__(self):
		self.__chave = 0
		self.__nome = ""

	def getChave(self):
		return self.__chave

	def setChave(self, valor):
		self.__chave = valor

	def getNome(self):
		return self.__nome

	def setNome(self, n):
		self.__nome = n

	def getValores(self):
		return self.__chave, self.__nome
     


