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

function isNumeric(value)
{
	return /^\d+$/.test(value);
}


function validateLogin()
{
	// if isNumeric returns true, proceed with POST request, otherwise, display error message
	if(isNumeric(document.getElementById("employee_id").value))
	{
        let id = document.getElementById("employee_id").value;
        let password = document.getElementById("user_password").value;
        
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = window.location.href;

        let hiddenField_one = document.createElement('input');
        hiddenField_one.type = 'hidden';
        hiddenField_one.name = 'employee_id';
        hiddenField_one.value = id;
        form.appendChild(hiddenField_one);

        let hiddenField_two = document.createElement('input');
        hiddenField_two.type = 'hidden'; 
        hiddenField_two.name = 'user_password';
        hiddenField_two.value = password;
        form.appendChild(hiddenField_two);

        let hiddenField_three = document.createElement('input');
        hiddenField_three.name = 'login_click';
        form.appendChild(hiddenField_three);

        document.body.appendChild(form);
        form.submit();	
	}
    else {
        alert('Bad Login');
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


