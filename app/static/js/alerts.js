var acontainer = 'alert-box',
	 	icon = 'icon ion-ios-alarm-outline',
	 	acontent = 'alert-content',
	 	atime = 'alert-time';

$(document).ready(function () {

	getAlerts();

	// Add alerts from temp json file
	//for (var i = 0; i < data_container.length; i++) {
	//	addAlert(data_container[i]['color'], data_container[i]['content'], data_container[i]['time']);
	//}

	// Shows/hides time on hover over clock icon
	// For mobile devices use on click and check if time is hidden
	$(document).on("mouseenter", "i.icon", function(event){
		$(this).parent().find($('div.' + atime)).show();
		$(this).parent().find($('div.' + acontent)).css('margin-left', '175px');	
	});

	$(document).on("mouseleave", "i.icon", function(event){
		$(this).parent().find($('div.' + atime)).hide();
		$(this).parent().find($('div.' + acontent)).css('margin-left', '35px');			
	});

});

 // Adds a new alert to the alert container
function addAlert(color, text, time){
	$('.alert-container').append($('<div class="' + acontainer + " " + color + '">')
		.append($('<i class="' + icon + '" title="' + time + '">'))
		.append($('<div class="' + atime + '">').text(time))
		.append($('<div class="' + acontent + '">').text(text))
	);
}

// Adds alerts from json file
function getAlerts(){
	$.ajax({
		url: 'http://localhost:5000/retrieveAlerts',
		type: 'GET',
		dataType: 'json',
		success: function(data){
			$.each(data.alerts, function(i,obj){
				// Could use better formatting
				var date = new Date(obj.start_date);
				var formattedDate = (date.getMonth()+1) + "/" + date.getDate() + " " + date.toLocaleTimeString();
				addAlert(obj.category, obj.content, formattedDate);
			});
		},
		error: function(err){console.log(err);}
	});
}