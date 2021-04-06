
document.addEventListener('DOMContentLoaded', () =>  {

	 document.getElementById("createNewButton").addEventListener('click', () => { params = {}; name='go_create_new'; post(params, name);});
});

function post(params, form_name) {

  const form = document.createElement('form');
  form.method = 'POST';
  form.action = window.location.href;
  form.enctype= "multipart/form-data";

  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const hiddenField = document.createElement('input');
      hiddenField.type = 'hidden';
      hiddenField.name = key;
      if (key == "product_img"){
        hiddenField.type="file";
        hiddenField.files = params[key];
      }
      else{
      hiddenField.value = params[key];
      }

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
    let img = document.getElementById("img").files;
    let error = false;

    
	document.getElementById("name_error").style.display = "none";
	document.getElementById("desc_error").style.display = "none";
	document.getElementById("price_error").style.display = "none";
	document.getElementById("qavail_error").style.display = "none";
	if(name === ""){
		document.getElementById("name_error").style.display = "";
		document.getElementById("name_error").style.visibility = "visible";
        error = true;
    }
    if(desc === ""){
		document.getElementById("desc_error").style.display = "";
		document.getElementById("desc_error").style.visibility = "visible";
        error = true;
    }
    if(!(isDollar(price))){
		document.getElementById("price_error").style.display = "";
		document.getElementById("price_error").style.visibility = "visible";
        error = true;
    }
    if(!(isNumeric(qavail))){
		document.getElementById("qavail_error").style.display = "";
		document.getElementById("qavail_error").style.visibility = "visible";
        error = true;
    }
    if (img.length != 0 && !error){
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
