var login_p = document.getElementById("user_password");

// Execute a function when the user releases a key on the keyboard
login_p.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    validateLogin()
  }
});


function post(params, form_name) {

  const form = document.createElement('form');
  form.method = 'POST';
  form.action = window.location.href;

  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const hiddenField = document.createElement('input');
      hiddenField.type = 'hidden';
      hiddenField.name = key;
      hiddenField.value = params[key];

      form.appendChild(hiddenField);
    }
  }
  const hiddenField = document.createElement('input');
  hiddenField.type = 'hidden';
  hiddenField.name = form_name;
  form.appendChild(hiddenField);
  
  document.body.appendChild(form);
  form.submit();
}


function isNumeric(value)
{
	return /^\d+$/.test(value);
}

function isOnlyAlphabetical(value)
{
	return /[^a-z]/i.test(value);
}


function validateLogin()
{
    let id = document.getElementById("employee_id").value;
    let password = document.getElementById("user_password").value;

    document.getElementById("id_error").style.display = "none";
    document.getElementById("password_error").style.display = "none";
	// if isNumeric returns true, proceed with POST request, otherwise, display error message
    if (!isNumeric(id)){
        if (password == ""){
            document.getElementById("id_error").style.display = "";
            document.getElementById("password_error").style.display = "";
            document.getElementById("password_error").style.visibility = "visible";
            document.getElementById("id_error").style.visibility = "visible";
        }
        else{
            document.getElementById("id_error").style.display = "";
            document.getElementById("id_error").style.visibility = "visible";
        }
    }
    else if (password == ""){
        document.getElementById("password_error").style.display = "";
        document.getElementById("password_error").style.visibility = "visible";

    }
    else{
        payload = {employee_id : id, user_password : password};
        post(payload, 'login_click');
	}
}



