
$(document).ready(function(){

	// Displaying either upcoming colloquia, or recent colloquia
	var id = $('#recent-1').data('id');
	var today = new Date("2019-01-01");
	var colDate = new Date($('#recent-1').data('start'));
	var newColloquia = false;
	var cntr = 1;

	while (document.getElementById('upcoming-'+cntr) != null) {
		colDate = new Date($('#upcoming-'+cntr).data('start'));
		if (colDate.getTime() >= today.getTime()) {
			newColloquia = true;
			break;
		}
		cntr++;
	}

	if (newColloquia == false) {
		$('#upcoming').hide();
		$('#ce-list-upcoming').hide();
		setPreview($('#recent-1'));
		setPreview($('#recent-2'));
	}
	else {
		$('#recent').hide();
		$('#ce-list-recent').hide();
		for(i=1;i<=id;i++){
			if (document.getElementById('upcoming-'+i) == null)
				break;
			var temp = new Date($('#upcoming-'+i).data('start'));
			if (temp.getTime() < today.getTime())
				$('#upcoming-'+i).hide();
			else setPreview($('#upcoming-'+i));
		}
	}
});


// Sets the fields for the article preview
function setPreview(article){
	// Preview Display
	var mod = '';
	if ($(article).get(0).id == 'recent-1' || $(article).get(0).id == 'recent-2')
		mod = 'r';
	var id = article.data('id');
	var elements = ['start', 'time', 'speaker', 'bio', 'prelude', 'content', 'postlude', 'location'];
	for(j=0;j<8;j++){
		if (document.getElementById(mod+id+'-'+elements[j]) == null && elements[j] != 'content'){
			// Prevents null pointer errors
		}
		else {
			if (elements[j] == 'content')
				document.getElementById(mod+id+'-content').innerHTML = article.data('article');
			else document.getElementById(mod+id+'-'+elements[j]).innerHTML = article.data(elements[j]);
		}
	}
	$('#'+mod+id+'-start').show();
	$('#'+mod+id+'-time').show();
	$('#'+mod+id+'-location').show();
	$('#'+mod+id+'-speaker').show();
	$('#'+mod+id+'-bio').show();
	$('#'+mod+id+'-content').show();
	$('#'+mod+id+'-postlude').show();

	// Date/Time Formatting
	var start = new Date(article.data('start'));
	var eDate = ("0" + (start.getMonth() + 1)).slice(-2) + " / " + ("0" + start.getDate()).slice(-2) + " / " + start.getFullYear();
	$('#'+mod+id+'-start').text('Colloquium Date: ' + eDate);
	if(!(start.getHours() == 0) || !(start.getMinutes() == 0)){
		var time = 'Time: ' + (start.getHours() % 12) + ":" + ("0" + start.getMinutes()).slice(-2);
		if(start.getHours() >= 12){
			time += " PM";
			if(start.getHours() == 12)
				time = time.replace("0:","12:");
		}else time += " AM";
		$('#'+mod+id+'-time').text(time);
	}
	else{
		$('#'+mod+id+'-time').text('');
		$('#'+mod+id+'-time').hide();
	}

	hideEmpty(article);
	showFilled(article);
	addFormatting(article);
}

// Hides fields that are empty; requires article input due to multiple instances
function hideEmpty(article){
	var id = article.data('id');
	var mod = '';
	if ($(article).get(0).id == 'recent-1' || $(article).get(0).id == 'recent-2')
		mod = 'r';
	var hidden = ['start', 'time', 'speaker', 'bio', 'prelude', 'content', 'postlude', 'location'];
	for(var x=0;x<8;x++){
		if(document.getElementById(mod+id+'-'+hidden[x]) == null){
			//Prevents nullpointer exceptions
		}else{
		switch (document.getElementById(mod+id+'-'+hidden[x]).innerHTML){
			case 'None': //Empty fields are listed as "None"
				$('#'+mod+id+'-'+hidden[x]).hide();
				document.getElementById(mod+id+'-'+hidden[x]).style.visibility = 'hidden';
				break;
			case '':
				$('#'+mod+id+'-'+hidden[x]).hide();
				document.getElementById(mod+id+'-'+hidden[x]).style.visibility = 'hidden';
				break;
			default:
				document.getElementById(mod+id+'-'+hidden[x]).style.visibility = 'visible';
				break;
		}
		}
	}
	if(document.getElementById(mod+id+'-'+hidden[2]).innerHTML == 'None' || document.getElementById(mod+id+'-'+hidden[2]).innerHTML == ''){
		$('#'+mod+id+'-'+hidden[3]).hide();
	}
}

// Shows fields that are filled; requires article input due to multiple instances
function showFilled(article){
	var id = article.data('id');
	var mod = '';
	if ($(article).get(0).id == 'recent-1' || $(article).get(0).id == 'recent-2')
		mod = 'r';
	var hidden = ['start', 'time', 'speaker', 'bio', 'prelude', 'content', 'postlude', 'location'];
	for(var y=0;y<8;y++){
		if(document.getElementById(mod+id+'-'+hidden[y]) == null){
			//Prevents nullpointer exceptions
		}else{
			var txt = document.getElementById(mod+id+'-'+hidden[y]).innerHTML.trim();
			if (txt != 'None' && txt != ''){
				$('#'+mod+id+'-'+hidden[y]).show();
			}
		}
	}
	if(document.getElementById(mod+id+'-'+hidden[2]).innerHTML == 'None' || document.getElementById(mod+id+'-'+hidden[2]).innerHTML == ''){
		$(id+'-'+hidden[3]).hide();
	}
}

// Adds formatting to fields
function addFormatting(article){
	var id = article.data('id');
	var mod = '';
	if ($(article).get(0).id == 'recent-1' || $(article).get(0).id == 'recent-2')
		mod = 'r';
	if(document.getElementById(mod+id+'-speaker').style.visibility != 'hidden')
		document.getElementById(mod+id+'-speaker').innerHTML = '<div style="font-size:1.3em">by ' + article.data('speaker') + '</div>';
	if(document.getElementById(mod+id+'-bio').style.visibility != 'hidden')
		document.getElementById(mod+id+'-bio').innerHTML = '<strong style="font-size:1.2em">About ' + article.data('speaker') + ':</strong></br><div style="padding-left:2em">' + article.data('bio') + '</div></br>';
	if(document.getElementById(mod+id+'-prelude').style.visibility != 'hidden')
		document.getElementById(mod+id+'-prelude').innerHTML = '<strong style="font-size:1.2em">Abstract:</strong></br><div style="padding-left:2em">' + article.data('prelude') + '</div></br>';
	if(document.getElementById(mod+id+'-content').style.visibility != 'hidden')
		document.getElementById(mod+id+'-content').innerHTML = '<strong style="font-size:1.2em">Description:</strong></br><div style="padding-left:2em">' + article.data('article') + '</div></br>';
	if(document.getElementById(mod+id+'-postlude').style.visibility != 'hidden')
		document.getElementById(mod+id+'-postlude').innerHTML = '<strong style="font-size:1.1em">Additional Notes:</strong></br><div style="padding-left:2em">' + article.data('postlude') + '</div></br>';
	if(document.getElementById(mod+id+'-location').style.visibility != 'hidden')
		document.getElementById(mod+id+'-location').innerHTML = 'Location: ' + article.data('location') + '</br>';
}
