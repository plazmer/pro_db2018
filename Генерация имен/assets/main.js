function getUser(){
    let userPromise = fetch('http://localhost:8080/user');
    userPromise
        .then(
        (response)=> {return response.json()}
        )
        .then(function (user){displayUser(user)});
}

function displayUser (user) {
    for (let key in user){
        document.querySelector(`#${key}`).innerHTML = user[key];
    }
}

setInterval(getUser, 500);