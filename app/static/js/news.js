
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
		// Show preview
		setPreview($(this));
		if($('#ne-side').css('display') == 'none') {
			extendSidePreview();
		}
	});

	$('#ne-return').click(function(){
		hideSidePreview();
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
	$('#ne-side-title').text(article.data('title'));
	document.getElementById("ne-side-article").innerHTML = article.data('article');
	$('#ne-side-intro').text(article.data('intro'));
	
	$('#ne-img-preview').css('background-image', article.data('img-url'));
	$('#ne-img-id').val(article.data('img-id'));

	// Date Formatting
	var start = new Date(article.data('start'));
	var sDate = ("0" + (start.getMonth() + 1)).slice(-2) + "-" + ("0" + start.getDate()).slice(-2) + "-" + start.getFullYear();
	$('#ne-side-start_date').text("Posted: " + sDate);
}

// Shows the preview fields
function showPreview(){
	$('#ne-side-start_date, #ne-side-title, #ne-side-intro, #ne-side-article, #ne-img-preview').show();
}

// Side preview slide animation (show)
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

// Side preview slide animation (hide)
function hideSidePreview(){
	$('#ne-side').animate({
		opacity: 0
	}, 700, function(){
		$('#ne-side').hide();
		$('#ne-list').animate({
			width: '100%'
		}, 300);
	});
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
