document.getElementById("registration-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });
    console.log(data);
    // You can send the form data to your server for processing here.
  });