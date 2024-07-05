document.querySelectorAll('.dropdown-toggle').forEach(button => {
    button.addEventListener('click', () => {
        button.nextElementSibling.classList.toggle('show');
    });
});