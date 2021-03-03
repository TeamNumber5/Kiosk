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


var create_p = document.getElementById("cuser_password");

// Execute a function when the user releases a key on the keyboard
create_p.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    validateCreateAccount(); 
  }
});




function gotoCreateAccount()
{
    document.getElementById("login").style.visibility = "hidden";
    document.getElementById("createUser").style.visibility = "visible";

    document.getElementById("id_error").style.display = "none";
    document.getElementById("password_error").style.display = "none";
    document.getElementById("login_error").style.display = "none";
    document.getElementById("login_error").style.visibility = "hidden";
}

function gotoLogin()
{
    document.getElementById("createUser").style.visibility = "hidden";
    document.getElementById("login").style.visibility = "visible";
}

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
        document.getElementById("password_error").style.visibility = "visible"

    }
    else{
        payload = {employee_id : id, user_password : password};
        post(payload, 'login_click');
	}
}

function validateCreateAccount()
{
	let id = document.getElementById("cemployee_id").value;
	let password = document.getElementById("cuser_password").value;
	let firstName = document.getElementById("cfirst_name").value;
	let lastName = document.getElementById("clast_name").value;
	let role = document.getElementById("crole").value;

	document.getElementById("uid_error").style.display = "none";
	document.getElementById("role_error").style.display = "none";
	if(!isNumeric(id))
	{
			//console.log(document.getElementById("employee_id").value);
			document.getElementById("uid_error").style.display = "";
			document.getElementById("uid_error").style.visibility = "visible";
	}
	else if(!(role == "GM" || role == "CS" || role == "SM"))
	{
			document.getElementById("role_error").style.display = "";
			document.getElementById("role_error").style.visibility = "visibile";
	}
	else{
		console.log("payload");
		payload = {employee_id : id, user_password : password, first_name : firstName, last_name : lastName, role : role};
		post(payload, 'create_click');
	}
	
}

function init(no_users, valid_info){
    if (no_users == 1){
        gotoCreateAccount();
    }
    else if (valid_info == 0){
        gotoCreateAccount();
    }
    else{
        gotoLogin();
    }
}


