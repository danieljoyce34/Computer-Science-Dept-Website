$(document).ready(function(){
	$(".submenu").click(function(){
		var $self = $(this);
		var menu_num = $self.data("menunum");
		$self.siblings(".submenu-item[data-menunum="+menu_num+"]").toggleClass("hiddensub");
	});
	$('.dropdown-menu').click(function(e) {
        e.stopPropagation();
    });
	$('.dropdown').hover(function(e){
		e.stopPropagation();
	});
});