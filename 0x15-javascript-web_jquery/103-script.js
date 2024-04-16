$(document).ready(function () {
  const helloElement = $('#hello');
  const userInput = $('#language_code');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const button = $('#btn_translate');

  button.click(function () {
    translate();
  });
