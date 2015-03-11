$(document).ready(function () {
	var image_container = $('.active-image'),
		current_title = $('.active-title');

	var data_container = [ 
		{
			"img_url": "https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg",
			"title": "XJ's head gets swapped with a phone",
			"description": "very tragic",
			"story_url": "localhost:5000/"
		},
		{
			"img_url": "https://s-media-cache-ak0.pinimg.com/236x/a7/03/af/a703afab4ddbad8138fe1bd103133861.jpg",
			"title": "David puts a space before parenthesis",
			"description": "When interviewed he claimed 'its not that uncommon'",
			"story_url": "localhost:5000/carousel"
		},
		{
			"img_url": "https://unsplash.imgix.net/uploads/1413386993023a925afb4/4e769802?q=75&fm=jpg&s=84dfb097d39ff1600cdd32be44813650",
			"title": "Some random title",
			"description": "Some random words that make up a description",
			"story_url": "localhost:5000/alerts"
		},
		{
			"img_url": "https://unsplash.imgix.net/photo-1423439793616-f2aa4356b37e?q=75&fm=jpg&s=3b42f9c018b2712544debf4d6a4998ff",
			"title": "Another random title",
			"description": "Another description can go here and in this case its really really really really really really really long",
			"story_url": "localhost:5000/"
		}
	];

	function cycleImages(images) {
		var i = 0,
			max = images.length;                     

		setInterval(function () { 
			i++;
			if (i > (max - 1))
				i = 0;
			
			swapImage(images[i]['img_url']);
			swapTitle(images[i]['title'], images[i]['description']);
		}, 5000);
	}

	function swapImage(url) {
		url = "url(" + url + ")"; 
		image_container.css('background-image', url);
	}

	function swapTitle(title, subtitle) {
		var contents = title + '<br>' 
			+ '<i class="active-description">' + subtitle + '<i>';
		current_title.html(contents);
	}

	cycleImages(data_container);
});

