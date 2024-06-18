// -----------работа поиска события--------
const filterPost = document.querySelectorAll('.blog-post');

document.querySelector('.months').addEventListener('click', (event)=>{
  if (event.target.tagName !== 'LI') return false;

  let filterClass = event.target.dataset['f'];
  
  filterPost.forEach( elem => {
    elem.classList.remove('hide');
    if (!elem.classList.contains(filterClass)) {
        elem.classList.add('hide');
    }
  });

});
