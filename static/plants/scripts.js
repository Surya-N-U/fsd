document.addEventListener('DOMContentLoaded', function () {
    const flipButtons = document.querySelectorAll('.btn-flip');

    flipButtons.forEach(button => {
        button.addEventListener('click', function () {
            const cardInner = this.closest('.card-inner');
            cardInner.classList.toggle('is-flipped');
        });
    });
});
