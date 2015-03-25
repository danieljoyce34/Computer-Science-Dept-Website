$(document).ready(function(){

	// Resonsive navigation button - shows/hides side navbar
	$('#nav-switch').click(function(){
		if($('#nav').css('display') == 'none'){
			$('#nav').show();
			$('#content-wrapper').children().css('pointer-events', 'none');
			// Slide animation for the responsive navigation bar
			$('#content-wrapper').animate({
				left: 200,
				right: -200
			}, 200, function(){
			});
		}
		else{
			// Slide animation for the responsive navigation bar
			$('#content-wrapper').animate({
				left: 0,
				right: 0
			}, 200, function(){
				$('#nav').hide();
				$('#content-wrapper').children().css('pointer-events', 'auto');
			});
		}
	});

	// For Mobile devices - shows the submenu options when a menu item is swiped down
	$('.nav-item').on('swiperight', function(){
		$('#nav').find('.subnav').hide();
		$(this).find('.subnav').slideDown(125);
	});

	// Hides the responsive sidenav bar when the page content is clicked
	$('#content-wrapper').click(function(){
		if($(this).css('left') == '200px'){
			$(this).animate({
				left: 0,
				right: 0
			}, 200, function(){
				$('#nav').hide();
				$('#content-wrapper').children().css('pointer-events', 'auto');
			});
		}
	});

	// Slide transition for displaying submenu options on hover
	$('.nav-item').hover(
		function(){ $(this).children('.subnav').slideDown(125); },
		function(){ $(this).children('.subnav').slideUp(125); }
	);
});