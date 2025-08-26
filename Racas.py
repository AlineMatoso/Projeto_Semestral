import random

class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento_tendencia, habilidades):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento_tendencia = alinhamento_tendencia
        self.habilidades = habilidades
    
    def __str__(self):
        infravisao_str = f"{self.infravisao} metros" if self.infravisao != "Não" else "Não possui"
        habilidades_str = "\n  - ".join(self.habilidades)
        return (f"{self.nome}:\n"
                f"  Movimento: {self.movimento} metros\n"
                f"  Infravisão: {infravisao_str}\n"
                f"  Tendência de Alinhamento: {self.alinhamento_tendencia}\n"
                f"  Habilidades:\n  - {habilidades_str}")

class Humano(Raca):
    def __init__(self):
        habilidades = [
            "Aprendizado: Recebe bônus de 10% sobre toda experiência (XP) recebida",
            "Adaptabilidade: Recebe +1 em uma única Jogada de Proteção à sua escolha"
        ]
        super().__init__("Humano", 9, "Não", "Qualquer", habilidades)

class Elfo(Raca):
    def __init__(self):
        habilidades = [
            "Percepção Natural: Pode detectar portas secretas com 1-2 em 1d6",
            "Graciosos: +1 em qualquer teste de Jogada de Proteção de Destreza (JPD)",
            "Arma Racial: +1 de dano em ataques à distância com arcos",
            "Imunidades: Imune a efeitos de sono e paralisia de Ghouls"
        ]
        super().__init__("Elfo", 9, 18, "Neutralidade", habilidades)

class Anao(Raca):
    def __init__(self):
        habilidades = [
            "Mineradores: Detecta anomalias em pedras com 1-2 em 1d6",
            "Vigoroso: +1 em qualquer teste de Jogada de Proteção de Constituição (JPC)",
            "Armas Grandes: Armas grandes forjadas como item racial são consideradas médias",
            "Inimigos: Ataques contra orcs, ogros e hobgoblins são considerados fáceis"
        ]
        super().__init__("Anão", 6, 18, "Ordem", habilidades)

class Halfling(Raca):
    def __init__(self):
        habilidades = [
            "Furtivos: Esconder-se com chance de 1-2 em 1d6 (+1 se for Ladrão)",
            "Destemidos: +1 em qualquer teste de Jogada de Proteção de Sabedoria (JPS)",
            "Bons de Mira: Ataques à distância com armas de arremesso são considerados fáceis",
            "Pequenos: Ataques de criaturas grandes são considerados difíceis",
            "Restrições: Só pode usar armaduras de couro e armas pequenas ou médias"
        ]
        super().__init__("Halfling", 6, "Não", "Neutralidade", habilidades)

class MeioElfo(Raca):
    def __init__(self):
        habilidades = [
            "Aprendizado: Recebe bônus de 10% sobre toda experiência (XP) recebida",
            "Gracioso e Vigoroso: +1 em JPD e JPC",
            "Idioma Extra: Aprende um idioma adicional",
            "Imunidades: Imune a efeitos de sono e paralisia de Ghouls"
        ]
        super().__init__("Meio-Elfo", 9, 9, "Caos", habilidades)

class Gnomo(Raca):
    def __init__(self):
        habilidades = [
            "Avaliadores: Percepção aguçada para detectar perigos",
            "Sacazes e Vigorosos: +1 em JPS e JPC",
            "Restrições: Limitações em equipamentos específicos"
        ]
        super().__init__("Gnomo", 6, 18, "Neutralidade", habilidades)

class GeradorRaca:
    def __init__(self):
        self.racas = {
            "1": Humano(),
            "2": Elfo(),
            "3": Anao(),
            "4": Halfling(),
            "5": MeioElfo(),
            "6": Gnomo()
        }
    
    def listar_racas(self):
        print("\nRaças disponíveis:")
        for key, raca in self.racas.items():
            print(f"{key} - {raca.nome}")
    
    def escolher_raca(self):
        self.listar_racas()
        
        while True:
            escolha = input("\nDigite o número da raça desejada: ").strip()
            if escolha in self.racas:
                return self.racas[escolha]
            else:
                print("Opção inválida. Tente novamente.")
    
    def raca_aleatoria(self):
        return random.choice(list(self.racas.values()))