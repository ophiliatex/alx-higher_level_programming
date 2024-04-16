$(document).ready(function () {
  const helloElement = $('#hello');

  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    beforeSend: function () {
      helloElement.append('<p>Loading Translation</p>');
    },
    success: function (data) {
      helloElement.find('p').remove();
      helloElement.append('<p>' + data.hello + '</p>');
    }
  });
});
