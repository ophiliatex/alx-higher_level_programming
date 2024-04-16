$(document).ready(function () {
  const listElement = $('.my_list');
  const addElement = $('div#add_item');
  const removeElement = $('div#remove_item');
  const clearElement = $('div#clear_list');

  addElement.click(function () {
    listElement.append('<li>Item</li>');
  });

  removeElement.click(function () {
    listElement.children('li').last().detach();
  });

  clearElement.click(function () {
    listElement.empty();
  });
});
