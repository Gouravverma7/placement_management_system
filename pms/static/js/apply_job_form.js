var darkmode = document.querySelector(".mode-switch");
var head = document.querySelector(".apply-form-header-element");
var headtext = document.querySelector(".apply-form-header-element p");
var cvtext= document.querySelector(".cv-box");
var forms = document.querySelectorAll(".apply-form-group");
var texts = document.querySelectorAll(".apply-form-group-txt");

darkmode.addEventListener("click", () => {
    forms.forEach(form => {
        if (form.style.backgroundColor === "white" || form.style.backgroundColor === "") {
            form.style.backgroundColor = "rgb(17, 24, 39)";
        } else {
            form.style.backgroundColor = "white";
        }
    });

    texts.forEach(text => {
        if (text.style.color === "black" || text.style.color === "") {
            text.style.color = "white";
        } else {
            text.style.color = "black";
        }
    });

    if (cvtext.style.color === "black" || cvtext.style.color === "") {
        cvtext.style.color = "white";
    } else {
        cvtext.style.color = "black";
    }

    if (head.style.backgroundColor === "black" || head.style.backgroundColor === "") {
        head.style.backgroundColor = "rgb(17, 24, 39)";
    } else {
        head.style.backgroundColor = "";
    }

    if (headtext.style.color === "black" || headtext.style.color === "") {
        headtext.style.color = "white";
    } else {
        headtext.style.color = "black";
    }


});

