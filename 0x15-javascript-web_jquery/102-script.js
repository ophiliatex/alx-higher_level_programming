$(document).ready(function () {
  const helloElement = $('#hello');
  const userInput = $('#language_code');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const button = $('#btn_translate');

  button.click(function () {
    const lanValue = userInput.val();
    const requestUrl = url + lanValue;

    $.ajax({
      type: 'GET',
      url: requestUrl,
      beforeSend: function () {
        helloElement.append('<p>Loading translation</p>');
      },
      success: function (hello) {
        if (helloElement.has('p')) {
          helloElement.children('p').remove();
        }
        helloElement.append('<p>' + hello.hello + '</p>');

        console.log(hello);
      }
    });
  });
});
