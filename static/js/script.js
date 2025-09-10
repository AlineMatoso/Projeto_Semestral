// Scripts para interatividade da interface
document.addEventListener('DOMContentLoaded', function() {
    // Toggle de visibilidade para listas de raças e classes
    const toggleLists = function() {
        const opcoesRaca = document.querySelectorAll('input[name="opcao_raca"]');
        const listaRacas = document.getElementById('lista-racas');
        
        if (opcoesRaca.length && listaRacas) {
            opcoesRaca.forEach(opcao => {
                opcao.addEventListener('change', function() {
                    if (this.value === 'sortear') {
                        listaRacas.style.display = 'none';
                    } else {
                        listaRacas.style.display = 'block';
                    }
                });
            });
        }
        
        const opcoesClasse = document.querySelectorAll('input[name="opcao_classe"]');
        const listaClasses = document.getElementById('lista-classes');
        
        if (opcoesClasse.length && listaClasses) {
            opcoesClasse.forEach(opcao => {
                opcao.addEventListener('change', function() {
                    if (this.value === 'sortear') {
                        listaClasses.style.display = 'none';
                    } else {
                        listaClasses.style.display = 'block';
                    }
                });
            });
        }
    };
    
    toggleLists();
});