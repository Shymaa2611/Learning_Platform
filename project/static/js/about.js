const changeMode=document.querySelector('.iconLight');
const mode=document.querySelector('.about-left');
const secondDiv=document.querySelector('.about-left-content');
const icons=document.querySelector('.icons');
const spanClass=document.querySelector('.spanClass');
changeMode.addEventListener('click',()=>{
    mode.classList.toggle('about-left-active');
// mode.classList.remove();
  secondDiv.classList.toggle('about-left-content-active');
  icons.classList.toggle('icons-active')
  spanClass.classList.toggle('spanClass-active')


})