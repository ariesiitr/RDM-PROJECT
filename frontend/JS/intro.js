let slider = document.querySelectorAll(".slide");
let sliderSent = document.querySelector("#bgSlider");
slider.forEach((e) =>
{
    e.addEventListener("click", ()=>
    {
        sliderSent.classList.add("whenSliding");
        sliderSent.classList.remove("pBgSlider");
        sliderSent.style.cssText += "font-size: 70px; font-weight: 900";
        document.querySelector(".slider").style.cssText += "scroll-padding-top:500px ";
    })
})

document.querySelector("#slide1").addEventListener("click", () =>
{
    sliderSent.classList.add("pBgSlider");
    sliderSent.classList.remove("whenSliding");
    sliderSent.style.cssText += "font-size: 50px; font-weight: 500;";

})
