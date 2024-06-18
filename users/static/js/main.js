window.onload = function() {
    document.getElementById('up-btn').onclick = function() {
        window.scrollTo(0,0);
    }

}

// barba.init({
//     views: [{
//         namespace: 'home',
//         // beforeEnter() {
//         //   // update the menu based on user navigation
//         //   swiper.update();
//         // },
//         afterEnter() {
//           // refresh the parallax based on new page content
//           cityPage();
//         }
//     }],
//     transitions: [{
//         name: 'opacity-transition',
//         sync: true,
//         leave(data) {
//         return gsap.to(data.current.container, {
//             opacity: 0
//         });
//         },
//         enter(data) {
//         return gsap.from(data.next.container, {
//             opacity: 0
//         });
//         }
//     }]
// });


const wrapper = document.querySelector('.log-wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});
$('.open-popup').click(function(e){
    e.preventDefault();
    $('.popup-bg').fadeIn(600);
});
$('.close-popup').click(function(){
    $('.popup-bg').fadeOut(600);
});




// -------------------------------------------



