import random

class Classe:
    def __init__(self, nome, dado_vida, armas, armaduras, itens_magicos, habilidades):
        self.nome = nome
        self.dado_vida = dado_vida
        self.armas = armas
        self.armaduras = armaduras
        self.itens_magicos = itens_magicos
        self.habilidades = habilidades
    
    def rolar_pontos_vida(self, modificador_constituicao):
        """Rola os pontos de vida iniciais baseado no dado de vida da classe"""
        if self.dado_vida == "d10":
            pv_base = 10
            dado = random.randint(1, 10)
        elif self.dado_vida == "d8":
            pv_base = 8
            dado = random.randint(1, 8)
        elif self.dado_vida == "d6":
            pv_base = 6
            dado = random.randint(1, 6)
        elif self.dado_vida == "d4":
            pv_base = 4
            dado = random.randint(1, 4)
        else:
            pv_base = 0
            dado = 0
        
        pv_total = pv_base + dado + modificador_constituicao
        return max(1, pv_total)  # Garante pelo menos 1 PV
    
    def __str__(self):
        habilidades_str = "\n  - ".join(self.habilidades)
        return (f"{self.nome}:\n"
                f"  Dado de Vida: {self.dado_vida}\n"
                f"  Armas: {self.armas}\n"
                f"  Armaduras: {self.armaduras}\n"
                f"  Itens Mágicos: {self.itens_magicos}\n"
                f"  Habilidades:\n  - {habilidades_str}")

class Guerreiro(Classe):
    def __init__(self):
        habilidades = [
            "Aparar: Pode sacrificar escudo ou arma para absorver dano",
            "Maestria em Arma: +1 de dano em uma arma à escolha (evolui nos níveis 3 e 10)",
            "Ataque Extra: No 6º nível, ganha um segundo ataque com a mesma arma"
        ]
        super().__init__("Guerreiro", "d10", "Todas as armas", "Todas as armaduras", 
                         "Não pode usar cajados, varinhas e pergaminhos (exceto proteção)", habilidades)

class Barbaro(Classe):
    def __init__(self):
        habilidades = [
            "Vigor Bárbaro: +2 PV por nível e +2 na Jogada de Proteção de Constituição (JPC)",
            "Talentos Selvagens: Escalar, Camuflagem natural, Surpresa Selvagem",
            "Força do Totem: Pode atingir criaturas que exigem armas mágicas +1",
            "Restrições: Não pode usar itens mágicos nem armaduras além de couro"
        ]
        super().__init__("Bárbaro", "d10", "Todas as armas", "Apenas couro", 
                         "Nenhum item mágico", habilidades)
    
    def rolar_pontos_vida(self, modificador_constituicao):
        """Bárbaro recebe +2 PV por nível além do modificador de CONST"""
        pv_base = 10  # Guerreiro base
        dado = random.randint(1, 10)
        pv_total = pv_base + dado + modificador_constituicao + 2  # +2 do Vigor Bárbaro
        return max(1, pv_total)

class Druida(Classe):
    def __init__(self):
        habilidades = [
            "Herbalismo: Identificar plantas, animais e água potável",
            "Previdência: Acampamentos criados nos ermos são sempre seguros",
            "Transformação: Assumir forma de animal pequeno (3x/dia, evolui no nível 10)",
            "Restrições: Alinhamento neutro, não pode usar armas/armaduras metálicas",
            "Magias Divinas: Conjura magias divinas como Clérigo"
        ]
        super().__init__("Druida", "d8", "Apenas armas impactantes e não metálicas", 
                         "Apenas armaduras não metálicas", "Todos os tipos (se ordeiros)", habilidades)

class Clerigo(Classe):
    def __init__(self):
        habilidades = [
            "Magias Divinas: Conjura magias divinas a partir do 1º nível",
            "Afastar Mortos-Vivos: Afasta mortos-vivos uma vez ao dia (evolui nos níveis 3 e 6)",
            "Cura Milagrosa: Pode trocar magias por Curar Ferimentos (evolui nos níveis 3 e 6)",
            "Restrições: Só pode usar armas impactantes para manter magias"
        ]
        super().__init__("Clérigo", "d8", "Apenas armas impactantes", "Todas as armaduras", 
                         "Todos os tipos (se ordeiros)", habilidades)

class Mago(Classe):
    def __init__(self):
        habilidades = [
            "Magias Arcanas: Conjura magias arcanas diariamente a partir do grimório",
            "Ler Magias: Identificar inscrições mágicas (1x/dia por nível)",
            "Detectar Magias: Perceber presença mágica (1x/dia por nível)",
            "Restrições: Nenhuma armadura, apenas armas pequenas"
        ]
        super().__init__("Mago", "d4", "Apenas armas pequenas", "Nenhuma", 
                         "Todos os tipos", habilidades)

class Ladrao(Classe):
    def __init__(self):
        habilidades = [
            "Ataque Furtivo: Dano multiplicado ao atacar sorrateiramente (x2, x3 no nível 3, x4 no nível 6)",
            "Ouvir Ruídos: Detectar sons com 1-2 em 1d6 (evolui nos níveis 3, 6 e 9)",
            "Talentos de Ladrão: Armadilha, Arrombar, Escalar, Furtividade, Punga",
            "Restrições: Apenas armas pequenas/médias e armaduras leves"
        ]
        super().__init__("Ladrão", "d6", "Apenas pequenas ou médias", "Apenas leves", 
                         "Não pode usar cajados, varinhas e pergaminhos (exceto proteção)", habilidades)

class GeradorClasse:
    def __init__(self):
        self.classes = {
            "1": Guerreiro(),
            "2": Barbaro(),
            "3": Druida(),
            "4": Clerigo(),
            "5": Mago(),
            "6": Ladrao()
        }
    
    def listar_classes(self):
        print("\nClasses disponíveis:")
        for key, classe in self.classes.items():
            print(f"{key} - {classe.nome} ({classe.dado_vida})")
    
    def escolher_classe(self):
        self.listar_classes()
        
        while True:
            escolha = input("\nDigite o número da classe desejada: ").strip()
            if escolha in self.classes:
                return self.classes[escolha]
            else:
                print("Opção inválida. Tente novamente.")
    
    def classe_aleatoria(self):
        return random.choice(list(self.classes.values()))