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


// review js

var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        },
    },
  });