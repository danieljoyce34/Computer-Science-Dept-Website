//TODO: Fix image file selection
//TODO: Switch to using AJAX calls for adding/editing

$(document).ready(function(){

	// Title search filter 
	$('#ne-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		// Hide/show news articles based on search terms
		$('.ne-news-container').each(function(){
			$(this).find('.ne-container-title').text().toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
		// Hide/show preview based on it's visibility
		checkSelected();
	});

	// Clear button for search filter
	$('#ne-search-clear').click(function(){
		$('#ne-search').val('');
		// Show all news articles
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
			saveNews($('.ne-selected .ne-container-id').text());
	})
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

// Shows news edit fields
function showEdit(){
	$('#ne-side-title, #ne-side-article').hide();
	$('.ne-side-label').show();
	$('#ne-title-edit, #ne-intro-edit, #ne-article-edit, #ne-img-edit, #ne-sdate-edit, #ne-edate-edit').show();
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
	return true;
}

// Adds news to the db
function saveNews(id){
	var data = {
		'headline' : $('#ne-title-edit').val(),
		'intro' : $('#ne-intro-edit').val(),
		'article' : $('#ne-article-edit').val(),
		'image' : $('#ne-img-edit').val(),
		'start_date' : $('#ne-sdate-edit').val(),
		'end_date' : $('#ne-edate-edit').val(),
	};

	var formData = new FormData($('#ne-side')[0]);

	url = '/addNews';
	if(id != -1)
		url = '/editNews/' + id;
	$.ajax({
		type: 'POST',
		url: url,
		data: formData,
		//data: $('form').serialize(),
        //contentType: "application/x-www-form-urlencoded",
        contentType: false,
        processData: false,
        cache: false,
        success: function(result) {
        	console.log(result.newsID);
           	hideEditForm(function(){ (id == -1) ? addNewsContainer(data, result.newsID) : updateNewsContainer(data); });
        },
        error: function(data, textStatus, jqXHR){
        	alert("Unable to save the news article. Please try again later.");
        	console.log(data.responseText + ", " + textStatus + ", " + jqXHR);
        }
	})
}

// Adds a new news container
function addNewsContainer(news, id){
	//TODO: get ID
	//TODO: add div for image when that gets implemented
	$('#ne-list').prepend($('<div class="ne-news-container">')
		.append($('<div class="ne-container-title">').text(news.headline))
		.append($('<div class="ne-container-intro">').text(news.intro))
		.append($('<div class="ne-container-id">').text(id))
		.append($('<div class="ne-container-article">').text(news.article))
		.append($('<div class="ne-container-start">').text(news.start_date))
		.append($('<div class="ne-container-end">').text(news.end_date)));
	
	$('#ne-list .ne-news-container').first().click();
}

function updateNewsContainer(data){
	news = $('#ne-list .ne-selected');
	news.find('.ne-container-title').text(data.headline);
	news.find('.ne-container-intro').text(data.intro);
	news.find('.ne-container-article').text(data.article);
	news.find('.ne-container-start').text(data.start_date);
	news.find('.ne-container-end').text(data.end_date);
	$('#ne-list .ne-selected').click();
}

