const dropdownToggle = document.querySelector('.dropdown-toggle');
const dropdownMenu = document.querySelector('.dropdown-menu');
const modeToggle = document.getElementById('modeToggle');
const html = document.documentElement;

dropdownToggle.addEventListener('click', function () {
    dropdownMenu.classList.toggle('show');
});

modeToggle.addEventListener('click', () => {
    html.classList.toggle('dark');
});
