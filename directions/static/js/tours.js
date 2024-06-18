const swiperComment = new Swiper('.js-commentList-slider', {
    grabCursor: true,
    slidesPerView: 3,
    spaceBetween: 10,
    pagination:{
        el: '.js-commentList-pagination',
        clickable: true
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    breakpoints:{
        676:{
            slidePerView: 2
        }
    }
});
// --------------------stars rating1-----------------------------------



// --------------------stars rating-----------------------------------

// const ratings = document.querySelectorAll('.rating');
// if (ratings.length > 0) {
//     initRatings();
// }

// //основная функция
// function initRatings() {
//     let ratingActive, ratingValue;
//     for (let index = 0; index < ratings.length; index++) {
//         const rating = ratings[index];
//         initRating(rating);
//     }

//     //Инициализация конкретного рейтинга
//     function initRating(rating) {
//         initRatingVars(rating);

//         setRatingActiveWidth();

//         if (rating.classList.contains('rating_set')) {
//             setRating(rating);
//         }
//     }

//     //Инициализация переменных
//     function initRatingVars(rating) {
//         ratingActive = rating.querySelector('.rating__active');
//         ratingValue = rating.querySelector('.rating__value');
//     }
//     //Измнение ширины активных звезд
//     function setRatingActiveWidth(index = ratingValue.innerHTML) {
//         const ratingActiveWidth = index / 0.05;
//         ratingActive.style.width = `${ratingActiveWidth}%`;
//     }

//     function setRating(rating) {
//         const ratingItems = rating.querySelectorAll('.rating__item');
//         for (let index = 0; index < ratingItems.length; index++) {
//             const ratingItem = ratingItems[index];
//             ratingItem.addEventListener("mouseenter", function (e) {
//                 initRatingVars(rating);
//                 setRatingActiveWidth(ratingItem.value);
//             });
//             ratingItem.addEventListener("mouseleave", function (e) {
//                 setRatingActiveWidth();
//             });
//         }
//     }
// }


