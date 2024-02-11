const nacl = require('tweetnacl')
nacl.util = require('tweetnacl-util')

document.getElementById("submit").addEventListener("click", (e) => {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let password = document.getElementById("password").value;
    let email = document.getElementById("email").value;
    let gender = document.getElementById("gender").value;

    let userInfo = {
        "name": name,
        "email": email,
        "gender": gender,
        "password": password,
    };

    console.log(userInfo);

    const csrfToken = getCookie('csrftoken');

    fetch('register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  
        },
        body: JSON.stringify(userInfo)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Réponse du serveur: ${response.status}`);
        }
        console.log('Réponse du serveur:', response);
        return response.json();
    })
    .then(data => {
        console.log('Données de la réponse:', data);
    })
    .catch(error => {
        console.error('Erreur lors de la requête:', error);
    });
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
