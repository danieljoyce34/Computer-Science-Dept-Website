

$(document).ready(function(){
	$('.ae-container-edit-button').on('click', function(){
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

	$('.ae-edit-cancel').on('click', function(){
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
        },
        error: function(data, textStatus, jqXHR){
        	console.log("Error");
        }
    });
}