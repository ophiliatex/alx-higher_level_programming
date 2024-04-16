const toggleHeader = $('#toggle_header');
const headerElement = $('header');
const initialColor = headerElement.css('color');
toggleHeader.click(function () {
  const color = headerElement.css('color');
  if (color === initialColor) {
    headerElement.css('color', '#FF0000');
  } else {
    headerElement.css('color', initialColor);
  }
});
