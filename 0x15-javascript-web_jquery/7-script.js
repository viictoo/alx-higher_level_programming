//  script that fetches the character name from
//  URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    success: function (data) {
      const name = data.name;
      $('#character').text(name);
    }
  });
});

//  using .get()
// $(document).ready(function () {
//     // Use the .get() method to make a GET request
//     $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
//       const characterName = data.name;
//       // Display the character name in the #character div
//       $("#character").text("Name: " + characterName);
//     })
//     .fail(function (error) {
//       console.log("Error: " + error);
//     });
//   });
