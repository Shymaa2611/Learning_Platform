const aboutBtn=document.querySelector(".about");
const detailsBtn=document.querySelector(".details");
const challengesBtn=document.querySelector(".challeges");
const contactInfo=document.querySelector(".contact_Info");
const detailsInfo=document.querySelector(".details-Info");
const challengesInfo=document.querySelector(".challenges-Info");

aboutBtn.addEventListener("click",()=>{
    detailsInfo.classList.add("hiddenClass");
     detailsBtn.classList.remove("active");
    challengesInfo.classList.add("hiddenClass");
      challengesBtn.classList.remove("active");
    contactInfo.classList.remove("hiddenClass");
    aboutBtn.classList.add("active");
});
detailsBtn.addEventListener("click",()=>{
   contactInfo.classList.add("hiddenClass");
   aboutBtn.classList.remove("active");
    challengesInfo.classList.add("hiddenClass");
   challengesBtn.classList.remove("active");
     detailsInfo.classList.remove("hiddenClass");
     detailsBtn.classList.add("active");
});
challengesBtn.addEventListener("click",()=>{
   contactInfo.classList.add("hiddenClass");
    aboutBtn.classList.remove("active");
   detailsInfo.classList.add("hiddenClass");
    detailsBtn.classList.remove("active");
     challengesInfo.classList.remove("hiddenClass");
       challengesBtn.classList.add("active");
});

