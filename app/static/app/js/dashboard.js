const navItems = document.querySelectorAll('.nav-item');

navItems.forEach(item => {
    item.addEventListener('click', () => {
        navItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
    });
});

const currentPath = window.location.pathname;
navItems.forEach(item => {
    if (item.getAttribute('href') === currentPath) {
        item.classList.add('active');
    }
});