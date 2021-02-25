
document.addEventListener('DOMContentLoaded', clickHandling);


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



function clickHandling() {
    document.getElementById("startTransaction").addEventListener('click', displayError);
    document.getElementById("viewProducts").addEventListener('click', () => { window.location.assign("/productListing"); });
    document.getElementById("createEmployee").addEventListener('click', () => { window.location.assign("/employeeDetail"); });
    document.getElementById("salesReport").addEventListener('click', displayError);
    document.getElementById("cashierReport").addEventListener('click', displayError);
}

function displayError() {
    alert("Functionality has not been implemented yet.");
}

function logout_click(){
    params = {}

    post(params, 'logout_click')

}



