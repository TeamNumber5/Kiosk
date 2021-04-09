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


function init_list(product_info){
   product = product_info;

   for (let i = 0; i < product.length; i++){
    document.addEventListener('DOMContentLoaded', () =>  {

	     document.getElementById(product[i][0]).addEventListener('click', () => { params = {product_id: product[i][0]}; name='go_update'; post(params, name);});
    });
        
   }
}

