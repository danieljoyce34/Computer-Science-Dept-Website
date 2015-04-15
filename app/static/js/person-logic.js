$(document).ready(function () {


	$.ajax({url:"http://127.0.0.1:5000/retrieveFaculty/1",success:function(result) {

		var faculty = result['faculty'][0];


		buildProfile(faculty);
	}});

});


function buildProfile (person) {
	$('#profile-header').append($('<div>').text(person['lname'])
		);
}