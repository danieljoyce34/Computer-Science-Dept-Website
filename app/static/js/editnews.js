var baseURL = 'http://127.0.0.1:5000/'

var ncontainer = 'news-container';
var nimg = 'news-image';
var ntitle = 'news-title';


$(document).ready(function(){
	$.ajax({
		url: baseURL + 'retrieveNews',
		dataType:'json',
		success: function(response){
			for(var i=0; i<response.news.length; i++)
				displayNews(response.news[i]);
		}
	});
});

function displayNews(news){
	$('#news-list').append($('<div class="' + ncontainer + '">' )
		.append($('<div class="' + nimg + '">').css('background-image', 'url(https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg)'))
		.append($('<div class="' + ntitle + '">').text(news.headline))
		.append($('<button class="edit-button">').text('Edit'))
	);
}

//$('#divID').css("background-image", "url(/myimage.jpg)");  