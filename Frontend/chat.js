const form = document.querySelector('form')
const submit_btn = document.querySelector('#submit-btn')

submit_btn.addEventListener('click', async(e)=>{
    e.preventDefault();
    const prompt = document.querySelector("#prompt").value
    // alert(prompt)

    const response = await fetch("http://127.0.0.1:8000/events", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            prompt: prompt
        }),
    })
    const result = await response.json()

    const prompt_response = document.getElementById("response")
    prompt_response.innerHTML = result.message

    // alert(result.message)
})

const token = localStorage.getItem("token")

const auth = await fetch("http://127.0.0.1:8000/events/uses/me", {
    method: "GET",
    headers: {
        "Accept": "application/json",
        "Authorization": "Bearer " + token
    }
})

if (auth.ok) {
    const userdata = await auth.json()
    alert("welocome" + userdata.username)
}

else{
    alert("unauthorized")
    window.location.href = "login.html"
}