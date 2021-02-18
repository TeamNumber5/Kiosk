
    	document.addEventListener('DOMContentLoaded', clickHandling);

    	function clickHandling() {
    		document.getElementById("startTransaction").addEventListener('click', displayError);
    		document.getElementById("viewProducts").addEventListener('click', displayError);
    		document.getElementById("createEmployee").addEventListener('click', displayError);
    		document.getElementById("salesReport").addEventListener('click', displayError);
    		document.getElementById("cashierReport").addEventListener('click', displayError);
    	}

    	function displayError() {
    		alert("Functionality has not been implemented yet.");
    	}

   