// alert("yaar")

const signup_btn = document.querySelector("#signup-btn")
const username = document.getElementById('username')
const password = document.getElementById('password')
const email = document.getElementById('email')
const full_name = document.getElementById('full_name')
const conf_password = document.getElementById('confirm-password')

async function sendData() {
    const user_data = {
        username: username.value,
        email: email.value,
        full_name: full_name.value,
        password: password.value
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/userdb/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
                // "Content-Type": "application/x-www-form-urlencoded",
            },
            body: JSON.stringify(user_data),
        });
        // const token = await response.json()

        if (response.ok) {
            // localStorage.setItem("token", token.access_token)
            // alert("redirecting")
            window.location.href = "login.html"
        }
        else{
            alert("error")
        }
    }
    catch (e) {
        console.error(e);
    }
}

signup_btn.addEventListener('click', (e) => {
    e.preventDefault()
    if (password.value != conf_password.value) {
        alert("check password carefully")
    }
    else {
        sendData()
    }
})
