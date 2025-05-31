function login() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    if (username && password) {
        alert('Login Successful!');
    } else {
        alert('Please enter username and password.');
    }
}

function searchHouse() {
    let searchInput = document.getElementById('searchInput').value;
    
    if (searchInput) {
        document.getElementById('searchResults').innerHTML = `<p>Showing results for: <strong>${searchInput}</strong></p>`;
    } else {
        document.getElementById('searchResults').innerHTML = '<p>Please enter a search term.</p>';
    }
}
