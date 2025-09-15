from flask import Flask, render_template, request, session, redirect, url_for
import random
import json
from model.Racas import Humano, Elfo, Anao, Halfling, MeioElfo, Gnomo, GeradorRaca
from model.Classes import Guerreiro, Barbaro, Druida, Clerigo, Mago, Ladrao, GeradorClasse
from model.ModoJogo import ModoClassico, ModoAventureiro, ModoHeroico

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Alterar para produção

class PersonagemController:
    @staticmethod
    def calcular_modificador(valor):
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

    @staticmethod
    def classificar_atributo(nome, valor):
        """Classifica o atributo conforme a tabela específica"""
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

@app.route('/')
def index():
    """Página inicial com formulário de criação de personagem"""
    return render_template('index.html')

@app.route('/criar_personagem', methods=['POST'])
def criar_personagem():
    """Processa a criação do personagem"""
    # Obter nome do jogador
    nome_jogador = request.form.get('nome_jogador')
    if not nome_jogador:
        return redirect(url_for('index'))
    
    session['nome_jogador'] = nome_jogador
    
    # Selecionar modo de jogo
    modo_jogo = request.form.get('modo_jogo')
    modos = {
        '1': ModoClassico(),
        '2': ModoAventureiro(),
        '3': ModoHeroico()
    }
    
    if modo_jogo not in modos:
        return redirect(url_for('index'))
    
    session['modo_jogo'] = modo_jogo
    resultado = modos[modo_jogo].rolar_atributos()
    
    # Se for modo clássico, já temos os atributos prontos
    if modo_jogo == '1':
        session['atributos'] = resultado
        return redirect(url_for('selecionar_raca'))
    else:
        # Para modos Aventureiro e Heroico, precisamos distribuir os valores
        session['valores_atributos'] = resultado['valores']
        session['atributos_distribuidos'] = False
        return redirect(url_for('distribuir_atributos'))

@app.route('/distribuir_atributos')
def distribuir_atributos():
    """Página para distribuir os valores dos atributos"""
    if 'valores_atributos' not in session:
        return redirect(url_for('index'))
    
    valores = session['valores_atributos']
    modo = session['modo_jogo']
    
    if modo == '2':
        modo_nome = "Aventureiro"
        modo_desc = "Distribua os valores rolados (3d6) livremente entre os atributos"
    else:
        modo_nome = "Heroico"
        modo_desc = "Distribua os valores rolados (4d6, eliminando o menor) livremente entre os atributos"
    
    # Converter valores para JSON string para usar no template
    valores_json = json.dumps(valores)
    
    return render_template('distribuir_atributos.html', 
                         valores=valores,
                         valores_json=valores_json,
                         modo_nome=modo_nome, 
                         modo_desc=modo_desc)

@app.route('/processar_distribuicao', methods=['POST'])
def processar_distribuicao():
    """Processa a distribuição dos atributos"""
    if 'valores_atributos' not in session:
        return redirect(url_for('index'))
    
    # Obter os valores dos atributos do formulário
    atributos = {
        'Força': int(request.form.get('forca')),
        'Destreza': int(request.form.get('destreza')),
        'Constituição': int(request.form.get('constituicao')),
        'Inteligência': int(request.form.get('inteligencia')),
        'Sabedoria': int(request.form.get('sabedoria')),
        'Carisma': int(request.form.get('carisma'))
    }
    
    # Verificar se todos os valores foram usados (validação básica)
    valores_originais = sorted(session['valores_atributos'])
    valores_distribuidos = sorted(list(atributos.values()))
    
    if valores_originais != valores_distribuidos:
        # Se os valores não coincidem, redirecionar de volta
        session['erro_distribuicao'] = "Os valores distribuídos não correspondem aos valores rolados."
        return redirect(url_for('distribuir_atributos'))
    
    # Salvar os atributos e continuar
    session['atributos'] = atributos
    session['atributos_distribuidos'] = True
    session.pop('valores_atributos', None)
    session.pop('erro_distribuicao', None)
    
    return redirect(url_for('selecionar_raca'))

@app.route('/selecionar_raca')
def selecionar_raca():
    """Página para seleção de raça"""
    # Verificar se os atributos já foram distribuídos (para modos 2 e 3)
    if session.get('modo_jogo') != '1' and not session.get('atributos_distribuidos'):
        return redirect(url_for('distribuir_atributos'))
    
    gerador_raca = GeradorRaca()
    racas = gerador_raca.racas
    
    return render_template('componentes/racas.html', racas=racas)

@app.route('/escolher_raca', methods=['POST'])
def escolher_raca():
    """Processa a escolha da raça"""
    opcao_raca = request.form.get('opcao_raca')
    gerador_raca = GeradorRaca()
    
    if opcao_raca == 'escolher':
        raca_id = request.form.get('raca_id')
        if raca_id in gerador_raca.racas:
            session['raca'] = {
                'nome': gerador_raca.racas[raca_id].nome,
                'movimento': gerador_raca.racas[raca_id].movimento,
                'infravisao': gerador_raca.racas[raca_id].infravisao,
                'alinhamento_tendencia': gerador_raca.racas[raca_id].alinhamento_tendencia,
                'habilidades': gerador_raca.racas[raca_id].habilidades
            }
    elif opcao_raca == 'sortear':
        raca_aleatoria = gerador_raca.raca_aleatoria()
        session['raca'] = {
            'nome': raca_aleatoria.nome,
            'movimento': raca_aleatoria.movimento,
            'infravisao': raca_aleatoria.infravisao,
            'alinhamento_tendencia': raca_aleatoria.alinhamento_tendencia,
            'habilidades': raca_aleatoria.habilidades
        }
    else:
        return redirect(url_for('selecionar_raca'))
    
    return redirect(url_for('selecionar_classe'))

@app.route('/selecionar_classe')
def selecionar_classe():
    """Página para seleção de classe"""
    if 'raca' not in session:
        return redirect(url_for('selecionar_raca'))
    
    gerador_classe = GeradorClasse()
    classes = gerador_classe.classes
    
    return render_template('componentes/classes.html', classes=classes)

@app.route('/escolher_classe', methods=['POST'])
def escolher_classe():
    """Processa a escolha da classe"""
    opcao_classe = request.form.get('opcao_classe')
    gerador_classe = GeradorClasse()
    
    if opcao_classe == 'escolher':
        classe_id = request.form.get('classe_id')
        if classe_id in gerador_classe.classes:
            classe = gerador_classe.classes[classe_id]
            session['classe'] = {
                'nome': classe.nome,
                'dado_vida': classe.dado_vida,
                'armas': classe.armas,
                'armaduras': classe.armaduras,
                'itens_magicos': classe.itens_magicos,
                'habilidades': classe.habilidades
            }
    elif opcao_classe == 'sortear':
        classe_aleatoria = gerador_classe.classe_aleatoria()
        session['classe'] = {
            'nome': classe_aleatoria.nome,
            'dado_vida': classe_aleatoria.dado_vida,
            'armas': classe_aleatoria.armas,
            'armaduras': classe_aleatoria.armaduras,
            'itens_magicos': classe_aleatoria.itens_magicos,
            'habilidades': classe_aleatoria.habilidades
        }
    else:
        return redirect(url_for('selecionar_classe'))
    
    # Calcular pontos de vida
    mod_con = PersonagemController.calcular_modificador(session['atributos'].get("Constituição", 10))
    
    # Instanciar a classe para calcular PV
    classe_obj = None
    if session['classe']['nome'] == 'Guerreiro':
        classe_obj = Guerreiro()
    elif session['classe']['nome'] == 'Bárbaro':
        classe_obj = Barbaro()
    elif session['classe']['nome'] == 'Druida':
        classe_obj = Druida()
    elif session['classe']['nome'] == 'Clérigo':
        classe_obj = Clerigo()
    elif session['classe']['nome'] == 'Mago':
        classe_obj = Mago()
    elif session['classe']['nome'] == 'Ladrão':
        classe_obj = Ladrao()
    
    if classe_obj:
        session['pontos_vida'] = classe_obj.rolar_pontos_vida(mod_con)
    
    return redirect(url_for('exibir_personagem'))

@app.route('/personagem')
def exibir_personagem():
    """Exibe o personagem completo"""
    if 'nome_jogador' not in session:
        return redirect(url_for('index'))
    
    # Preparar dados para exibição
    atributos_com_modificadores = {}
    for nome, valor in session['atributos'].items():
        modificador = PersonagemController.calcular_modificador(valor)
        classificacao = PersonagemController.classificar_atributo(nome, valor)
        atributos_com_modificadores[nome] = {
            'valor': valor,
            'modificador': modificador,
            'classificacao': classificacao
        }
    
    return render_template('personagem.html', 
                         nome_jogador=session['nome_jogador'],
                         raca=session['raca'],
                         classe=session['classe'],
                         pontos_vida=session.get('pontos_vida', 0),
                         atributos=atributos_com_modificadores)

@app.route('/reiniciar')
def reiniciar():
    """Reinicia a criação do personagem"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)