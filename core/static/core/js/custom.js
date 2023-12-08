//Creating user API
const add_user_button = document.querySelector("#add-user-button");
// listents to save button
add_user_button.addEventListener("click", (event)=>{
    let username = document.querySelector("#add-username");
    let role = document.querySelector("#add-role-option");
    fetch("/api/", {
        method:"POST",
        headers: {
            "Content-Type": "application/json",
          },
        body: JSON.stringify({
            "username": username,
            "role":role
        })
    })
});