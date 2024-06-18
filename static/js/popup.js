//----------------------------------------------------------------------
//функции для сворачивания меню --------------------------------------------


let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.links');

menu.onclick = () => {
    menu.classList.toggle('static/images/close.png');
    navbar.classList.toggle('active');
}

//----------------------------------------------------------------------
//функции для модальных окон---------------------------------------------

// document.addEventListener('click', Event => {
//     const btnType = Event.target.dataset.btn
//     const id = Event.target.dataset.id
     

//     if (btnType === 'open-popup') {
//         document.querySelector('.place').style.display = 'block';
//     }
// })

// document.querySelectorAll('.place-popup').forEach(placePopup =>{
//     placePopup.onclick = () => {
//         document.querySelector('.place').style.display = 'block';
//         document.querySelector('.place').id = div.getAttribute('id');
//     }
// });

let allPlaces = document.querySelectorAll('.place');

document.querySelectorAll('.place-popup').forEach(place =>{
    place.onclick = () =>{
        let id = place.getAttribute('data-id');
        allPlaces.forEach(content =>{
            let target = content.getAttribute('data-target');
            if(id == target){
                document.querySelector('.place').style.display = 'block';
            }
        });
    };
});


document.querySelector('.close-popup').onclick = () =>{
    document.querySelector('.place').style.display = 'none';
}