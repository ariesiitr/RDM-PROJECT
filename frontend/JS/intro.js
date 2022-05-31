let sliderSent = document.querySelector(".bgSlider");
let images = document.querySelectorAll(".img");

images.forEach((e)=>
{
    e.addEventListener("mouseenter", ()=>
    {
        e.classList.add("zoom");
        sliderSent.classList.add("whenSliding");
        sliderSent.classList.remove("pBgSlider");
        sliderSent.style.cssText += "font-size: 70px; font-weight: 900";

    })
    e.addEventListener("mouseout", ()=>
    {
        e.classList.remove("zoom");
        document.querySelector(".slide").scrollRight +=800;
    })

})


document.querySelector("#slide1").addEventListener("click", () =>
{
    sliderSent.classList.add("pBgSlider");
    sliderSent.classList.remove("whenSliding");
    sliderSent.style.cssText += "font-size: 50px; font-weight: 500;";

})

document.querySelector("#img1").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "600px";
})
document.querySelector("#img2").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "500px";
})
document.querySelector("#img3").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "400px";
})
document.querySelector("#img4").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "200px";
})
document.querySelector("#img5").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "0px";
})
document.querySelector("#img6").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "-200px";
})
document.querySelector("#img7").addEventListener("mouseenter", () =>
{
    document.querySelector(".slider").style.marginLeft = "-500px";
})


