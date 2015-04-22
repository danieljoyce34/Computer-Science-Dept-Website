$(document).ready(function () {


	$.ajax({url:"http://127.0.0.1:5000/retrieveFaculty/1",success:function(result) {

		var faculty = result['faculty'][0];


		buildProfile(faculty);
	}});

});


function buildProfile (person) {
	$('#profile-header').append($('<div class="card">').text(person['lname'])
		.append($('<img class="profile-image" height="150" width="150" src="https://media.licdn.com/media/p/3/000/2c8/24c/039e2a7.jpg">')));
}