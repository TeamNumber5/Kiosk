
/*
 * Event listener for hitting enter on password
 */
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



/*
 * After Create user post request, this loads  the page
 * with the proper error messages if there were some.
 */
function init(v, u, c){
    if (v == 0 && u == 1){
        document.getElementById("man_error").style.display="";
        document.getElementById("man_error").style.visibility = "visible"; 
    }
    else if (v == 0){
        document.getElementById("unique").style.display="";
        document.getElementById("unique").style.visibility = "visible";
    }
    else if (c == 1){
        document.getElementById("cuser").style.display="";
        document.getElementById("cuser").style.visibility = "visible";

    }
}



/*
 * Post request creates a hidden form in the html
 * and submits a form rather than doing ajax.
 */
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


/*
 * Client side error checking of create user form.
 */
function validateCreateAccount()
{
	let firstName = document.getElementById("cfirst_name").value;
	let lastName = document.getElementById("clast_name").value;
	let id = document.getElementById("cemployee_id").value;
	let role = document.getElementById("crole").value;
	let password = document.getElementById("cuser_password").value;

    let error = false;


	document.getElementById("fname_error").style.display = "none";
	document.getElementById("fname_alpha").style.display = "none";
	document.getElementById("lname_alpha").style.display = "none";
	document.getElementById("lname_error").style.display = "none";
	document.getElementById("uid_error").style.display = "none";
	document.getElementById("cid_error").style.display = "none";
	document.getElementById("crole_error").style.display = "none";
	document.getElementById("cpassword_error").style.display = "none";
	if(firstName === ""){
		document.getElementById("fname_error").style.display = "";
		document.getElementById("fname_error").style.visibility = "visible";
        error = true;
	}
    else if(isOnlyAlphabetical(firstName)){
			document.getElementById("fname_alpha").style.display = "";
			document.getElementById("fname_alpha").style.visibility = "visible";
        error = true;
	}
	if (lastName === ""){
		document.getElementById("lname_error").style.display = "";
		document.getElementById("lname_error").style.visibility = "visible";
        error = true;
	}
    else if(isOnlyAlphabetical(lastName)){
		document.getElementById("lname_alpha").style.display = "";
		document.getElementById("lname_alpha").style.visibility = "visible";
        error = true;
	}
	if(!isNumeric(id)){
		document.getElementById("uid_error").style.display = "";
		document.getElementById("uid_error").style.visibility = "visible";
        error = true;
	}
    else if(!(id.length ==5)){
		document.getElementById("cid_error").style.display = "";
		document.getElementById("cid_error").style.visibility = "visible";
        error = true;
	}		
	if(!(role === "GM" || role === "CS" || role === "SM")){
			document.getElementById("crole_error").style.display = "";
			document.getElementById("crole_error").style.visibility = "visible";
        error = true;
	}
	if(password === ""){
			document.getElementById("cpassword_error").style.display = "";
			document.getElementById("cpassword_error").style.visibility = "visible";
        error = true;
	}
	if (!error){
		payload = {employee_id : id, user_password : password, first_name : firstName, last_name : lastName, role : role};
		post(payload, 'create_click');
	}
	
}

/*
 * Function for returning the user to the menu 
 */

function back(){
    params = {}
    post(params, 'back')

}



