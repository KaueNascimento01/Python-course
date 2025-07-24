class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}')"

p = Pessoa("Kauê")
p  # Pessoa(nome='Kauê')AA
