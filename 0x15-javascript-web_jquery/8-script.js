const moviesList = $('#list_movies');

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.ajax({
  type: 'GET',
  url,
  beforeSend: function () {
    $('header').append('<p>Loading movies ...</p>');
  },
  success: function (movies) {
    $('header').find('p').remove();
    $.each(movies.results, function (i, movie) {
      moviesList.append('<li>' + movie.title + '</li>');
    });
  }
});
