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
document.getElementById("open__reviews__modal__btn").addEventListener("click", function () {
    const modal = document.getElementById("reviews__modal");
    const modalBody = document.getElementById("modal__body");
    const url = this.getAttribute("data-url");

    modal.style.display = "flex";

    fetch(url)
        .then(res => res.text())
        .then(html => {
            modalBody.innerHTML = html;
        })
        .catch(() => {
            modalBody.innerHTML = "<p>Erro ao carregar avaliações.</p>";
        });
});

document.querySelector(".modal__close__btn").addEventListener("click", function () {
    document.getElementById("reviews__modal").style.display = "none";
});