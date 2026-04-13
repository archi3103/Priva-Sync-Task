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
    if (prompt_response) {
        prompt_response.innerHTML = result.message

    }
    else{
        console.error("oops")
    }

    alert(result.message)
})