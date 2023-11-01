/// a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

//      The new element must be: <li>Item</li>
//      The new element must be added to UL.my_list
//      When the user clicks on DIV#add_item: a new element is added to the list
//      When the user clicks on DIV#remove_item: the last element is removed from the list
//      When the user clicks on DIV#clear_list: all elements of the list are removed
$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });

  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
