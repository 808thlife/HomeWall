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
let delete_alert = document.querySelector(".alert-danger")
//Alert won't be shown until user clicks a button
delete_alert.style.display = "none"
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
            "role":role,
        })
    })
    .then(response => {
        if (response.status === 400) {
            console.log("errro")
        } else if (!response.ok) {
          // Handle other non-200 status code errors
          throw new Error('Fetch error: ' + response.status);
        }
            else if(response.ok){
                const users_table = document.querySelector("#user-table")
                document.querySelector("#close-modal-button").click();
                alert.style.display = "block";
                window.onload = setTimeout(function(){
                   alert.style.display = "none";
                }, 4000);
                let new_user_element = document.createElement("tr")
                new_user_element.innerHTML +=`
                <tr>
                <th scope="row">${document.querySelector("table").rows.length}</th>
                <td>${username}</td>
                <td>${role}</td>
                <td>Traffic</td>
                <td>None</td>
                <td><button class = "btn btn-info"><i class="bi bi-pencil"></i></button></td>
                <td><button class = "btn btn-danger delete-user"><i class="bi bi-trash"></i></button></td>
                </tr>
              `
                users_table.append(new_user_element);
            }
        return response.json();
      })
      .then(data =>{
        let request_error = data["error"]
        const error_field = document.querySelector("#unique-user-error")
        error_field.innerHTML = request_error
        //unique-user-error
      })

});


//Deleting user API

let delete_buttons = document.querySelectorAll(".delete-user");
delete_buttons.forEach((button) => {
  button.addEventListener("click", (e) => {
    let t_row = e.target.parentElement.parentElement;
    id = t_row.children[0].innerHTML
    fetch(`/api/${id}`,{
        method:"DELETE",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json",
          },
        body: JSON.stringify({
            "id": id
        })
    })
    .then(response => {
      if (response.status === 403) {
          console.log("error")
      } else if (!response.ok) {
        // Handle other non-200 status code errors
        throw new Error('Fetch error: ' + response.status);
      }
          else if(response.ok){
            delete_alert.style.display = "block";
            window.onload = setTimeout(function(){
              delete_alert.style.display = "none";
           }, 4000);
           t_row.remove();
          }
      return response.json();
    })
  });
});
