const addElement = $('#add_item');
const listElement = $('.my_list');

addElement.click(function () {
  listElement.append('<li>Item</li>');
});
