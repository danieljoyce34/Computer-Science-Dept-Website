

$(document).ready(function(){

	// Set default dates
	setDates();

	// Alert edit button click handler
	$(document).on("click", ".ae-container-edit-button", function(){
		// Shows edit fields
		container = $(this).parent().parent();
		container.find('.ae-container-content').hide();
		container.find('.ae-container-content-edit').show();
		container.find('.ae-container-edit-button').hide();
		container.find('.ae-container-edits').show();
		container.find('.ae-edit-buttons').show();
		// Set edit field information
		container.find('.ae-container-content-edit').val(container.find('.ae-container-content').text());
		startDate = new Date(container.find('.ae-hidden-start').text());
		container.find('.ae-edit-start').val(startDate.getFullYear() + "-" + ("0" + (startDate.getMonth() + 1)).slice(-2) + "-" + ("0" + startDate.getDate()).slice(-2));
		endDate = new Date(container.find('.ae-hidden-end').text());
		container.find('.ae-edit-end').val(endDate.getFullYear() + "-" + ("0" + (endDate.getMonth() + 1)).slice(-2) + "-" + ("0" + endDate.getDate()).slice(-2));
		// Hide other alert editing displays
		container.siblings().find('.ae-edit-cancel').click();
	});
	
	// Cancel edit button
	$(document).on("click", ".ae-edit-cancel", function(){
		// Hides edit fields and show basic alert display
		container = $(this).closest('.ae-container');
		container.find('.ae-container-content').show();
		container.find('.ae-container-content-edit').hide();
		container.find('.ae-container-edit-button').show();
		container.find('.ae-container-edits').hide();
		container.find('.ae-edit-buttons').hide();
	});

	$(document).on("click", ".ae-edit-submit", function(){
		a = $(this).closest('.ae-container');
		if(validAlertEdits(a))
			submitAlertEdits(a);
	});

	// New alert reset - resets add alert fields
	$('#ae-new-reset').click(function(){
		box = $(this).closest('#ae-creator');
		box.find('#ae-new-content').val("");
		box.find('#ae-new-author').val("");
		setDates();
	});

	// New alert submit - attempts to submit alert if valid new alert input
	$('#ae-new-submit').click(function(){
		if(validAlert())
			submitAlert();
	});


	// New Alert Toolbar
	$('#btnedit-bold').on("click",function(e) {
		wrapText('b');
	});

	$('#btnedit-italic').on("click",function(e) {
		wrapText('i');
	});

	$('#btnedit-underline').on("click",function(e) {
		wrapText('u');
	});

	$('#btnedit-link').on("click",function(e) {
		var textArea = $('.area'),
			len = textArea.val().length,
			start = textArea[0].selectionStart,
			end = textArea[0].selectionEnd,
			selectedText = textArea.val().substring(start, end);
		$('#btnedit-title').val(selectedText);
		$('#btnedit-url').val('http://');
		$('#prompt').show();
	});

	$('#btnedit-ok').on("click",function(e) {
		e.preventDefault();
		$('#prompt').hide();
	    replacement = '<a title="'+$('#btnedit-title').val()+'" href="'+$('#btnedit-url').val()+'" rel="external">' + $('#btnedit-title').val() + '</a>';
        wrapLink(replacement);
	}); 

	$('#btnedit-cancel').on("click",function(e) {
		e.preventDefault();
		$('#prompt').hide();
	}); 
});

// Set default dates
function setDates(){
	var now = new Date();
    var month = (now.getMonth() + 1);               
    var day = now.getDate();
    if(month < 10) 
        month = "0" + month;
    if(day < 10) 
        day = "0" + day;
    var today = now.getFullYear() + '-' + month + '-' + day;
    $('#ae-new-start').val(today);

    var month2 = (now.getMonth() + 2);
    var day2 = (now.getDate());
    if(month2 < 10) 
        month2 = "0" + month2;
    if(month2 == 12)
    	month2 = "01"
    if(day2 < 10) 
        day2 = "0" + day2;
    var year2 = now.getFullYear();
    var twoWeeks = year2 + '-' + month2 + '-' + day2;
    $('#ae-new-end').val(twoWeeks);
}

// Checks if the new alert input is valid
function validAlert(){
	// Check for alert text
	if($('#ae-new-content').val().trim() == ""){
		alert('Alert text is required');
		return false;
	}
	// Check for valid start date
	else if($('#ae-new-start').val() == ""){
		alert('A start date is required');
		return false;
	}
	// Check for valid end date
	else if($('#ae-new-end').val() == ""){
		alert('An end date is required');
		return false;
	}
	// Check for valid name
	else if($('#ae-new-author').val() == ""){
		alert('An author is required');
		return false;
	}
	// Check if start date is before end date
	else if(new Date($('#ae-new-start').val()) >= new Date($('#ae-new-end').val())){
		alert('The start date must be before then end date');
		return false;
	}
	return true;
}

// Adds alert to db
function submitAlert(){
	// Get new alert information
	var aContent = $('#ae-new-content').val();
	var aStart = $('#ae-new-start').val();
	var aEnd = $('#ae-new-end').val();
	var aAuthor = $('#ae-new-author').val();
	var data = {
    	'content' : aContent,
    	'start_date' : aStart,
    	'end_date' : aEnd,
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
            addNewAlert(data, result.alertID, result.alertUser);
        },
        error: function(data, textStatus, jqXHR){
        	alert("Unable to save alert. Please try again later.");
        }
    });
}

// Adds a new alert container to the list after successfully saving to db
function addNewAlert(data, id, user){
	//prepend to #ae-list
	$('#ae-list').prepend($('<div class="ae-container">')
		.append($('<div class="ae-container-content">').text(data.content))
		.append($('<textarea class="ae-container-content-edit" maxlength="175">'))
		.append($('<div class="ae-container-header">')
			.append($('<a href="#" class="ae-container-edit-button">').text("Edit")))
		.append($('<div class="ae-container-edits">')
			.append($('<div>')
				.append($('<span>').text("Start Date"))
				.append($('<input type="date" class="ae-edit-start">')))
			.append($('<div>')
				.append($('<span>').text("End Date"))
				.append($('<input type="date" class="ae-edit-end">')))
			.append($('<div>')
				.append($('<span>').text("Your Name"))
				.append($('<input type="text" class="ae-edit-author">'))))
		.append($('<div class="ae-edit-buttons">')
			.append($('<button type="button" class="ae-edit-cancel">').text("Cancel"))
			.append($('<button type="button" class="ae-edit-submit">').text("Submit")))
		.append($('<div style="display:none;" class="ae-hidden-id">').text(id))
		.append($('<div style="display:none;" class="ae-hidden-start">').text(data.start_date))
		.append($('<div style="display:none;" class="ae-hidden-end">').text(data.end_date))
		.append($('<div style="display:none;" class="ae-hidden-author">').text(data.author)));
}

function validAlertEdits(a){
	// Check for alert text
	if(a.find('.ae-container-content-edit').val().trim() == ""){
		alert('Alert text is required');
		return false;
	}
	// Check for valid start date
	else if(a.find('.ae-edit-start').val() == ""){
		alert('A start date is required');
		return false;
	}
	// Check for valid end date
	else if(a.find('.ae-edit-end').val() == ""){
		alert('An end date is required');
		return false;
	}
	// Check for valid name
	else if($('#ae-new-author').val() == ""){
		alert('An author is required');
		return false;
	}
	// Check if start date is before end date
	else if(new Date(a.find('.ae-edit-start').val()) >= new Date(a.find('.ae-edit-end').val())){
		alert('The start date must be before then end date');
		return false;
	}
	return true;
}

function submitAlertEdits(a){
	var contentEdit = a.find('.ae-container-content-edit').val();
	var startEdit = a.find('.ae-edit-start').val();
	var endEdit = a.find('.ae-edit-end').val();
	var authorEdit = $('#ae-edit-author').val();
	var data = {
    	'content' : contentEdit,
    	'start_date' : startEdit,
    	'end_date' : endEdit,
    	'author' : authorEdit
	};
	// Ajax call to save alert edits to db
	$.ajax({
        type : 'POST',
        url : "/editAlert/" + a.find('.ae-hidden-id').text(),
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        dataType: 'json',
        success: function(result) {
            updateAlert(a, data);
            alert("Edits saved");
            a.find('.ae-edit-cancel').click();
        },
        error: function(data, textStatus, jqXHR){
        	alert("Unable to save alert edits. Please try again later.");
        }
    });
}

function updateAlert(a, data){
	a.find('.ae-container-content').text(data.content);
	a.find('.ae-hidden-start').text(data.start_date);
	a.find('.ae-hidden-end').text(data.end_date);
	a.find('.ae-hidden-author').text(data.author);
}


function wrapLink(link) {
	var textArea = $('.area'),
		len = textArea.val().length,
		start = textArea[0].selectionStart,
		end = textArea[0].selectionEnd,
		selectedText = textArea.val().substring(start, end);
	textArea.val(textArea.val().substring(0, start) + link + textArea.val().substring(end, len));
	$('.area').keyup();
}

function wrapText(tag) {
	var textArea = $('.area'),
		len = textArea.val().length,
		start = textArea[0].selectionStart,
		end = textArea[0].selectionEnd,
		selectedText = textArea.val().substring(start, end),
		replacement = '<' + tag + '>' + selectedText + '</' + tag + '>';
	textArea.val(textArea.val().substring(0, start) + replacement + textArea.val().substring(end, len));
	$('.area').keyup();
}

$(function() {	
	$('.area').keyup(function(){					
		var value = $(this).val();
		var contentAttr = $(this).attr( 'name' );
		$( '.' + contentAttr + '' ).html(value);
	})
});

