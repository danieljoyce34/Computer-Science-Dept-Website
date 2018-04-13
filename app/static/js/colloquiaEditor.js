
$(document).ready(function(){

	// Title search filter
	$('#ce-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		// Hide/show colloquium articles based on search terms
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
		// Enable edit/delete buttons
		$('#ce-edit, #ce-delete').prop('disabled', false);
		// Show preview
		setPreview($(this));
		if($('#ce-side').css('display') == 'none')
			extendSidePreview();
	});

	// Add colloquium button
	$('#ce-add').click(function(){
		clearSide();
		$('#ce-submit').show();
		$('#ce-save').hide();
		showEdit();
		extendSideEdit();
	});

	// Edit colloquium button
	$('#ce-edit').click(function(){
		$('#ce-submit').hide();
		$('#ce-save').show();
		showEdit();
		extendSideEdit();
	});

	// Cancel edits button
	$('#ce-cancel').click(function(){ hideEditForm(function(){}); });

	$('#ce-submit').click(function(){
		if(validColloquiaInput())
			saveColloquia(-1);
	});
	
	$('#ce-preview').click(function(){ previewPopup(this,'colloquiaPopup.html'); });
	
	$('#ce-save').click(function(){
		if(validColloquiaInput())
			saveColloquia($('.ce-selected').data('id'));
	})

	$('#ip-ok-btn').click(function(){});
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
	$('#ce-side-location').text(article.data('location'));
	$('#ce-side-prelude').text(article.data('prelude'));
	$('#ce-side-bio').text(article.data('bio'));
	$('#ce-side-article').text(article.data('article'));
	$('#ce-side-postlude').text(article.data('postlude'));
	$('#ce-side-author').text(article.data('author'));

	// Date/Time Formatting
	var start = new Date(article.data('start'));
	var sDate = ("0" + (start.getMonth() + 1)).slice(-2) + " / " + ("0" + start.getDate()).slice(-2) + " / " + (start.getFullYear());
	$('#ce-side-event').text('Colloquium Date: ' + sDate);
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

	// Edit Display
	$('#ce-title-edit').val(article.data('title'));
	$('#ce-speaker-edit').val(article.data('speaker'));
	$('#ce-location-edit').val(article.data('location'));
	$('#ce-prelude-edit').val(article.data('prelude'));
	$('#ce-bio-edit').val(article.data('bio'));
	$('#ce-content-edit').val(article.data('article'));
	$('#ce-postlude-edit').val(article.data('postlude'));
	$('#ce-author-edit').val(article.data('author'));

	// Clearing Empty Fields
	if(article.data('speaker') == 'None')
		$('#ce-speaker-edit').val('');
	if(article.data('bio') == 'None')
		$('#ce-bio-edit').val('');
	if(article.data('prelude') == 'None')
		$('#ce-prelude-edit').val('');
	if(article.data('postlude') == 'None')
		$('#ce-postlude-edit').val('');
	if(article.data('author') == 'None')
		$('#ce-author-edit').val('');

	// Date/Time Formatting
	var event = new Date(article.data('start'));
	var eDate = event.getFullYear() + "-" + ("0" + (event.getMonth() + 1)).slice(-2) + "-" + ("0" + event.getDate()).slice(-2) + "T" + ("0" + event.getHours()).slice(-2) + ":" + ("0" + event.getMinutes()).slice(-2);
	$('#ce-edate-edit').val(eDate);

	hideEmpty();
	showFilled();
	addFormatting(article);
}

// Shows the preview fields
function showPreview(){
	$('#ce-side-title, #ce-side-speaker, #ce-side-bio, #ce-side-prelude, #ce-side-article, #ce-side-postlude, #ce-side-location, #ce-side-author, #ce-side-event, #ce-side-time').show();
	$('.ce-side-label, #ce-title-edit, #ce-speaker-edit, #ce-bio-edit, #ce-prelude-edit, #ce-content-edit, #ce-postlude-edit, #ce-location-edit, #ce-author-edit, #ce-edate-edit').hide();
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
		document.getElementById('ce-side-location').innerHTML = '<strong style="font-size:1.1em">Location: </strong>' + article.data('location') + '</br>';
	if(document.getElementById('ce-side-author').style.visibility != 'hidden')
		document.getElementById('ce-side-author').innerHTML = '<strong style="font-size:1.1em">Author: </strong>' + article.data('author') + '</br>';
}

// Hides fields that are empty
function hideEmpty(){
	var hidden = ['ce-side-event', 'ce-side-time', 'ce-side-title', 'ce-side-speaker', 'ce-side-bio', 'ce-side-prelude', 'ce-side-article', 'ce-side-postlude', 'ce-side-location', 'ce-side-author'];
	for(var x=0;x<10;x++){
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
	var hidden = ['ce-side-event', 'ce-side-time', 'ce-side-title', 'ce-side-speaker', 'ce-side-bio', 'ce-side-prelude', 'ce-side-article', 'ce-side-postlude', 'ce-side-location', 'ce-side-author'];
	for(var x=0;x<10;x++){
		if(document.getElementById(hidden[x]) == null){
			//Prevents nullpointer exceptions
		}else{
			if (document.getElementById(hidden[x]).innerHTML != 'None' && document.getElementById(hidden[x]).innerHTML != ''){
				$('#'+hidden[x]).show();
			}
		}
	}
}

// Side preview slide animation
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

// Clears preview/form fields
function clearSide(){
	$('#ce-side-title, #ce-side-speaker, #ce-side-bio, #ce-side-prelude, #ce-side-article, #ce-side-postlude, #ce-side-location, #ce-side-author, #ce-side-event, #ce-side-time').text('');
	$('#ce-speaker-edit, #ce-bio-edit, #ce-prelude-edit, #ce-content-edit, #ce-postlude-edit, #ce-location-edit, #ce-author-edit, #ce-side input').val('');
}

// Shows colloquia edit fields
function showEdit(){
	$('#ce-side-title, #ce-side-speaker, #ce-side-bio, #ce-side-prelude, #ce-side-article, #ce-side-postlude, #ce-side-location, #ce-side-author, #ce-side-event, #ce-side-time').hide();
	$('.ce-side-label, #ce-title-edit, #ce-speaker-edit, #ce-bio-edit, #ce-prelude-edit, #ce-content-edit, #ce-postlude-edit, #ce-location-edit, #ce-author-edit, #ce-edate-edit, #ce-time-edit').show();
}

// Side edit display slide animation
function extendSideEdit(){
	if($('#ce-side').css('display') != 'none'){
		$('#ce-list').animate({
			left: '-60%'
		},300);
		$('#ce-side').animate({
			left: '5'
		},300);
	}
	else{
		$('#ce-side').show();
		$('#ce-list').animate({
			opacity: '0'
		}, 500, function(){
			$('#ce-side').css('left', '5px');
			$('#ce-side').animate({
				opacity: 1
			}, 500);
		});
	}
	$('#ce-options button').prop('disabled', true);
	$('#ce-edit-options').show();
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

// Sets empty fields to "None"
function outputFormat(){
	if($('#ce-speaker-edit').val().trim() == ""){
		$('#ce-speaker-edit').val('None');
	}
	if($('#ce-bio-edit').val().trim() == ""){
		$('#ce-bio-edit').val('None');
	}
	if($('#ce-prelude-edit').val().trim() == ""){
		$('#ce-prelude-edit').val('None');
	}
	if($('#ce-postlude-edit').val().trim() == ""){
		$('#ce-postlude-edit').val('None');
	}
}

// Checks if colloquia edit field input is valid
function validColloquiaInput(){
	// Check for title
	if($('#ce-title-edit').val().trim() == ""){
		alert('A title is required');
		return false;
	}
	else if($('#ce-content-edit').val().trim() == ""){
		alert('Article text is required');
		return false;
	}
	else if($('#ce-location-edit').val().trim() == ""){
		alert('A location is required');
		return false;
	}
	else if($('#ce-author-edit').val().trim() == ""){
		alert('An author is required');
		return false;
	}
	else if($('#ce-edate-edit').val().trim() == ""){
		alert("A date is required");
		return false;
	}
	/*else if(!$('#ce-img-edit').is('img')){
		alert('Chosen file is not an image');
		return false;
	}*/
	return true;
}

// Adds colloquia to the db
function saveColloquia(id){
	// Create an alert for this colloquia
	addColloquiaAlert();
	
	var formData = new FormData($('#ce-side')[0]);

	url = '/addColloquia';
	if(id != -1)
		url = '/editColloquia/' + id;
	$.ajax({
		type: 'POST',
		url: url,
		data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function(result) {
        	jsonObj = $.parseJSON(result);
           	hideEditForm(function(){ (id == -1) ? addColloquiaContainer(jsonObj.colloquia) : updateColloquiaContainer(jsonObj.colloquia); });
        },
        error: function(data, textStatus, jqXHR){
        	if ('image')
        	alert("Unable to save the colloquia article. Please try again later.");
        	console.log(data.responseText + ", " + textStatus + ", " + jqXHR);
        }
	})
}

// Adds a new colloquia container
function addColloquiaContainer(colloquia){
	c = $('<div class="ce-colloquium-container">');
	c.data('title', colloquia.title);
	c.data('speaker', colloquia.speaker);
	c.data('start', colloquia.event_date);
	c.data('location', colloquia.location);
	c.data('prelude', colloquia.prelude);
	c.data('bio', colloquia.speaker_bio);
	c.data('article', colloquia.content);
	c.data('postlude', colloquia.postlude);
	c.data('author', colloquia.author);
	$('#ce-list').prepend(c.append($('<div class="ce-container-title">').text(colloquia.title)));
	$('#ce-list .ce-colloquium-container').first().click();
}

// Updates colloquia container
function updateColloquiaContainer(colloquia){
	c = $('#ce-list .ce-selected');
	c.data('id', colloquia.id);
	c.data('title', colloquia.title);
	c.data('speaker', colloquia.speaker);
	c.data('start', colloquia.event_date);
	c.data('location', colloquia.location);
	c.data('prelude', colloquia.prelude);
	c.data('bio', colloquia.speaker_bio);
	c.data('article', colloquia.content);
	c.data('postlude', colloquia.postlude);
	c.data('author', colloquia.author);
	c.find('.ce-container-title').text(colloquia.title);
	$('#ce-list .ce-selected').click();
}

// Adds an alert for the colloquia
function addColloquiaAlert(){
	// Get new alert information
	var aContent = 'Colloquium: ' + $('#ce-title-edit').val();
	var aStart = $('#ce-edate-edit').val();
	var aEnd = $('#ce-edate-edit').val();
	var aAuthor = $('#ce-author-edit').val();

	// Formatting dates
	var temp = new Date($('#ce-edate-edit').val());
	aContent = aContent + ', on ' + (temp.getMonth()+1) + '/' + temp.getDate() + '/' + temp.getFullYear();
	
	// Creating start/end dates from colloquia's date
	var date = new Date($('#ce-edate-edit').val());
	var sDate = new Date($('#ce-edate-edit').val());
	var eDate = new Date($('#ce-edate-edit').val());
	var days = 31;

	// Configures calendar formatting & sets new dates to +- 1 week
	switch (date.getMonth()){
		case 0:
			if (date.getDate() <= 7) {
				// aStart month = December, year--
				sDate.setMonth(11);
				sDate.setYear(date.getFullYear()-1);
			}else if (date.getDate() >= days - 7) {
				// Year is the same
				eDate.setMonth(1);
			}

			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 1:
			// Leap year adjustments
			if (date.getFullYear() % 4 == 0)
				days = 29;
			else days = 28;
			
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 2:
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 3:
			days = 30;
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 4:
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 5:
			days = 30;
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 6:
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 7:
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 8:
			days = 30;
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 9:
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 10:
			days = 30;
			if (date.getDate() <= 7){
				sDate.setMonth(date.getMonth()-1);
			}else if (date.getDate() >= (days - 7)){
				eDate.setMonth(date.getMonth()+1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		case 11:
			if (date.getDate() >= 24) {
				// aEnd month = January, year++
				eDate.setMonth(0);
				eDate.setYear(date.getFullYear()+1);
			}else if (date.getDate() <= 7) {
				// Year is the same
				sDate.setMonth(date.getMonth()-1);
			}
			
			sDate.setDate((date.getDate() - 7) % days);
			eDate.setDate((date.getDate() + 7) % days);
			break;
		default:
			// Error was made
			alert('An error was made creating the alert dates, please edit manually');
			break;
	}
	aStart = sDate.getFullYear() + '-' + ('0' + (sDate.getMonth()+1)).slice(-2) + '-' + ('0' + sDate.getDate()).slice(-2) + 'T00:00';
	aEnd = eDate.getFullYear() + '-' + ('0' + (eDate.getMonth()+1)).slice(-2) + '-' + ('0' + eDate.getDate()).slice(-2) + 'T00:00';

	var data = {
    	'content' : aContent,
    	'start_date' : aStart,
    	'end_date' : aEnd,
	//'user_id' : 1,
    	'author' : aAuthor
	};

	// Ajax call to save alert to db
	$.ajax({
        	type : 'POST',
        	url : "/addAlert",
        	data: JSON.stringify(data),
        	contentType: 'application/json; charset=UTF-8',
        	dataType: 'json',
        	success: function(result) {
			// Adding the new alert to the screen is not necessary
        	    // addNewAlert(data, result.alertID, result.alertUser);
        	},
        	error: function(data, textStatus, jqXHR){
        		alert("Unable to save colloquia alert. Please edit manually.");
        	}
    	});
	
}

// Unused: Opens a preview of the colloquium (not properly implemented yet)
/*function previewPopup(article,url){
	nWindow = window.open(url,'Preview','height=250,width=200');
	if (window.focus)
		nWindow.focus();
	return false;
}
*/
// Unused: Uncomment and edit for colloquia editor image support (not properly implemented)
/*function readURL(input) {
	if (input.files && input.files[0]) {
	    var reader = new FileReader();
		reader.onload = function (e) {
	    	//$('#sbe-img-preview').attr('src', e.target.result);
	        //$('#ce-img-preview').css('background-image', "url(" + e.target.result + ")");
	    }
	    reader.readAsDataURL(input.files[0]);
  	}
}
*/
