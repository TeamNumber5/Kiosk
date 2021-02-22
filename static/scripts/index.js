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


