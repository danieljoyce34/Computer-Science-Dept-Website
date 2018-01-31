
$(document).ready(function(){

	// Title search filter 
	$('#ne-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		// Hide/show news articles based on search terms
		$('.ne-news-container').each(function(){
			$(this).data('title').toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
		checkSelected();
	});

	// Clear button for search filter
	$('#ne-search-clear').click(function(){
		$('#ne-search').val('');
		$('.ne-news-container').show();
		checkSelected();
	});

	// News article container selection
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
		$('#ne-submit').show();
		$('#ne-save').hide();
		showEdit();
		extendSideEdit();
	});

	// Edit news button
	$('#ne-edit').click(function(){
		$('#ne-submit').hide();
		$('#ne-save').show();
		showEdit();
		extendSideEdit();
	});

	// Cancel edits button
	$('#ne-cancel').click(function(){ hideEditForm(function(){}); });

	$('#ne-submit').click(function(){
		if(validNewsInput())
			saveNews(-1);
	});

	$('#ne-save').click(function(){
		if(validNewsInput())
			saveNews($('.ne-selected').data('id'));
	})

	$('#ip-ok-btn').click(function(){
		if($('#image-list').find('.selected-image').length){
			$('#image-picker').hide();
			// Set news image preview to the selected image
			$('#ne-img-edit-preview').css('background-image', $('.selected-image .image-preview').css('background-image'));
			$('#ne-img-upload').val("");
			$('#ne-img-id').val($('.selected-image .image-id').text());
			$('.selected-image').removeClass("selected-image");
		}
		else
			alert("Please select an image");
	});
	
	$("#ne-img-upload").change(function(){ readURL(this); });
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
	$('#ne-side-title').text(article.data('title'));
	$('#ne-side-intro').text(article.data('intro'));
	$('#ne-side-article').text(article.data('article'));
	$('#ne-img-preview').css('background-image', article.data('img-url'));

	// Edit Display
	$('#ne-title-edit').val(article.data('title'));
	$('#ne-intro-edit').val(article.data('intro'));
	$('#ne-article-edit').val(article.data('article'));
	$('#ne-img-edit-preview').css('background-image', article.data('img-url'));
	$('#ne-img-id').val(article.data('img-id'));

	// Date Formatting
	var start = new Date(article.data('start'));
	var sDate = start.getFullYear() + "-" + ("0" + (start.getMonth() + 1)).slice(-2) + "-" + ("0" + start.getDate()).slice(-2);
	$('#ne-sdate-edit').val(sDate);
	var end = new Date(article.data('end'));
	var eDate = end.getFullYear() + "-" + ("0" + (end.getMonth() + 1)).slice(-2) + "-" + ("0" + end.getDate()).slice(-2);
	$('#ne-edate-edit').val(eDate);
}

// Shows the preview fields
function showPreview(){
	$('#ne-side-title, #ne-side-intro, #ne-side-article, #ne-img-preview').show();
	$('.ne-side-label, #ne-title-edit, #ne-intro-edit, #ne-article-edit, #ne-img-edit, #ne-sdate-edit, #ne-edate-edit, #ne-img-edit').hide();
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
	$('#ne-side-title, #ne-side-article, #ne-side-intro').text('');
	$('#ne-article-edit, #ne-side input, #ne-img-upload, #ne-img-id').val('');
	$('#ne-img-edit-preview').css('background-image', "");
	$('#ne-img-preview').css('background-image', "");
}

// Shows news edit fields
function showEdit(){
	$('#ne-side-title, #ne-side-article, #ne-side-intro, #ne-img-preview').hide();
	$('.ne-side-label, #ne-title-edit, #ne-intro-edit, #ne-article-edit, #ne-img-edit, #ne-sdate-edit, #ne-edate-edit, #ne-img-edit, #ne-img-edit-preview').show();
}

// Side edit display slide animation
function extendSideEdit(){
	if($('#ne-side').css('display') != 'none'){
		$('#ne-list').animate({
			left: '-60%'
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

// Side edit hide slide animation
function hideEditForm(callback){
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
			callback();
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
			callback();
		});
	}
}

// Checks if news edit field input is valid
function validNewsInput(){
	// Check for title
	if($('#ne-title-edit').val().trim() == ""){
		alert('Headline is required');
		return false;
	}
	else if($('#ne-article-edit').val().trim() == ""){
		alert('Article text is required');
		return false;
	}
	else if($('#ne-sdate-edit').val() == ""){
		alert("A start date is required");
		return false;
	}
	else if($('#ne-edate-edit').val() == ""){
		alert("An end date is required");
		return false;
	}
	else if(new Date($('#ne-sdate-edit').val()) >= new Date($('#ne-edate-edit').val())){
		alert('The start date must be before the end date');
		return false;
	}
	/*else if(!$('#ne-img-edit').is('img')){
		alert('Chosen file is not an image');
		return false;
	}*/
	return true;
}

// Adds news to the db
function saveNews(id){
	imageURL = $('#ne-img-edit-preview').css('background-image');
	var formData = new FormData($('#ne-side')[0]);

	url = '/addNews';
	if(id != -1)
		url = '/editNews/' + id;
	$.ajax({
		type: 'POST',
		url: url,
		data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function(result) {
        	jsonObj = $.parseJSON(result);
           	hideEditForm(function(){ (id == -1) ? addNewsContainer(jsonObj.news, imageURL) : updateNewsContainer(jsonObj.news, imageURL); });
        },
        error: function(data, textStatus, jqXHR){
        	if ('image')
        	alert("Unable to save the news article. Please try again later.");
        	console.log(data.responseText + ", " + textStatus + ", " + jqXHR);
        }
	})
}

// Adds a new news container
function addNewsContainer(news, imgURL){
	n = $('<div	class="ne-news-container">');
	n.data('title', news.headline);
	n.data('intro', news.intro);
	n.data('id', news.id);
	n.data('article', news.article);
	n.data('start', news.start_date);
	n.data('end', news.end_date);
	n.data('img-id', news.image_id);
	n.data('img-url', imgURL);
	$('#ne-list').prepend(n.append($('<div class="ne-container-title">').text(news.headline)));
	$('#ne-list .ne-news-container').first().click();
}

function updateNewsContainer(news, imgURL){
	n = $('#ne-list .ne-selected');
	n.data('title', news.headline);
	n.data('intro', news.intro);
	n.data('article', news.article);
	n.data('start', news.start_date);
	n.data('end', news.end_date);
	n.data('img-id', news.image_id);
	n.data('img-url', imgURL);
	n.find('.ne-container-title').text(news.headline);
	$('#ne-list .ne-selected').click();
}

function readURL(input) {
	if (input.files && input.files[0]) {
	    var reader = new FileReader();
		reader.onload = function (e) {
	    	//$('#sbe-img-preview').attr('src', e.target.result);
	        $('#ne-img-edit-preview').css('background-image', "url(" + e.target.result + ")");
	    }
	    reader.readAsDataURL(input.files[0]);
  	}
}
