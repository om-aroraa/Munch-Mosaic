// document.getElementById('menu-icon').addEventListener('click', function() {
//     document.querySelector('.navbar').classList.toggle('menu-open');
//     document.querySelector('.main-content').classList.toggle('menu-open');
// });


function scrollCards(cardNumber) {
    const targetCard = document.getElementById(`card${cardNumber}`);
    targetCard.scrollIntoView({ behavior: 'smooth' });
}

const cursorRounded = document.querySelector('.rounded');
const cursorPointed = document.querySelector('.pointed');


const moveCursor = (e) => {
    const mouseY = e.clientY;
    const mouseX = e.clientX;

    cursorPointed.style.left = `${mouseX}px`;
    cursorPointed.style.top = `${mouseY}px`;


    cursorRounded.animate({
        left: `${mouseX}px`,
        top: `${mouseY}px`
    }, {duration: 400, fill: 'forwards'})
}

window.addEventListener('mousemove', moveCursor)