
$(document).ready(function(){

	// Title search filter 
	$('#sbe-search').keyup(function(){
		var search = $(this).val().toLowerCase();
		// Hide/show sidebar contents based on search terms
		$('.sbe-sidebar-container').each(function(){
			$(this).find('.sbe-container-title').text().toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
		// Hide/show preview based on it's visibility
		checkSelected();
	});

	// Clear button for search filter
	$('#sbe-search-clear').click(function(){
		$('#sbe-search').val('');
		// Show all sidebar contents
		$('.sbe-sidebar-container').show();
		checkSelected();
	});

	// Sidebar content container selection
	$(document).on('click', '.sbe-sidebar-container', function(){
		// Set selected class
		$(this).siblings().removeClass("sbe-selected");
		$(this).addClass("sbe-selected");
		// Enable edit/delete buttons
		$('#sbe-edit, #sbe-delete').prop('disabled', false);
		// Show preview
		setPreview($(this));
		if($('#sbe-side').css('display') == 'none')
			extendSidePreview();
	});

	// Add sidebar button
	$('#sbe-add').click(function(){
		clearSide();
		$('#sbe-submit').show();
		$('#sbe-save').hide();
		showEdit();
		extendSideEdit();
	});

	// Edit sidebar button
	$('#sbe-edit').click(function(){
		$('#sbe-submit').hide();
		$('#sbe-save').show();
		showEdit();
		extendSideEdit();
	});

	// Cancel edits button
	$('#sbe-cancel').click(function(){ hideEditForm(function(){}); });

	$('#sbe-submit').click(function(){
		if(validSidebarInput())
			saveSidebar(-1);
	});

	$('#sbe-save').click(function(){
		if(validSidebarInput())
			saveSidebar($('.sbe-selected .sbe-container-id').text());
	})
});

// Checks if an content is selected from the list
function checkSelected(){
	var noSelection = $('#sbe-list').find('.sbe-selected').length == 0 || $('.sbe-selected').css('display') == 'none';
	$('#sbe-edit, #sbe-delete').prop('disabled', noSelection);
	noSelection ? clearSide() : setPreview($('.sbe-selected'));
}

// Sets the fields for the content preview
function setPreview(content){
	// Preview Display
	$('#sbe-side-title').text(content.find('.sbe-container-title').text());
	$('#sbe-side-content').text(content.find('.sbe-container-content').text());
	// Edit Display
	$('#sbe-title-edit').val(content.find('.sbe-container-title').text());
	$('#sbe-content-edit').val(content.find('.sbe-container-content').text());
	$('#sbe-category-edit').val(content.find('.sbe-container-category').text());
	$('#sbe-active-edit').prop('checked', content.find('.sbe-container-active').text()==1);
}

// Shows the preview fields
function showPreview(){
	$('#sbe-side-title, #sbe-side-content').show();
	$('.sbe-side-label').hide();
	$('#sbe-title-edit, #sbe-content-edit, #sbe-img-edit, #sbe-category-edit, #sbe-active').hide();
}

// Side preview slide animation
function extendSidePreview(){
	$('#sbe-list').animate({
		width: '30%'
	}, 300, function(){
		$('#sbe-side').show();
		$('#sbe-side').animate({
			opacity: 1
		}, 700);
	});
}

// Clears preview/form fields
function clearSide(){
	$('#sbe-side-title, #sbe-side-content').text('');
	$('#sbe-content-edit, #sbe-side input').val('');
}

// Shows sidebar edit fields
function showEdit(){
	$('#sbe-side-title, #sbe-side-content').hide();
	$('.sbe-side-label').show();
	$('#sbe-title-edit, #sbe-content-edit, #sbe-img-edit, #sbe-category-edit').show();
	$('#sbe-active').show();
}

// Side edit display slide animation
function extendSideEdit(){
	if($('#sbe-side').css('display') != 'none'){
		$('#sbe-list').animate({
			left: '-60%'
		},300);
		$('#sbe-side').animate({
			left: '5'
		},300);
	}
	else{
		$('#sbe-side').show();
		$('#sbe-list').animate({
			opacity: '0'
		}, 500, function(){
			$('#sbe-side').css('left', '5px');
			$('#sbe-side').animate({
				opacity: 1
			}, 500);
		});
	}
	$('#sbe-options button').prop('disabled', true);
	$('#sbe-edit-options').show();
}

// Side edit hide slide animation
function hideEditForm(callback){
	$('#sbe-edit-options').hide();
	if($('#sbe-list').find('.sbe-selected').length == 0){
		$('#sbe-list').css('opacity', '1');
		$('#sbe-side').animate({
			opacity: 0
		}, 900, function(){
			$('#sbe-side').css('left', '30%');
			$('#sbe-side').hide();
			showPreview();
			$('#sbe-add').prop('disabled',false);
			callback();
		});
	}
	else{
		$('#sbe-list').animate({
			left: '0'
		},300);
		$('#sbe-side').animate({
			left: '30%'
		},300, function(){
			showPreview();
			$('#sbe-options button').prop('disabled', false);
			checkSelected();
			callback();
		});
	}
}

// Checks if sidebar edit field input is valid
function validSidebarInput(){
	// Check for title
	if($('#sbe-title-edit').val().trim() == ""){
		alert('Title is required');
		return false;
	}
	else if($('#sbe-content-edit').val().trim() == ""){
		alert('Content is required');
		return false;
	}
	// Check for a selected category
	else if($('#sbe-category-edit option:selected').val() == ""){
		alert('Alert category is required');
		return false;
	}
	return true;
}

// Adds sidebar to the db
function saveSidebar(id){
	var data = {
		'title' : $('#sbe-title-edit').val(),
		'content' : $('#sbe-content-edit').val(),
		'image' : $('#sbe-img-edit').val(),
		'category' : $('#sbe-category-edit option:selected').val(),
		'active' : $('#sbe-active-edit').is(':checked') ? 1 : 0
	};
	var formData = new FormData($('#sbe-side')[0]);

	url = '/addSidebar';
	if(id != -1)
		url = '/editSidebar/' + id;
	$.ajax({
		type: 'POST',
		url: url,
		data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function(result) {
        	jsonObj = $.parseJSON(result);
           	hideEditForm(function(){ (id == -1) ? addSidebarContainer(data, jsonObj.sideviewID) : updateSidebarContainer(data); });
        },
        error: function(data, textStatus, jqXHR){
        	alert("Unable to save the sidebar content. Please try again later.");
        	console.log(data.responseText + ", " + textStatus + ", " + jqXHR);
        }
	})
}

// Adds a new sidebar container
function addSidebarContainer(sidebar, id){
	//TODO: add div for image when that gets implemented
	$('#sbe-list').prepend($('<div class="sbe-sidebar-container">')
		.append($('<div class="sbe-container-title">').text(sidebar.title))
		.append($('<div class="sbe-container-id">').text(id))
		.append($('<div class="sbe-container-content">').text(sidebar.content)));
	
	$('#sbe-list .sbe-sidebar-container').first().click();
}

function updateSidebarContainer(data){
	sidebar = $('#sbe-list .sbe-selected');
	sidebar.find('.sbe-container-title').text(data.title);
	sidebar.find('.sbe-container-content').text(data.content);
	sidebar.find('.sbe-container-category').text(data.category);
	sidebar.find('.sbe-container-active').text(data.active);
	$('#sbe-list .sbe-selected').click();
}

