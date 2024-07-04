// Selecting the form element
const signUpForm = document.getElementById('signUpForm');

// Adding submit event listener
signUpForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Getting form values
    const name = signUpForm.elements['name'].value;
    const email = signUpForm.elements['email'].value;
    const password = signUpForm.elements['password'].value;
    const phone = signUpForm.elements['phone'].value;
    const gender = signUpForm.elements['gender'].value;

    // Creating user object
    const user = {
        name: name,
        email: email,
        password: password,
        phone: phone,
        gender: gender
    };

    // Save user object to localStorage
    localStorage.setItem('user', JSON.stringify(user));

    // Optionally, you can redirect to another page after successful registration
    // window.location.href = '/success'; // Replace with your success page

    // Clear the form inputs
    signUpForm.reset();
});
