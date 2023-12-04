document.addEventListener("DOMContentLoaded", function () {
    var modeSwitch = document.querySelector(".mode-switch");
  
    modeSwitch.addEventListener("click", function () {
      document.documentElement.classList.toggle("dark");
      modeSwitch.classList.toggle("active");
    });
  });
  
// style sheet change dark light
var toggler = document.querySelector('.mode-switch');

function toggleStyles() {
    var oldStylesLink = document.querySelector('#old');
    var newStylesLink = document.querySelector('#new');
    
    if (oldStylesLink.disabled) {
        oldStylesLink.disabled = false;
        newStylesLink.disabled = true;
    } else {
        oldStylesLink.disabled = true;
        newStylesLink.disabled = false;
    }
    console.log('abcd');
}

toggler.addEventListener('click', function () {
    if (this.checked) {
        // document.body.classList.add('dark');
        toggleStyles();
    } else {
        // document.body.classList.remove('dark');
        toggleStyles();
    }
});

