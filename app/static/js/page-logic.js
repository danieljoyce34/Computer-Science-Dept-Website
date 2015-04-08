var pageName = '';
var pageTitle = '';
var container = document.getElementById("content");
var section = '';
var wrapper;

$(document).ready(function () {

	pageName = container.innerHTML.trim();
	container.innerHTML = '';
	section = pageName + '-wrapper';
	$(container).append($('<div class="' + section + '">'));
	// wrapper.innerHTML=pageName;

	$.ajax({url:"http://127.0.0.1:5000/loadJSON",success:function(result) { 
	 	//document.write(result);
	 	pageTitle = result['Page'];

	 	//debugger;
		for(var component in result['Page-Components']) {
			//debugger;
			//window.alert(result['Page-Components'][component]['Section'])
			//window.alert(component['Section']);
	 		addContent(section, result['Page-Components'][component]['Section'], result['Page-Components'][component]['Section-Data']);
	 	}
	 	//window.alert(result['Page']);// works yo
	 }});
	// //TODO
	//Make the Ajax request to the JSON and call the addContent Page to create dynamic cards for each page.

});

//TODO
//Have this function create a card based on the JSON specs
function addContent(section, CardName, Data) {

	$('.' + section).append($('<div class="' + CardName + " " + 'card' + '">').text(Data)
	);
	//David's scared about the carousel
} 