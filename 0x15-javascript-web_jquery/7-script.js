const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const characterElement = $('#character');
$.ajax({
  url,
  type: 'GET',
  beforeSend: function () {
    characterElement.append('<p>Loading Character</p>');
  },
  success: function (ch) {
    characterElement.find('p').remove();
    characterElement.append('<p>' + ch.name + '</p>');
  }
});
