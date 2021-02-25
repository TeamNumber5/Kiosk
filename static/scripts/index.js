function gotoCreateAccount()
{
    document.getElementById("login").style.visibility = "hidden";
    document.getElementById("createUser").style.visibility = "visible";
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
            document.getElementById("id_error").style.visibility = "visible"
            document.getElementById("password_error").style.visibility = "visible"
        }
        else{
            document.getElementById("id_error").style.display = "";
            document.getElementById("id_error").style.visibility = "visible"
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



function validateForm()
{
//This method will validate the entries of the form -> allow for the restriction of different fields
//This method by definition will be false although validForm is initialized to true --> the do loop will catch the required fields
//CURRENTLY WORK IN PROGRESS, experimenting between using "onclick" metho and "onsubmit" method for this particular problem
    var validForm = true;
    do{

    if(document.getElementById("role") == "GM")
    {
        validForm = false;
    }
    else if(document.getElementById("employee_id") == "")
    {
        validForm = false;
    }
    }
    while(!validForm)

}


function init(no_users, valid_info){
    if (valid_info == 0 ){
        gotoCreateAccount();
    }
    else if (no_users == 1){
        gotoCreateAccount();
    }
    else{
        gotoLogin();
    }
}


