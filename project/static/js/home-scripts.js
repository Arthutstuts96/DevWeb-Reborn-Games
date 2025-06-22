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