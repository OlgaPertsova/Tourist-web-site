// ------------------работа слайдера---------
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 2,
    spaceBetween: 100,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
});

// -----------работа поиска города--------

document.querySelector('#list-cities').oninput = function(){
  let val = this.value.trim();
  let listItems = document.querySelectorAll('.category-list li');
  if (val != ''){
    listItems.forEach(function(elem){
      if (elem.innerText.search(val) == -1) {
        elem.classList.add('hide');
      }
      else {
        elem.classList.remove('hide');
      }
    });
  }
  else {
    listItems.forEach(function(elem){
        elem.classList.remove('hide');
      });
  }
}