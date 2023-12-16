function callAlert(alert){
  alert.style.display = "block";
  window.onload = setTimeout(function(){
    alert.style.display = "none";
 }, 4000);
}



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

const error_field = document.querySelector("#unique-user-error")
error_field.style.display = "none";
//Creating user API
const add_user_button = document.querySelector("#add-user-button");
let alert = document.querySelector("#add-user-success")
const edit_alert = document.querySelector("#edit-user-success");
let delete_alert = document.querySelector(".alert-danger")
const errorAlert = document.querySelector("#error-alert");
//Alert won't be shown until user clicks a button
errorAlert.style.display = "none";
delete_alert.style.display = "none";
alert.style.display = "none";
edit_alert.style.display = "none";
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
          console.log('error')
        } else if (!response.ok) {
          
          console.log("error")
        }
            else if(response.ok){
                const users_table = document.querySelector("#user-table")
                //document.querySelector("#close-add-modal-button").click();
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
        if (request_error != undefined){
          let error_alert = document.querySelector("#error-p")
          error_field.style.display = "block"
          errorAlert.style.display = "block"
          error_field.innerHTML = request_error
  
          error_alert.innerHTML = request_error
  
          window.onload = setTimeout(function(){
            errorAlert.style.display = "none";
            error_field.style.display = "none";
         }, 4000);
        }
        
       
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
        callAlert(errorAlert);
      } else if (!response.ok) {
        callAlert(errorAlert);
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



//UPDATE USER INFORMATION API




const edit_buttons = document.querySelectorAll(".edit-user");
const edit_saves = document.querySelector("#edit-user-button");

edit_buttons.forEach((button)=>{
  button.addEventListener("click", (e)=>{
    let t_row = e.target.parentElement.parentElement
    id = t_row.children[0].innerHTML
    username = t_row.children[1].innerHTML
    userRole = t_row.children[2].innerHTML

    document.querySelector("#edit-username").value = username
    
    const selectElement = document.getElementById("edit-role-option");
    
    // Loop through options and set the 'selected' attribute for the matching role
    for (let i = 0; i < selectElement.options.length; i++) {
        if (selectElement.options[i].value === userRole) {
            selectElement.options[i].selected = true;
            break;
        }
    }

    edit_saves.addEventListener("click", ()=>{
      fetch(`/api/${id}`, {
        method:"PUT",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "id":id,
          "username":document.querySelector("#edit-username").value,
          "role":document.querySelector("#edit-role-option").value
        })
      })
      .then(response => {
        if (response.status === 403) {
          
        } else if (!response.ok) {
          // Handle other non-200 status code errors
          
          
        }
            else if(response.ok){
              edit_alert.style.display = "block"

            window.onload = setTimeout(function(){
              edit_alert.style.display = "none";
           }, 4000);
     
              t_row.children[1].innerHTML = document.querySelector("#edit-username").value
              t_row.children[2].innerHTML = document.querySelector("#edit-role-option").value
            }
        return response.json();
      })

      .then(data =>{
        let request_error = data["error"]
        if (request_error != undefined){
          let error_alert = document.querySelector("#error-p")
          error_field.style.display = "block"
          errorAlert.style.display = "block"
          error_field.innerHTML = request_error
  
          error_alert.innerHTML = request_error
  
          window.onload = setTimeout(function(){
            errorAlert.style.display = "none";
            error_field.style.display = "none";
         }, 4000);
        }
        
       
        //unique-user-error
      })
    })
  })
})
