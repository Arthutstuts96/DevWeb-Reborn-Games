const block = document.querySelector('.fixed__block');
const btn = document.getElementById('move__block');
const target = document.querySelector('.form__container');

// Função para alinhar o bloco com o formulário
function alignBlock() {
    const rect = target.getBoundingClientRect();

    block.style.width = `${rect.width}px`;
    block.style.height = `${rect.height}px`;
    block.style.left = `${rect.left + window.scrollX}px`;  // importante para scroll
    block.style.top = `${rect.top + window.scrollY}px`;
}

// Alinhar ao carregar
window.addEventListener('DOMContentLoaded', alignBlock);
// Alinhar quando redimensionar a tela
window.addEventListener('resize', alignBlock);

// Animação ao clicar (garante alinhamento antes de mover)
btn.addEventListener('click', () => {
    alignBlock(); 
    block.classList.toggle('move');
});
