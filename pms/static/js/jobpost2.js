const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');

sideLinks.forEach(item => {
    const li = item.parentElement;
    item.addEventListener('click', () => {
        sideLinks.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});

const menuBar = document.querySelector('.content nav .bx.bx-menu');
const sideBar = document.querySelector('.sidebar');

menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
});

const searchBtn = document.querySelector('.content nav form .form-input button');
const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
const searchForm = document.querySelector('.content nav form');

searchBtn.addEventListener('click', function (e) {
    if (window.innerWidth < 576) {
        e.preventDefault;
        searchForm.classList.toggle('show');
        if (searchForm.classList.contains('show')) {
            searchBtnIcon.classList.replace('bx-search', 'bx-x');
        } else {
            searchBtnIcon.classList.replace('bx-x', 'bx-search');
        }
    }
});

window.addEventListener('resize', () => {
    if (window.innerWidth < 768) {
        sideBar.classList.add('close');
    } else {
        sideBar.classList.remove('close');
    }
    if (window.innerWidth > 576) {
        searchBtnIcon.classList.replace('bx-x', 'bx-search');
        searchForm.classList.remove('show');
    }
});

const toggler = document.getElementById('theme-toggle');

function toggleStyles() {
    var oldStylesLink = document.querySelector('#old');
    var newStylesLink = document.querySelector('#new-styles');
    
    if (oldStylesLink.disabled) {
        oldStylesLink.disabled = false;
        newStylesLink.disabled = true;
    } else {
        oldStylesLink.disabled = true;
        newStylesLink.disabled = false;
    }
}
const lable = document.querySelector("#label")
const date = document.querySelector("#date-time");
const title = document.querySelector(".login__title");
toggler.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark');
        toggleStyles();
        title.style.color="white"
        date.style.color="white"
        lable.style.color="white"
    } else {
        document.body.classList.remove('dark');
        toggleStyles();
        title.style.color="black"
        date.style.color="black"
        lable.style.color="black"
    }
});