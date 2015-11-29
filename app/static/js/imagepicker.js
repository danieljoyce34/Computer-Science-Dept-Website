$(document).ready(function(){

	$(document).on('click', '.image-container', function(){
		$(this).parent().find('.selected-image').removeClass("selected-image");
		$(this).addClass("selected-image");
	});

	$('#ip-open-btn').click(function(){
		$('#image-picker').show();
	});

	$('#ip-cancel-btn, .modal-btn-close').click(function(){
		$('#image-picker').hide();
		$('.selected-image').removeClass("selected-image");
	});
});