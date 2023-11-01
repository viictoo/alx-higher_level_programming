// script that updates the text color of the <header> element to red (#FF0000):
$('header').css('color', 'red');
$('header').click(function () {
  $('footer').add('span').add('textarea').css('background', 'red').text('Click Here').animate({ width: '40px' }, 500);
});
$('footer').click(function () {
  $('footer').add('span').add('textarea').css('background', 'white').text('BOO!');
  $('header').add('span').add('textarea').css('background', 'white').text('');
});
