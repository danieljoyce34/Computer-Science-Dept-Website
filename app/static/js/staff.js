
$(document).ready(function () {
	// Type filter change
	$('#type-filter').change(function(){
		var type = $(this).val().toLowerCase();
		if (type == 'all') 
			$('#staff-list>div.staff-container').show();
		else {
			$('#staff-list>div.staff-container').each(function(){
				$(this).find('.staff-email').text().toLowerCase() == type ? $(this).show() : $(this).hide();
			});
		}
	});

	// Name search text field change
	$('#search-filter').keyup(function(){
		var search = $(this).val().toLowerCase();
		$('#staff-list>div.staff-container').each(function(){
			$(this).find('.staff-name').text().toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
	});

	// Filter reset button
	$('#filter-reset').click(function(){
		$('#type-filter').prop('selectedIndex',0);
		$('#search-filter').val('');
		$('#staff-list').find('.staff-container').show();
	});
});