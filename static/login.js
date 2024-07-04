// Selecting the form element
const signInForm = document.getElementById('signInForm');

// Adding submit event listener
signInForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Getting form values
    const email = signInForm.elements['email'].value;
    const password = signInForm.elements['password'].value;

    // Retrieving user object from localStorage
    const savedUser = JSON.parse(localStorage.getItem('user'));

    // Check if user exists and credentials match
    if (savedUser && savedUser.email === email && savedUser.password === password) {
        alert('Login successful!'); // Replace with your desired login success behavior

        // Redirect to home page after login
        window.location.href = 'templates\index.html'; // Replace with your home page URL
    } else {
        alert('Invalid email or password');
    }

    // Clear the form inputs
    signInForm.reset();
});
