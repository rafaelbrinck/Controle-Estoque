class Produto:
    def __init__(self, nome, preco, medidas, categoria):
        self.nome = nome
        self.preco = preco
        self.medidas = medidas
        self.categoria = categoria
    def getnome(self):
        return self.nome
    def getpreco(self):
        return self.preco
    def getmedidas(self):
        return self.medidas
    def getcategoria(self):
        return self.categoria
    
    def to_dict(self):
        return {
            "Nome": self.nome,
            "Preco": self.preco,
            "Medidas": self.medidas,
            "Categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data["Nome"],
            preco=data["Preco"],
            medidas=data["Medidas"],
            categoria = data["Categoria"]
        )
