function toggleMenu() {
    document.getElementById('profileMenu').classList.toggle('navbar__dropdown--active');
}

// Carrossel automático
const carousel = document.getElementById('carousel');
let index = 0;
setInterval(() => {
    index = (index + 1) % carousel.children.length;
    carousel.scrollTo({
        left: carousel.clientWidth * index,
        behavior: 'smooth'
    });
}, 3500);

// Requisição para as reviews de um jogo específico
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('reviews__modal');
    const openBtn = document.getElementById('open__reviews__modal__btn');
    const closeBtn = document.querySelector('.modal__close__btn');
    const modalBody = document.getElementById('modal__body');

    openBtn.onclick = async function () {
        const url = openBtn.dataset.url;

        modalBody.innerHTML = '<p>Carregando avaliações...</p>';
        modal.style.display = 'flex';

        try {
            // Faz a requisição AJAX para a URL das reviews
            const response = await fetch(url);
            const reviewsHtml = await response.text();

            modalBody.innerHTML = reviewsHtml;
        } catch (error) {
            modalBody.innerHTML = '<p>Ocorreu um erro ao carregar as avaliações.</p>';
            console.error('Erro na requisição AJAX:', error);
        }
    }

    closeBtn.onclick = function () {
        modal.style.display = 'none';
    }
    // window.onclick = function (event) {
    //     if (event.target == modal) {
    //         modal.style.display = 'none';
    //     }
    // }
});