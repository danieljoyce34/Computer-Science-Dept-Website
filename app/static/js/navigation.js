$(document).ready(function(){
	$('#nav-switch').click(function(){
		if($('#nav').css('display') == 'none'){
			$('#nav').show();
			$('#content-wrapper').css('left', 200);
			$('#content-wrapper').css('right', -200);
		}
		else{
			$('#nav').hide();
			$('#content-wrapper').css('left', 0);
			$('#content-wrapper').css('right', 0);
		}
	})
});