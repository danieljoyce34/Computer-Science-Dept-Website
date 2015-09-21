

$(document).ready(function(){

	$(document).on("click", ".ae-container-edit-button", function(){
		container = $(this).parent().parent();
		container.find('.ae-container-content').hide();
		container.find('.ae-container-content-edit').show();
		container.find('.ae-container-edit-button').hide();
		container.find('.ae-container-edits').show();
		container.find('.ae-edit-buttons').show();

		container.find('.ae-container-content-edit').val(container.find('.ae-container-content').text());

		container.find('.ae-edit-category').val(container.find('.ae-hidden-cat').text());

		startDate = new Date(container.find('.ae-hidden-start').text());
		container.find('.ae-edit-start').val(startDate.getFullYear() + "-" + ("0" + (startDate.getMonth() + 1)).slice(-2) + "-" + ("0" + startDate.getDate()).slice(-2));

		endDate = new Date(container.find('.ae-hidden-end').text());
		container.find('.ae-edit-end').val(endDate.getFullYear() + "-" + ("0" + (endDate.getMonth() + 1)).slice(-2) + "-" + ("0" + endDate.getDate()).slice(-2));

		container.siblings().find('.ae-edit-cancel').click();
	});

	$(document).on("click", ".ae-edit-cancel", function(){
		container = $(this).parent().parent();
		container.find('.ae-container-content').show();
		container.find('.ae-container-content-edit').hide();
		container.find('.ae-container-edit-button').show();
		container.find('.ae-container-edits').hide();
		container.find('.ae-edit-buttons').hide();
	});

	$('#ae-new-reset').click(function(){
		box = $(this).closest('#ae-creator');
		box.find('#ae-new-content').val("");
		box.find('#ae-new-details select').val("");
		box.find('#ae-new-start').val("");
		box.find('#ae-new-end').val("");
	});

	$('#ae-new-submit').click(function(){
		if(validAlert()){
			submitAlert();
		}
	});
});

function validAlert(){
	if($('#ae-new-content').val().trim() == ""){
		alert('Alert text is required');
		return false;
	}
	else if($('#ae-new-category option:selected').val() == ""){
		alert('Alert category is required');
		return false;
	}
	else if($('#ae-new-start').val() == ""){
		alert('A start date is required');
		return false;
	}
	else if($('#ae-new-end').val() == ""){
		alert('An end date is required');
		return false;
	}
	else if(new Date($('#ae-new-start').val()) >= new Date($('#ae-new-end').val())){
		alert('The start date must be before then end date');
		return false;
	}
	return true;
}

function submitAlert(){
	var aContent = $('#ae-new-content').val();
	var aCategory = $('#ae-new-category option:selected').val();
	var aStart = $('#ae-new-start').val();
	var aEnd = $('#ae-new-end').val();
	var data = {
    	'content' : aContent,
    	'category' : aCategory,
    	'start_date' : aStart,
    	'end_date' : aEnd,
	};
	$.ajax({
        type : 'POST',
        url : "/addAlert",
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        dataType: 'json',
        success: function(result) {
            console.log(result);
            addNewAlert(JSON.parse(data));
        },
        error: function(data, textStatus, jqXHR){
        	console.log("Error");
        }
    });
}

function addNewAlert(data){
	//prepend to #ae-list
	// Replace "user_id" and "post_date"
	// Replace hidden-id text with actual ID
	$('#ae-list').prepend($('<div class="ae-container">')
		.append($('<div class="ae-container-content">').text(data['content']))
		.append($('<textarea class="ae-container-content-edit" maxlength="175">'))
		.append($('<div class="ae-container-header">')
			.append($('<a href="#" class="ae-container-edit-button">').text("Edit"))
			.append($('<span>').text("Posted by: " + "user_id" + " on " + "post_date")))
		.append($('<div class="ae-container-edits">')
			.append($('<select class="ae-edit-category">')
				.append($('<option value="General">').text("General"))
				.append($('<option value="Warning">').text("Warning"))
				.append($('<option value="Colloquium">').text("Colloquium"))
				.append($('<option value="Class">').text("Class"))
				.append($('<option value="Meeting">').text("Meeting"))
				.append($('<option value="Club">').text("Club")))
			.append($('<div>')
				.append($('<span>').text("Start Date"))
				.append($('<input type="date" class="ae-edit-start">')))
			.append($('<div>')
				.append($('<span>').text("End Date"))
				.append($('<input type="date" class="ae-edit-end">'))))
		.append($('<div class="ae-edit-buttons">')
			.append($('<button type="button" class="ae-edit-cancel">').text("Cancel"))
			.append($('<button type="button" class="ae-edit-submit">').text("Submit")))
		.append($('<div style="display:none;" class="ae-hidden-id">').text("ID"))
		.append($('<div style="display:none;" class="ae-hidden-start">').text(data.start_date))
		.append($('<div style="display:none;" class="ae-hidden-end">').text(data.end_date))
		.append($('<div style="display:none;" class="ae-hidden-cat">').text(data.category)));
}



