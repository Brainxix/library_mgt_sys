// ===============================
// Mobile Navigation
// ===============================

const menuToggle = document.getElementById("menu-toggle");
const navbar = document.getElementById("navbar");

menuToggle.addEventListener("click", () => {

    navbar.classList.toggle("active");

    const icon = menuToggle.querySelector("i");

    if(navbar.classList.contains("active")){

        icon.classList.remove("fa-bars");
        icon.classList.add("fa-xmark");

    }else{

        icon.classList.remove("fa-xmark");
        icon.classList.add("fa-bars");

    }

});

// Close menu after clicking a link

document.querySelectorAll("#navbar a").forEach(link=>{

    link.addEventListener("click",()=>{

        navbar.classList.remove("active");

        menuToggle.querySelector("i").classList.remove("fa-xmark");

        menuToggle.querySelector("i").classList.add("fa-bars");

    });

});


// ===============================
// Smooth Scroll
// ===============================

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        const target=document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({

                behavior:"smooth"

            });

        }

    });

});


// ===============================
// Reveal Animation
// ===============================

const reveals=document.querySelectorAll("section");

window.addEventListener("scroll",()=>{

    reveals.forEach(section=>{

        const top=section.getBoundingClientRect().top;

        const visible=window.innerHeight-120;

        if(top<visible){

            section.classList.add("show");

        }

    });

});