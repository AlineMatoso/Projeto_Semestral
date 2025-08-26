from ModoJogo import ModoClassico, ModoAventureiro, ModoHeroico
from Racas import Humano, Elfo, Anao, Halfling, MeioElfo, Gnomo, GeradorRaca
from Classes import Guerreiro, Barbaro, Druida, Clerigo, Mago, Ladrao, GeradorClasse
import random

class Main:
    def __init__(self):
        self.nome_jogador = ""
        self.atributos = {}
        self.raca = None
        self.classe = None
        self.pontos_vida = 0
    
    def obter_nome_jogador(self):
        print("=" * 50)
        print("CRIAÇÃO DE PERSONAGEM - OLD DRAGON 2")
        print("=" * 50)
        self.nome_jogador = input("Digite o nome do jogador: ").strip()
    
    def selecionar_modo_jogo(self):
        print(f"\n{self.nome_jogador}, escolha o modo de geração de atributos:")
        print("1 - Clássico (3d6 em ordem fixa)")
        print("2 - Aventureiro (3d6, distribui livremente)")
        print("3 - Heroico (4d6, elimina o menor, distribui livremente)")
        
        modos = {
            "1": ModoClassico(),
            "2": ModoAventureiro(),
            "3": ModoHeroico()
        }
        
        while True:
            escolha = input("Digite o número da opção desejada (1, 2 ou 3): ").strip()
            if escolha in modos:
                modo_selecionado = modos[escolha]
                self.atributos = modo_selecionado.rolar_atributos()
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def selecionar_raca(self):
        print(f"\n{self.nome_jogador}, agora selecione a raça do personagem:")
        gerador_raca = GeradorRaca()
        
        print("Deseja escolher uma raça ou sortear aleatoriamente?")
        print("1 - Escolher raça")
        print("2 - Sortear aleatoriamente")
        
        while True:
            opcao_raca = input("Digite sua escolha (1 ou 2): ").strip()
            if opcao_raca == "1":
                self.raca = gerador_raca.escolher_raca()
                break
            elif opcao_raca == "2":
                self.raca = gerador_raca.raca_aleatoria()
                print(f"\nRaça sorteada: {self.raca.nome}")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def selecionar_classe(self):
        print(f"\n{self.nome_jogador}, agora selecione a classe do personagem:")
        gerador_classe = GeradorClasse()
        
        print("Deseja escolher uma classe ou sortear aleatoriamente?")
        print("1 - Escolher classe")
        print("2 - Sortear aleatoriamente")
        
        while True:
            opcao_classe = input("Digite sua escolha (1 ou 2): ").strip()
            if opcao_classe == "1":
                self.classe = gerador_classe.escolher_classe()
                break
            elif opcao_classe == "2":
                self.classe = gerador_classe.classe_aleatoria()
                print(f"\nClasse sorteada: {self.classe.nome}")
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        # Calcular pontos de vida baseado na constituição
        mod_con = self.calcular_modificador(self.atributos.get("Constituição", 10))
        self.pontos_vida = self.classe.rolar_pontos_vida(mod_con)
    
    def calcular_modificador(self, valor):
        """Calcula o modificador de atributo baseado no valor"""
        if valor <= 3:
            return -3
        elif valor <= 5:
            return -2
        elif valor <= 8:
            return -1
        elif valor <= 12:
            return 0
        elif valor <= 14:
            return 1
        elif valor <= 16:
            return 2
        elif valor <= 18:
            return 3
        else:
            return 4
    
    def classificar_atributo(self, nome, valor):
        """Classifica o atributo conforme a tabela específica de cada um (páginas 12-13)"""
        if nome == "Força":
            if valor <= 8: return "Fraco"
            elif valor <= 12: return "Mediano"
            elif valor <= 16: return "Forte"
            else: return "Muito Forte"
        
        elif nome == "Destreza":
            if valor <= 8: return "Letárgico"
            elif valor <= 12: return "Mediano"
            elif valor <= 16: return "Ágil"
            else: return "Preciso"
        
        elif nome == "Constituição":
            if valor <= 8: return "Frágil"
            elif valor <= 12: return "Mediano"
            elif valor <= 16: return "Resistente"
            else: return "Vigoroso"
        
        elif nome == "Inteligência":
            if valor <= 8: return "Inepto"
            elif valor <= 12: return "Mediano"
            elif valor <= 16: return "Inteligente"
            else: return "Gênio"
        
        elif nome == "Sabedoria":
            if valor <= 8: return "Tolo"
            elif valor <= 12: return "Mediano"
            elif valor <= 16: return "Intuitivo"
            else: return "Presidente"
        
        elif nome == "Carisma":
            if valor <= 8: return "Descortês"
            elif valor <= 12: return "Mediano"
            elif valor <= 16: return "Influente"
            else: return "Ídolo"
        
        return "Desconhecido"
    
    def exibir_personagem_completo(self):
        print("\n" + "=" * 60)
        print("FICHA DO PERSONAGEM - OLD DRAGON 2")
        print("=" * 60)
        print(f"Jogador: {self.nome_jogador}")
        print(f"Raça: {self.raca.nome}")
        print(f"Classe: {self.classe.nome}")
        print(f"Pontos de Vida: {self.pontos_vida}")
        
        print("\nATRIBUTOS:")
        for atributo, valor in self.atributos.items():
            classificacao = self.classificar_atributo(atributo, valor)
            modificador = self.calcular_modificador(valor)
            sinal = "+" if modificador >= 0 else ""
            print(f"  {atributo}: {valor} ({classificacao}) - Modificador: {sinal}{modificador}")
        
        print(f"\nINFORMAÇÕES DA RAÇA:")
        print(f"  Movimento: {self.raca.movimento} metros")
        print(f"  Infravisão: {self.raca.infravisao}")
        print(f"  Tendência de Alinhamento: {self.raca.alinhamento_tendencia}")
        print("  Habilidades:")
        for habilidade in self.raca.habilidades:
            print(f"    - {habilidade}")
        
        print(f"\nINFORMAÇÕES DA CLASSE:")
        print(f"  Dado de Vida: {self.classe.dado_vida}")
        print(f"  Armas Permitidas: {self.classe.armas}")
        print(f"  Armaduras Permitidas: {self.classe.armaduras}")
        print(f"  Itens Mágicos: {self.classe.itens_magicos}")
        print("  Habilidades:")
        for habilidade in self.classe.habilidades:
            print(f"    - {habilidade}")
        
        print("\n" + "=" * 60)
    
    def executar(self):
        self.obter_nome_jogador()
        self.selecionar_modo_jogo()
        self.selecionar_raca()
        self.selecionar_classe()
        self.exibir_personagem_completo()

# Executar o programa
if __name__ == "__main__":
    criador_personagem = Main()
    criador_personagem.executar()