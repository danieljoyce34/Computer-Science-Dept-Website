
var types = ["fulltime", "adjunct", "other"];

var staff = [
	{
		"name" : "staff1",
		"position" : ["instructor"],
		"email" : "staff1@gmail.com",
		"type" : "fulltime"
	},
	{
		"name" : "staff2",
		"position" : ["professor"],
		"email" : "staff2@gmail.com",
		"type" : "fulltime"
	},
	{
		"name" : "staff3",
		"position" : ["assistant"],
		"email" : "staff3@gmail.com",
		"type" : "adjunct"
	},
	{
		"name" : "staff4",
		"position" : ["administrator"],
		"email" : "staff4@gmail.com",
		"type" : "other"
	},
	{
		"name" : "staff5",
		"position" : ["professor", "chair"],
		"email" : "staff5@gmail.com",
		"type" : "fulltime"
	},
	{
		"name" : "staff6",
		"position" : ["adjunct instructor"],
		"email" : "staff6@gmail.com",
		"type" : "adjunct"
	}
];

$(document).ready(function(){
	getTypes();
	getStaff('all');

	$('#type-filter').change(function(){
		$('#staff-list').find('div.staff-container').remove();
		getStaff($(this).val());
	});

	$('#search-filter').keyup(function(){
		var search = $(this).val().toLowerCase();
		$('#staff-list>div.staff-container').each(function(){
			$(this).find('.staff-name').text().toLowerCase().indexOf(search) >= 0 ? $(this).show() : $(this).hide();
		});
	});

	$('#filter-reset').click(function(){
		$('#type-filter').prop('selectedIndex',0);
		getStaff('all');
		$('#search-filter').val('');
		$('#staff-list').find('.staff-container').show();
	});

});

function getTypes(){
	for(var i=0; i<types.length; i++)
		$('#type-filter').append($('<option>').attr("value", types[i]).text(types[i]));
}

function getStaff(type){
	$('#staff-list').find('.staff-container').remove();
	for(var i=0; i<staff.length; i++){
		if(type == 'all' || type == staff[i].type){
			$('#staff-list').append($('<div class="staff-container">')
				.append($('<div class="staff-image">').text("image"))
				.append($('<div class="staff-info">')
					.append($('<div class="staff-name">').text(staff[i].name))
					.append($('<div class="staff-position">').text(staff[i].position))
					.append($('<div class="staff-email">').text(staff[i].email))
				)
			);
		}
	}
}