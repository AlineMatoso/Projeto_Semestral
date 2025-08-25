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
        
        print("\nRolando 3d6 para cada atributo na ordem fixa...")
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
        print("\nRolando 3d6 seis vezes...")
        for i in range(6):
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            dado3 = random.randint(1, 6)
            soma = dado1 + dado2 + dado3
            valores.append(soma)
        
        atributos = {}
        nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        
        print(f"\nValores rolados: {valores}")
        print("Distribua esses valores nos atributos na ordem que desejar.")
        
        for nome in nomes:
            while True:
                try:
                    print(f"\nValores disponíveis: {valores}")
                    valor = int(input(f"Digite o valor para {nome}: "))
                    if valor in valores:
                        atributos[nome] = valor
                        valores.remove(valor)
                        break
                    else:
                        print("Valor não está na lista de valores rolados. Tente novamente.")
                except ValueError:
                    print("Por favor, digite um número inteiro.")
        
        return atributos

class ModoHeroico(ModoJogo):
    def __init__(self):
        super().__init__("Heroico", "Role 4d6 seis vezes, eliminando o menor valor de cada rolagem, e distribua livremente")
    
    def rolar_atributos(self):
        valores = []
        print("\nRolando 4d6 seis vezes (eliminando o menor valor)...")
        for i in range(6):
            dados = [random.randint(1, 6) for _ in range(4)]
            dados.sort()
            soma = sum(dados[1:])  # Elimina o menor (primeiro da lista ordenada)
            valores.append(soma)
        
        atributos = {}
        nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        
        print(f"\nValores rolados: {valores}")
        print("Distribua esses valores nos atributos na ordem que desejar.")
        
        for nome in nomes:
            while True:
                try:
                    print(f"\nValores disponíveis: {valores}")
                    valor = int(input(f"Digite o valor para {nome}: "))
                    if valor in valores:
                        atributos[nome] = valor
                        valores.remove(valor)
                        break
                    else:
                        print("Valor não está na lista de valores rolados. Tente novamente.")
                except ValueError:
                    print("Por favor, digite um número inteiro.")
        
        return atributos