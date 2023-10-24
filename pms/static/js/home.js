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
    btn.style.marginRight = "300px"
  }
  else{
    sideBar.style.display = "none"
    btn.style.marginRight = "25px"
  }
  
})