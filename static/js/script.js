document.addEventListener('DOMContentLoaded', function() {
    // Configurar toggles para raças e classes
    configurarToggle('opcao_raca', 'lista-racas');
    configurarToggle('opcao_classe', 'lista-classes');
    
    // Função reutilizável
    function configurarToggle(nomeInput, idLista) {
        const opcoes = document.querySelectorAll(`input[name="${nomeInput}"]`);
        const lista = document.getElementById(idLista);
        
        if (!opcoes.length || !lista) return;
        
        // Configurar cada opção
        opcoes.forEach(opcao => {
            opcao.addEventListener('change', function() {
                lista.style.display = this.value === 'sortear' ? 'none' : 'block';
                
                // Adicionar feedback visual
                lista.style.transition = 'opacity 0.3s ease';
                lista.style.opacity = this.value === 'sortear' ? '0' : '1';
            });
        });
        
        // Configurar estado inicial
        const selecionado = document.querySelector(`input[name="${nomeInput}"]:checked`);
        if (selecionado) {
            lista.style.display = selecionado.value === 'sortear' ? 'none' : 'block';
        }
    }
});