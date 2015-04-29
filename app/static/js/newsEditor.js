// Needs some kind of form validation

var baseURL = "http://127.0.0.1:5000/"

$(document).ready(function(){

	// Edit button listener
	$('#news-editor-edit').click(function(){
		var index = $('#news-editor-selected').text();
		var news = $('#news-editor-list').find('div.editor-news-container:eq(' + (parseInt(index)-1) + ')')
		$('#edit-news-headline').val(news.find('.editor-news-title').text());
		$('#edit-news-intro').val(news.find('.editor-news-intro').text());
		$('#edit-news-article').val(news.find('.editor-news-article').text());
		
		// TODO Fix date formatting
		$('#edit-news-start').val(news.find('.editor-news-start').text());
		$('#edit-news-end').val(news.find('.editor-news-end').text());
		// Set the form action
		$('#news-editor-editing').prop('action', '/submitNewsEdits/' + index);
		showNewsForm();
	});

	// Add button listener
	$('#news-editor-add').click(function(){
		// Set form action
		$('#news-editor-editing').prop('action', '/submitNews');
		clearNewsForm();
		showNewsForm();
	});

	// Form cancel - hides form
	$('#cancel-edits').click(function(){ hideNewsForm(); });

	// Search Filter
	$('#news-editor-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		$('#news-editor-list>div.editor-news-container').each(function(){
			$(this).find('.editor-news-title').text().toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
	});

	// Clears the search filter
	$('#news-editor-clear').click(function(){
		$('#news-editor-search').val('');
		$('#news-editor-list').find('.editor-news-container').show();
	});

	// News list selection listener
	$(document).on('click', '.editor-news-container', function(){
		$('#news-editor-preview').text($(this).find('div.editor-news-article').text());
		$(this).css('background','#3cb0fd');
		$(this).siblings().css('background','white');
		$('#news-editor-selected').text($(this).find('div.editor-news-id').text());
		$('#news-editor-edit').prop('disabled',false);
	});
});

// Unecessary
/*
	function getNewsList(){
	$.ajax({
		url: baseURL + "retrieveNews",
		type: 'GET',
		dataType: 'json',
		error: function(xhr, status, error){console.log(xhr + " " + status + " " + error);},
		success: function(response){
			$('#news-editor-list').children().remove();
			$.each(response.news, function(){
				$('#news-editor-list').append($('<div class="editor-news-container">')
					.append($('<div class="editor-news-title">').text($(this)[0].headline))
					.append($('<div class="editor-news-intro">').text($(this)[0].intro))
					.append($('<div class="editor-news-id">').text($(this)[0].id))
					.append($('<div class="editor-news-article">').text($(this)[0].article))
					.append($('<div class="editor-news-start">').text($(this)[0].start_date))
					.append($('<div class="editor-news-end">').text($(this)[0].end_date))
				);
			});
			$('#news-editor-preview').text("");
			$('#news-editor-selected').text("");
			$('#news-editor-edit').prop('disabled',true);
		}
	})
	}
*/

// Clears the form
function clearNewsForm(){
	$('#edit-news-headline').val("");
	$('#edit-news-intro').val("");
	$('#edit-news-article').val("");
	$('#edit-news-start').val("");
	$('#edit-news-end').val("");
}

// Shows the form
function showNewsForm(){
	$('#news-editor-preview').hide();
	$('#news-editor-edit').prop('disabled',true);
	$('#news-editor-add').prop('disabled',true);
	$('#news-editor-side').animate({
		left: 5
	}, 200, function(){
		$('#news-editor-editing').show();
		$('#news-editing-options').show();
	});
}

// Hides the form
function hideNewsForm(){
	$('#news-editor-editing').hide();
	if($('#news-editor-selected').text())
		$('#news-editor-edit').prop('disabled',false);
	$('#news-editor-add').prop('disabled',false);
	$('#news-editor-side').animate({
		left: 350
	}, 200, function(){
		$('#news-editing-options').hide();
		$('#news-editor-preview').show();
	});
}

