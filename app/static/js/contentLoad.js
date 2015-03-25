var pageName = '';
var container = 'card';
var header = 'card-header';
var content = 'card-content';

$(document).ready(function () {

	pageName = document.getElementById("content").innerHTML;
	document.getElementById("content").innerHTML = '<div class="' + pageName.trim().toLowerCase() + '-content"></div>';

	//TODO
	//Make the Ajax request to the JSON and call the addContent Page to create dynamic cards for each page.

});

//TODO
//Have this function create a card based on the JSON specs
function addContent(header, content) {

} 