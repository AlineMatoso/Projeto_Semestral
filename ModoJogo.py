import random

class ModoJogo:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
    
    def rolar_atributos(self):
        pass

class ModoClassico(ModoJogo):
    def __init__(self):
        super().__init__("Clássico", "Role 3d6 seis vezes e distribua na ordem: Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma")
    
    def rolar_atributos(self):
        atributos = {}
        nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        
        for nome in nomes:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            dado3 = random.randint(1, 6)
            soma = dado1 + dado2 + dado3
            atributos[nome] = soma
        
        return atributos

class ModoAventureiro(ModoJogo):
    def __init__(self):
        super().__init__("Aventureiro", "Role 3d6 seis vezes e distribua livremente entre os atributos")
    
    def rolar_atributos(self):
        valores = []
        for i in range(6):
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            dado3 = random.randint(1, 6)
            soma = dado1 + dado2 + dado3
            valores.append(soma)
        
        return {"valores": valores, "distribuicao_pendente": True}

class ModoHeroico(ModoJogo):
    def __init__(self):
        super().__init__("Heroico", "Role 4d6 seis vezes, eliminando o menor valor de cada rolagem, e distribua livremente")
    
    def rolar_atributos(self):
        valores = []
        for i in range(6):
            dados = [random.randint(1, 6) for _ in range(4)]
            dados.sort()
            soma = sum(dados[1:])  # Elimina o menor (primeiro da lista ordenada)
            valores.append(soma)
        
        return {"valores": valores, "distribuicao_pendente": True}