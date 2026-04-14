const login_form = document.getElementById('login-form')
const login_btn = document.getElementById('login-btn')
const username = document.getElementById('username')
const password = document.getElementById('password')


async function sendData() {
    const params = new URLSearchParams()
    params.append("username", username.value);
    params.append("password", password.value)

    try {
        const response = await fetch("http://127.0.0.1:8000/token", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: params,
        });
        const token = await response.json()

        if (response.ok) {
            localStorage.setItem("token", token.access_token)
            alert("redirecting")
            window.location.href = "chat.html"
        }
        else{
            alert("oops")
        }
    }
    catch (e) {
        console.error(e);
    }
}

console.log(login_btn)
login_btn.addEventListener('click', (e) => {
    alert("skdfj ");
    e.preventDefault()
    alert("hii")
    sendData()
})

