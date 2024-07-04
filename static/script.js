function signUp() {
    const name = $('#name').val();
    const email = $('#email').val();
    const password = $('#password').val();
    const phone_number = $('#phone_number').val();
    const gender = $('#gender').val();

    $.ajax({
        url: '/register',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({name: name, email: email, password: password, phone_number: phone_number, gender: gender}),
        success: function(response) {
            alert(response.message);
        }
    });
}

function signIn() {
    const email = $('#login_email').val();
    const password = $('#login_password').val();

    $.ajax({
        url: '/login',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({email: email, password: password}),
        success: function(response) {
            alert(response.message);
        },
        error: function(response) {
            alert(response.responseJSON.message);
        }
    });
}
