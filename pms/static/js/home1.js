// locomotive start
gsap.registerPlugin(ScrollTrigger);

// Using Locomotive Scroll from Locomotive https://github.com/locomotivemtl/locomotive-scroll

const locoScroll = new LocomotiveScroll({
  el: document.querySelector("#wrapper"),
  smooth: true
});
// each time Locomotive Scroll updates, tell ScrollTrigger to update too (sync positioning)
locoScroll.on("scroll", ScrollTrigger.update);

// tell ScrollTrigger to use these proxy methods for the "#main" element since Locomotive Scroll is hijacking things
ScrollTrigger.scrollerProxy("#wrapper", {
  scrollTop(value) {
    return arguments.length ? locoScroll.scrollTo(value, 0, 0) : locoScroll.scroll.instance.scroll.y;
  }, // we don't have to define a scrollLeft because we're only scrolling vertically.
  getBoundingClientRect() {
    return {top: 0, left: 0, width: window.innerWidth, height: window.innerHeight};
  },
  // LocomotiveScroll handles things completely differently on mobile devices - it doesn't even transform the container at all! So to get the correct behavior and avoid jitters, we should pin things with position: fixed on mobile. We sense it by checking to see if there's a transform applied to the container (the LocomotiveScroll-controlled element).
  pinType: document.querySelector("#wrapper").style.transform ? "transform" : "fixed"
});

// each time the window updates, we should refresh ScrollTrigger and then update LocomotiveScroll. 
ScrollTrigger.addEventListener("refresh", () => locoScroll.update());

// after everything is set up, refresh() ScrollTrigger and update LocomotiveScroll because padding may have been added for pinning, etc.
ScrollTrigger.refresh();


// locomotive end

// scroll script


// scroll script end


let isLoggedIn = false; 

const userProfileLink = document.querySelector('#user-profile');
const loginLink = document.querySelector('#login');
const signupLink = document.querySelector('#register');

if (isLoggedIn) {
    userProfileLink.style.display = 'block';
    loginLink.style.display = 'none';
    signupLink.style.display = 'none';
}

const homeLink = document.getElementById('home');
homeLink.addEventListener('click', () => {
    window.location.href = '#';
});

// sidebar 

let sideBar = document.querySelector("#side-menu")
let btn = document.querySelector("#button")
btn.addEventListener("click",()=>{
  if(sideBar.style.display !== "flex"){
    sideBar.style.display = "flex"
    // btn.style.marginRight = "300px"
    btn.style.zIndex = "2"
    btn.style.color = "black"
}
else{
    sideBar.style.display = "none"
    btn.style.marginRight = "25px"
    btn.style.color = "white"
  }
  
})