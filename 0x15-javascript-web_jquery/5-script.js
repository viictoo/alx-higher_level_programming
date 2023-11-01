// create a new list item element with the content "Item."
//      $(document).ready(function) is a best practice
//      to ensure that your JavaScript code is executed
//      at the right time, after the DOM is fully loaded
//      and ready for interaction, which prevents issues
//      related to manipulating elements that aren't yet
//      available in the DOM.
$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });
});

// $("#add_item").click(function(){
//     $(".my_list").append("<li>Item</li>");
// });
