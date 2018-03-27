
$(document).ready(function(){

	// Title search filter
	$('#ce-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		// Hide/show colloquia articles based on search terms
		$('.ce-colloquium-container').each(function(){
			$(this).data('title').toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
		checkSelected();
	});

	// Clear button for search filter
	$('#ce-search-clear').click(function(){
		$('#ce-search').val('');
		$('.ce-colloquium-container').show();
		checkSelected();
	});

	// Colloquia article container selection
	$(document).on('click', '.ce-colloquium-container', function(){
		// Set selected class
		$(this).siblings().removeClass("ce-selected");
		$(this).addClass("ce-selected");
		// Show preview
		setPreview($(this));
		showFilled();
		if($('#ce-side').css('display') == 'none') {
			extendSidePreview();
		}
	});

	$('#ce-return').click(function(){
		hideSidePreview();
	})


});

// Checks if an article is selected from the list
function checkSelected(){
	var noSelection = $('#ce-list').find('.ce-selected').length == 0 || $('.ce-selected').css('display') == 'none';
	$('#ce-edit, #ce-delete').prop('disabled', noSelection);
	noSelection ? clearSide() : setPreview($('.ce-selected'));
}

// Sets the fields for the article preview
function setPreview(article){
	// Preview Display
	$('#ce-side-title').text(article.data('title'));
	$('#ce-side-speaker').text(article.data('speaker'));
	document.getElementById("ce-side-bio").innerHTML = article.data('bio');
	document.getElementById("ce-side-prelude").innerHTML = article.data('prelude');
	document.getElementById("ce-side-article").innerHTML = article.data('article');
	document.getElementById("ce-side-postlude").innerHTML = article.data('postlude');
	$('#ce-side-location').text(article.data('location'));
	//$('#ce-side-author').text(article.data('author'));

	// Date/Time Formatting
	var start = new Date(article.data('start'));
	var eDate = ("0" + (start.getMonth() + 1)).slice(-2) + " / " + ("0" + start.getDate()).slice(-2) + " / " + start.getFullYear();
	$('#ce-side-event_date').text('Colloquium Date: ' + eDate);
	if(!(start.getHours() == 0) || !(start.getMinutes() == 0)){
		var time = 'Time: ' + (start.getHours() % 12) + ":" + ("0" + start.getMinutes()).slice(-2);
		if(start.getHours() >= 12){
			time += " PM";
			if(start.getHours() == 12)
				time = time.replace("0:","12:");
		}else time += " AM";
		$('#ce-side-time').text(time);
	}
	else{
		$('#ce-side-time').text('');
		$('#ce-side-time').hide();
	}

	hideEmpty();
	showFilled();
	addFormatting(article);
}

// Shows the preview fields
function showPreview(){
	$('#ce-side-event_date, #ce-side-time, #ce-side-title, #ce-side-speaker, #ce-side-bio, #ce-side-prelude, #ce-side-article, #ce-side-postlude, #ce-side-location, #ce-img-preview').show();
}

// Adds formatting to fields
function addFormatting(article){
	if(document.getElementById('ce-side-title').style.visibility != 'hidden')
		document.getElementById('ce-side-title').innerHTML = article.data('title');
	if(document.getElementById('ce-side-speaker').style.visibility != 'hidden')
		document.getElementById('ce-side-speaker').innerHTML = '<strong style="font-size:1.1em">Speaker:</strong> ' + article.data('speaker') + '</br>';
	if(document.getElementById('ce-side-bio').style.visibility != 'hidden')
		document.getElementById("ce-side-bio").innerHTML = '<strong style="font-size:1.2em">About ' + article.data('speaker') + ':</strong></br><div style="padding-left:2em">' + article.data('bio') + '</div></br>';
	if(document.getElementById('ce-side-prelude').style.visibility != 'hidden')
		document.getElementById("ce-side-prelude").innerHTML = '<strong style="font-size:1.2em">Abstract:</strong></br><div style="padding-left:2em">' + article.data('prelude') + '</div></br>';
	if(document.getElementById('ce-side-article').style.visibility != 'hidden')
		document.getElementById("ce-side-article").innerHTML = '<strong style="font-size:1.2em">Description:</strong></br><div style="padding-left:2em">' + article.data('article') + '</div></br>';
	if(document.getElementById('ce-side-postlude').style.visibility != 'hidden')
		document.getElementById("ce-side-postlude").innerHTML = '<strong style="font-size:1.1em">Additional Notes:</strong></br><div style="padding-left:2em">' + article.data('postlude') + '</div></br>';
	if(document.getElementById('ce-side-location').style.visibility != 'hidden')
		document.getElementById('ce-side-location').innerHTML = '<strong style="font-size:1.1em">Location: </strong></br>' + article.data('location') + '</br>';
	//if(document.getElementById('ce-side-author').style.visibility != 'hidden')
	//	document.getElementById('ce-side-author').innerHTML = '<strong style="font-size:1.1em">Author: </strong>' + article.data('author') + '</br>';
}

// Hides fields that are empty
function hideEmpty(){
	var hidden = ['ce-side-event', 'ce-side-time', 'ce-side-title', 'ce-side-speaker', 'ce-side-bio', 'ce-side-prelude', 'ce-side-article', 'ce-side-postlude', 'ce-side-location'];
	for(var x=0;x<9;x++){
		if(document.getElementById(hidden[x]) == null){
			//Prevents nullpointer exceptions
		}else{
		switch (document.getElementById(hidden[x]).innerHTML){
			case 'None': //Empty fields are listed as "None"
				$('#'+hidden[x]).hide();
				document.getElementById(hidden[x]).style.visibility = 'hidden';
				break;
			case '':
				$('#'+hidden[x]).hide();
				document.getElementById(hidden[x]).style.visibility = 'hidden';
				break;
			default:
				document.getElementById(hidden[x]).style.visibility = 'visible';
				break;
		}
		}
	}
	if(document.getElementById('ce-side-speaker').innerHTML == 'None' || document.getElementById('ce-side-speaker').innerHTML == ''){
		$('#ce-side-bio').hide();
	}
}

// Shows fields that are filled
function showFilled(){
	var hidden = ['ce-side-event_date', 'ce-side-time', 'ce-side-title', 'ce-side-speaker', 'ce-side-bio', 'ce-side-prelude', 'ce-side-article', 'ce-side-postlude', 'ce-side-location', 'ce-side-author'];
	for(var x=0;x<10;x++){
		if(document.getElementById(hidden[x]) == null){
			//Prevents nullpointer exceptions
		}else{
			var txt = document.getElementById(hidden[x]).innerHTML.trim();
			if (txt != 'None' && txt != ''){
				$('#'+hidden[x]).show();
			}
		}
	}
	if(document.getElementById('ce-side-speaker').innerHTML == 'None' || document.getElementById('ce-side-speaker').innerHTML == ''){
		$('#ce-side-bio').hide();
	}
}

// Side preview slide animation (show)
function extendSidePreview(){
	$('#ce-list').animate({
		width: '30%'
	}, 300, function(){
		$('#ce-side').show();
		$('#ce-side').animate({
			opacity: 1
		}, 700);
	});
}

// Side preview slide animation (hide)
function hideSidePreview(){
	$('#ce-side').animate({
		opacity: 0
	}, 700, function(){
		$('#ce-side').hide();
		$('#ce-list').animate({
			width: '100%'
		}, 300);
	});
}

// Side edit hide slide animation
function hideEditForm(callback){
	$('#ce-edit-options').hide();
	if($('#ce-list').find('.ce-selected').length == 0){
		$('#ce-list').css('opacity', '1');
		$('#ce-side').animate({
			opacity: 0
		}, 900, function(){
			$('#ce-side').css('left', '30%');
			$('#ce-side').hide();
			showPreview();
			hideEmpty();
			showFilled();
			$('#ce-add').prop('disabled',false);
			callback();
		});
	}
	else{
		$('#ce-list').animate({
			left: '0'
		},300);
		$('#ce-side').animate({
			left: '30%'
		},300, function(){
			showPreview();
			$('#ce-options button').prop('disabled', false);
			checkSelected();
			hideEmpty();
			showFilled();
			callback();
		});
	}
}
