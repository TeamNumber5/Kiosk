
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

    if (!error){
        if (document.getElementById("Submit").innerHTML === "Update"){
            params = {product_id : document.getElementById("Submit").value, product_name : name, product_desc : desc, product_price : price, product_qavail : qavail};
            post(params, "update_product");
        }
        else{
            params = {product_name : name, product_desc : desc, product_price : price, product_qavail : qavail};
            post(params, "create_product");
        }
    }



}


function logout_click(){
    params = {};
    post(params, 'logout_click');

}

function fillform(id){
    if (typeof product === 'undefined')
        return;
    for (let i = 0; i < product.length; i++){
        if (product[i][0] == id){
            document.getElementById("name").value = product[i][1];
            document.getElementById("desc").value = product[i][3];
            document.getElementById("price").value = product[i][2];
            document.getElementById("qavail").value = product[i][4];
            document.getElementById("Submit").value = String(id)
            document.getElementById("Submit").innerHTML= "Update";

        }
    }
    if (role != "CS"){
    document.getElementById("cancel").visibility = "visible";
    document.getElementById("cancel").style.display="";
    }

}

function unfillform(){
    document.getElementById("name").value = null;
    document.getElementById("desc").value = null;
    document.getElementById("price").value = null;
    document.getElementById("qavail").value = null;
    document.getElementById("Submit").value = 0 
    document.getElementById("Submit").innerHTML= "Submit";
    document.getElementById("cancel").style.display="none";


}

function init(product_info, c, u, t, r){
    if (c == 1){
        document.getElementById("product_created").style.display="";
        document.getElementById("product_created").style.visibility = "visible"; 
    }
    if (t != 0){
        document.getElementById("name").value = t[1];
        document.getElementById("desc").value = t[3];
        document.getElementById("price").value = t[2];
        document.getElementById("qavail").value = t[4];
        document.getElementById("Submit").value = t[0]
        document.getElementById("Submit").innerHTML= "Update";
        document.getElementById("cancel").visibility = "visible";
        document.getElementById("cancel").style.display="";

    }
    if (u == 1){
        document.getElementById("product_updated").style.display="";
        document.getElementById("product_updated").style.visibility = "visible";
        unfillform();

    }
    if (r == 'CS'){
        document.getElementById("name").readOnly = true;
        document.getElementById("desc").readOnly = true;
        document.getElementById("price").readOnly = true;
        document.getElementById("qavail").readOnly = true;
		document.getElementById("Submit").style.display = "none";
		document.getElementById("Submit").style.visibility = "hidden";
        document.getElementById("cancel").style.display="none";
    }
    role = r    
    product = product_info;
}
