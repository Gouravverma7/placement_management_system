// Custom select 
let customSelects = document.querySelectorAll('.hex-select-js');

customSelects.forEach((element) => {
  const originalSelect = element.querySelector('select');
  const newSelect = document.createElement('div');
  newSelect.className = "custom-select";
  newSelect.innerHTML = '<span>' + originalSelect.options[0].text + '</span>';
  
  const optionsList = document.createElement('ul');
  optionsList.className = 'select-options';
  newSelect.appendChild(optionsList);
  
  for (i = 0; i < originalSelect.options.length; ++i) {
    const option = document.createElement('li');
    let optionText = originalSelect.options[i].text,
        optionValue = originalSelect.options[i].value;
    option.className = 'option-item';
    option.innerHTML = optionText;
    option.dataset.optionValue = optionValue;
    optionsList.appendChild(option);
    
    let event = new Event('change');
}
  
  let checkPosition = function (event) {
    const rect = element.getBoundingClientRect();
    const spaceAbove = rect.top;
    const spaceBelow = window.innerHeight - rect.bottom;
    
    if (spaceAbove < spaceBelow) {
      optionsList.style.top = '100%';
      optionsList.style.bottom = 'auto';
      optionsList.style.flexDirection = 'column';
    } else {
      optionsList.style.top = 'auto';
      optionsList.style.bottom = '100%';
      optionsList.style.flexDirection = 'column-reverse';
    }
  };
  
  newSelect.addEventListener('click', checkPosition, false);
  newSelect.addEventListener('mouseover', checkPosition, false);
});

// dshdhsaoifhsa
