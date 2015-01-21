// contents of this script serve the purpose of handling jQuery events

$('li.dropdown').hover(function () {
	$(this).addClass('open');
}, function () {
	$(this).removeClass('open');
});