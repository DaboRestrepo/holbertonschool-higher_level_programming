#!/usr/bin/node
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const arr = data.results;
  $.each(arr, (key, value) => {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
