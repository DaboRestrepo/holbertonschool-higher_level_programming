#!/usr/bin/node
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});
