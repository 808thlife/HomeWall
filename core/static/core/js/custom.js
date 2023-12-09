function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//Creating user API
const add_user_button = document.querySelector("#add-user-button");
let alert = document.querySelector("#add-user-success")
//Alert won't be shown until user clicks a button
alert.style.display = "none";
// listents to save button
add_user_button.addEventListener("click", (event)=>{
    let username = document.querySelector("#add-username").value;
    let role = document.querySelector("#add-role-option").value;
    fetch("/api/", {
        method:"POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json",
          },
        body: JSON.stringify({
            "username": username,
            "role":role
        })
    })
    .then(response => {
        if (response.status === 400) {
          // Handle 400 error
          return response.json().then(errorData => {
            // Use error data to display specific error message
            console.error(errorData.message);
          });
        } else if (!response.ok) {
          // Handle other non-200 status code errors
          throw new Error('Fetch error: ' + response.status);
        }
            else if(response.ok){
                document.querySelector("#close-modal-button").click();
                alert.style.display = "block";
                window.onload = setTimeout(function(){
                   alert.style.display = "none";
                }, 4000);
            }
        return response.json();
      })
      .then(data => {
        // Process data
      })
      .catch(error => {
        // Handle generic errors
        console.error(error);
      });
});