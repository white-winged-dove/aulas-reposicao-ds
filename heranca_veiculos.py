# classe mãe
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

# classe filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, numero_portas):
        super().__init__(marca, modelo, cor)  # herdando os atributos da classe base
        self.numero_portas = numero_portas




