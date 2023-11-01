// script that fetches and prints how to say “Hello” depending on the language

// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
// The translation of “Hello” must be displayed in the HTML tag DIV#hello

$(document).ready(() => {
  function translateFn () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const cc = $('#language_code').val();
    $.get(url + cc, function (data) {
      $('#hello').html(data.hello);
    });
  }
  $('#btn_translate').click(() => { translateFn(); });
  $('#language_code').keypress((event) => {
    if (event.which === 13) { translateFn(); }
  });
  $('INPUT#language_code').focus(() => { translateFn(); });
});
