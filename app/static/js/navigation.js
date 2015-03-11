$(document).ready(function(){
	$('#nav-switch').click(function(){
		if($('#nav').css('display') == 'none'){
			$('#nav').show();
			$('#content-wrapper').css('left', 160);
		}
		else{
			$('#nav').hide();
			$('#content-wrapper').css('left', 0);
		}
	})
});