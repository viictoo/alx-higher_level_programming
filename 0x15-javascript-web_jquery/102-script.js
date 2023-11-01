// script that fetches and prints how to say “Hello” depending on the language
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const cc = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + cc, (data) => {
      $('#hello').html(data.hello);
    });
  });
});

// $(document).ready(function () {
//     $("#btn_translate").click(function (event) {
//       event.preventDefault(); // Prevent the default form submission behavior
