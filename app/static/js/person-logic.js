$(document).ready(function () {


	$.ajax({url:"http://127.0.0.1:5000/retrieveFaculty/1",success:function(result) {

		var faculty = result['faculty'][0];


		buildProfile(faculty);
	}});

	generateXJs();

});


function buildProfile (person) {

	$('#profile').append($('<div class="id">')
		.append($('<img class="profile-image" src="https://media.licdn.com/media/p/3/000/2c8/24c/039e2a7.jpg">'))
		.append($('<div class="name">').text(person['fname'] + ' ' + person['minit'] + ' ' +person['lname']))
	);
		//.append($('<img class="profile-image2" src="https://media.licdn.com/media/p/3/000/2c8/24c/039e2a7.jpg">')));


	var educations = "";

	for(eds in person['educations']) {
		educations += person['educations'][eds]['school'] + ", " + person['educations'][eds]['degree'] + "  " + person['educations'][eds]['discipline'] + '\n';
	}



	$('#profile').append($('<div class="bio">').text('education:\n' + educations));
}
//need to be more careful with building this, maybe lots of elements is the way to go?





function generateXJs() {

	var xjs = ["https://media.licdn.com/media/p/3/000/2c8/24c/039e2a7.jpg", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/10482933_815978445079030_88990320408955843_n.jpg?oh=17b68477dc8defcce4ab060da8e4cf3e&oe=55AB907A", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xaf1/t31.0-8/620340_475916059085272_1876076557_o.jpg", 
	"https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xaf1/v/t1.0-9/396732_345755432101336_1242733007_n.jpg?oh=c7634f53428c549eec0f8acd40e7c85f&oe=55AE82A5&__gda__=1440418420_4fabf06e6c23e457498cba5724963098", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/254242_229677483709132_433801_n.jpg?oh=af7864f49bd809b21bf073c5cef6655c&oe=55E1EEEC", 
	"https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-xfa1/v/t1.0-9/251258_229140603762820_5215581_n.jpg?oh=399ceaa35034d24b6a012eb76522cdb8&oe=55E27C91&__gda__=1440630873_cf670849cffdb3c70ae4617001da9dc3", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xpf1/t31.0-8/218925_220219207988293_536842_o.jpg", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-ash2/v/t1.0-9/228159_220217847988429_1426956_n.jpg?oh=fbc09b293b121dda98b5ca161a8a0717&oe=55A74800", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xfa1/v/t1.0-9/264708_1613142426784_3101780_n.jpg?oh=cfadb7d9db83379b6c898729df101d17&oe=55DEF3FE", 
	"https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-xpa1/v/t1.0-9/248308_10150214127764725_721176_n.jpg?oh=9b7e48c673edd5f64e6bae4d2ddbbeac&oe=55A01F6A&__gda__=1437071962_d776b9dcb03bfd71045e6208126a6c38", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/167863_177230075633675_2379063_n.jpg?oh=3223be1c50956c9da57a1fba13d731db&oe=559BE5E5", 
	"https://scontent-iad.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/163249_177231265633556_6805791_n.jpg?oh=de1407ace5c247d07c04bf0f5b499af8&oe=55A98374", ];


	var width = screen.width;
	var height = screen.height;

		$('.profile-image').animate({right: width});
}
