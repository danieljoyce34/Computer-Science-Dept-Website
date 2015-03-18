$(document).ready(function(){
	$('#nav-switch').click(function(){
		if($('#nav').css('display') == 'none'){
			$('#nav').show();
			// Slide animation for the responsive navigation bar
			$('#content-wrapper').animate({
				left: 200,
				right: -200
			}, 200, function(){
			});
			//$('#content-wrapper').css('left', 200);
			//$('#content-wrapper').css('right', -200);
		}
		else{
			// Slide animation for the responsive navigation bar
			$('#content-wrapper').animate({
				left: 0,
				right: 0
			}, 200, function(){
				$('#nav').hide();
			});
			//$('#content-wrapper').css('left', 0);
			//$('#content-wrapper').css('right', 0);
		}
	});

	$('.nav-item').on('swipedown', function(){
		$('#nav').find('.subnav').hide();
		$('this').find('.subnav').show();
	});
});
