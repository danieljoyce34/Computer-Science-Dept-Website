var acontainer = 'alert-box';
var icon = 'icon ion-ios-alarm-outline';
var acontent = 'alert-content';
var atime = 'alert-time';

$(document).ready(function () {

	var data_container = [ 
		{
			"color" : "General",
			"content" : "Atention all campers, meals are cancelled today due to lack of hustle... deal with it",
			"time" : "12:00AM",
			"who" : 11
		},
		{
		"color" : "Warning",
		"content" : "I'm affraid I can't let you do that",
		"time" : "5:00PM",
		"who" : 22
		},
		{
		"color" : "Abrupt Comment",
		"content" : "Imma let you finish, but Beyonce had the best web-page ever",
		"time" : "4:00PM",
		"who" : 33
		},
		{
		"color" : "Colloquiums",
		"content" : "All Colloquiums are cancelled today",
		"time" : "3:00PM",
		"who" : 44
		},
		{
		"color" : "Warning",
		"content" : "Take that causality!",
		"time" : "11:00AM",
		"who" : 55
		}, 
		{
		"color": "class",
		"content": "Dr. Ways class has been cancelled",
		"time": "12:30PM",
		"who": 12
		},
		{
		"color": "meeting",
		"content": "Bansai Gardening club meeting today!",
		"time": "1:30PM",
		"who": 55
		},
		{
		"color": "colloqium",
		"content": "Former totalitarian dictator Stalin giving colloqium in room M292",
		"time": "4:30PM",
		"who": 122
		},
		{
		"color": "reschedule",
		"content": "All classes pushed back to tomorrow",
		"time": "2:30PM",
		"who": 1
		},
		{
		"color": "club",
		"content": "Rom com club meeting tomorrow",
		"time": "12:30PM",
		"who": 15
		},
		{
		"color" : "colloqium",
		"content" : "Colloqium today at 4:30 in Mendel 115",
		"time" : "2:30PM",
		"who" : 1234
		},
		{
		"color":"class",
		"content" : "Graduate Computer Vision Course has been cancelled tonight",
		"time" : "2:30PM",
		"who" : 123
		},
		{
		"color":"meeting",
		"content":"CAVE Crew meeting tomorrow at 2:30pm in Mendel 292",
		"time":"2:30PM",
		"who": 111
		},
		{
		"color":"reschedule",
		"content":"Colloqium scheduled for today has been rescheduled for next week",
		"time":"2:30PM",
		"who":134
		},
		{
		"color":"meeting",
		"content":"There is some kind of meeting",
		"time":"2:30PM",
		"who":234
		}
	];

	// Add alerts from json file
	for (var i = 0; i < data_container.length; i++) {
		addAlert(data_container[i]['color'], data_container[i]['content'], data_container[i]['time']);
	}

	// Shows/hides time on hover over clock icon
	// For mobile devices use on click and check if time is hidden
	$(document).on("mouseenter", "i.icon", function(event){
		$(this).parent().find($('div.' + atime)).show();
		$(this).parent().find($('div.' + acontent)).css('margin-left', '110px');	
	});
	$(document).on("mouseleave", "i.icon", function(event){
		$(this).parent().find($('div.' + atime)).hide();
		$(this).parent().find($('div.' + acontent)).css('margin-left', '35px');			
	});
});


// Adds a new alert to the alert container
function addAlert(color, text, time){
	$('.alert-container').append($('<div class="' + acontainer + '">')
		.append($('<i class="' + icon + '" title="' + time + '">'))
		.append($('<div class="' + atime + '">').text(time))
		.append($('<div class="' + acontent + '">').text(text))
	);
}
