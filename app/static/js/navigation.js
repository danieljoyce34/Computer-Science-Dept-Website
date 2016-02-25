$(document).ready(function(){
	// Resonsive navigation button - shows/hides side navbar
	$('#nav-switch').click(function(){ $('#nav').css('display') == 'none' ? showNav() : hideNav(); });

	// For Mobile devices - shows the submenu options when a menu item is swiped down
	$('.nav-item').on('swiperight', function(){
		$('#nav').find('.subnav').hide();
		$(this).find('.subnav').slideDown(125);
	});

	// Hides the responsive sidenav bar when the page content is clicked
	$('#page-content').click(function(){
		if($(this).css('left') == '200px')
			hideNav();
	});

	// Slide transition for displaying submenu options on hover
	$('.nav-item').hover(
		function(){ $(this).children('.subnav').stop().slideDown(100); },
		function(){ $(this).children('.subnav').stop().slideUp(100); }
	);
});

// Shows the responsive navigation menu
function showNav(){
	$('#nav').show();
	$('#page-content').children().css('pointer-events', 'none');
	// Responsive nav menu slide animation
	$('#page-content').animate({
		left: 200,
		right: -200
	}, 200, function(){});
}

// Hides the responsive navigation menu
function hideNav(){
	$('#page-content').animate({
		left: 0,
		right: 0
	}, 200, function(){
		$('#nav').hide();
		$('#page-content').children().css('pointer-events', 'auto');
	});
}
