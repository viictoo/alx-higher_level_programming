//  script that fetches and lists the title for all movies
//  by using URL: https://swapi-api.alx-tools.com/api/films/?format=json
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (i, epic) {
      const movie = epic.title;
      const item = $('<li>').text(movie);
      $('#list_movies').append(item);
    });
  });
});

// .ajax version

// $.ajax({
//     url: "https://swapi-api.alx-tools.com/api/films/?format=json",
//     method: "GET",
//     dataType: "json",
//     success: function (data) {
//       $.each(data.results, function (_, epic) {
//         const movie = epic.title;
//         const item = $("<li>").text(movie);
//         $("#list_movies").append(item);
//       });
//     },
//     error: function (error) {
//       console.log("Error: " + error);
//     }
//   });
