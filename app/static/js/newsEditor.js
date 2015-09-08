//TODO: Needs some kind of form validation
//TODO: Fix date formatting
//TODO: Add delete feature
//TODO: Fix image file selection
//TODO: Switch to using AJAX calls for adding/editing

var baseURL = "http://127.0.0.1:5000/"

$(document).ready(function(){

	// Title search filter 
	$('#ne-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		$('.ne-news-container').each(function(){
			$(this).find('.ne-container-title').text().toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
		checkSelected();
	});

	// Clear button for search filter
	$('#ne-search-clear').click(function(){
		$('#ne-search').val('');
		$('.ne-news-container').show();
		checkSelected();
	});

	// Container selection
	$(document).on('click', '.ne-news-container', function(){
		// Set selected class
		$(this).siblings().removeClass("ne-selected");
		$(this).addClass("ne-selected");
		// Enable edit/delete buttons
		$('#ne-edit, #ne-delete').prop('disabled', false);
		// Show preview
		setPreview($(this));
		if($('#ne-side').css('display') == 'none')
			extendSidePreview();
	});

	// Add news button
	$('#ne-add').click(function(){
		clearSide();
		showEdit();
		extendSideEdit();
		$('#ne-side').prop('action', '/submitNews');
	});

	// Edit news button
	$('#ne-edit').click(function(){
		showEdit();
		extendSideEdit();
		$('#ne-side').prop('action', '/submitNewsEdits/' + $('.ne-selected .ne-container-id').text());
	});

	// Cancel edits button
	$('#ne-cancel').click(function(){ hideEditForm(); });
});

// Checks if an article is selected from the list
function checkSelected(){
	var noSelection = $('#ne-list').find('.ne-selected').length == 0 || $('.ne-selected').css('display') == 'none';
	$('#ne-edit, #ne-delete').prop('disabled', noSelection);
	noSelection ? clearSide() : setPreview($('.ne-selected'));
}

// Sets the fields for the article preview
function setPreview(article){
	// Preview Display
	$('#ne-side-title').text(article.find('.ne-container-title').text());
	$('#ne-side-article').text(article.find('.ne-container-article').text());
	// Edit Display
	$('#ne-title-edit').val(article.find('.ne-container-title').text());
	$('#ne-intro-edit').val(article.find('.ne-container-intro').text());
	$('#ne-article-edit').val(article.find('.ne-container-article').text());
	// Date Formatting
	var start = new Date(article.find('.ne-container-start').text());
	var sDate = start.getFullYear() + "-" + ("0" + (start.getMonth() + 1)).slice(-2) + "-" + ("0" + start.getDate()).slice(-2);
	$('#ne-sdate-edit').val(sDate);
	var end = new Date(article.find('.ne-container-end').text());
	var eDate = end.getFullYear() + "-" + ("0" + (end.getMonth() + 1)).slice(-2) + "-" + ("0" + end.getDate()).slice(-2);
	$('#ne-edate-edit').val(eDate);

	$('#ne-side').prop('action', '/submitNewsEdits/' + $('.ne-selected .ne-container-id').text());

}

// Shows the preview fields
function showPreview(){
	$('#ne-side-title, #ne-side-article').show();
	$('.ne-side-label').hide();
	$('#ne-title-edit, #ne-intro-edit, #ne-article-edit, #ne-img-edit, #ne-sdate-edit, #ne-edate-edit').hide();
}

// Side preview slide animation
function extendSidePreview(){
	$('#ne-list').animate({
		width: '30%'
	}, 300, function(){
		$('#ne-side').show();
		$('#ne-side').animate({
			opacity: 1
		}, 700);
	});
}

// Clears preview/form fields
function clearSide(){
	$('#ne-side-title, #ne-side-article').text('');
	$('#ne-article-edit, #ne-side input').val('');
}


function showEdit(){
	$('#ne-side-title, #ne-side-article').hide();
	$('.ne-side-label').show();
	$('#ne-title-edit, #ne-intro-edit, #ne-article-edit, #ne-img-edit, #ne-sdate-edit, #ne-edate-edit').show();
}

function extendSideEdit(){
	if($('#ne-side').css('display') != 'none'){
		$('#ne-list').animate({
			left: '-30%'
		},300);
		$('#ne-side').animate({
			left: '5'
		},300);
	}
	else{
		$('#ne-side').show();
		$('#ne-list').animate({
			opacity: '0'
		}, 500, function(){
			$('#ne-side').css('left', '5px');
			$('#ne-side').animate({
				opacity: 1
			}, 500);
		});
	}
	$('#ne-options button').prop('disabled', true);
	$('#ne-edit-options').show();
}

function hideEditForm(){
	$('#ne-edit-options').hide();
	if($('#ne-list').find('.ne-selected').length == 0){
		$('#ne-list').css('opacity', '1');
		$('#ne-side').animate({
			opacity: 0
		}, 900, function(){
			$('#ne-side').css('left', '30%');
			$('#ne-side').hide();
			showPreview();
			$('#ne-add').prop('disabled',false);
		});
	}
	else{
		$('#ne-list').animate({
			left: '0'
		},300);
		$('#ne-side').animate({
			left: '30%'
		},300, function(){
			showPreview();
			$('#ne-options button').prop('disabled', false);
			checkSelected();
		});
	}
}
