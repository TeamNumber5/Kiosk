

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
function isDollar(value)
{
	return /^\d+(?:\.\d{0,2})$/.test(value);
}

function isNumeric(value)
{
	return /^\d+$/.test(value);
}

function validateCreateProduct(){
    let name = document.getElementById("name").value;
    let desc = document.getElementById("desc").value;
    let price = document.getElementById("price").value;
    let qavail = document.getElementById("qavail").value;
    let img = document.getElementById("img").value;
    let error = false;

    
	if(name === ""){
        console.log('name empty');
        error = true;
    }
    else if(desc === ""){
        console.log('desc empty');
        error = true;
    }
    else if(!(isDollar(price))){
        console.log('not dollar');
        error = true;
    }
    else if(!(isNumeric(qavail))){
        console.log('not int');
        error = true;
    }
    if (img != null && !error){
        params = {product_name : name, product_desc : desc, product_price : price, product_qavail : qavail, product_img : img};
        post(params, "create_product");
    }
    else if (!error){
        params = {product_name : name, product_desc : desc, product_price : price, product_qavail : qavail};
        post(params, "create_product");
    }
}

function logout_click(){
    params = {};
    post(params, 'logout_click');

}
