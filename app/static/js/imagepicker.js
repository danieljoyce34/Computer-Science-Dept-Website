$(document).ready(function(){

	$(document).on('click', '.image-container', function(){
		$(this).parent().find('.selected-image').removeClass("selected-image");
		$(this).addClass("selected-image");
	});

	/*
	$('#ip-ok-btn').click(function(){
		if($('#image-list').find('.selected-image').length){
			alert("Selected Image ID: " + $('.selected-image .image-id').text());
			$('#image-picker').hide();
			// Use image info before removing selected-image class
			$('.selected-image').removeClass("selected-image");
		}
		else{
			alert("Please select an image");
		}
	});*/

	$('#ip-open-btn').click(function(){
		$('#image-picker').show();
	});

	$('#ip-cancel-btn, .modal-btn-close').click(function(){
		$('#image-picker').hide();
		$('.selected-image').removeClass("selected-image");
	});
});