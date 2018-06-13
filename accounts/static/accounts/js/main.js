/*
function setStyleSheet(url) {
  var stylesheet = document.getElementById("stylesheet2");
  stylesheet.setAttribute('href', url);
}
*/


function lightswitch() {
  var $body = $("body");
  $body.toggleClass("dark-mode");
  if($('body').hasClass('dark-mode')){
        localStorage.setItem('theme', 'dark-mode');
        var theme = localStorage.getItem('theme');
        $('body').addClass(theme);
        $('div[class^="card bg-light mb-3"]').removeClass('card bg-light mb-3').addClass('card text-white bg-dark mb-3');
        $('nav[class^="navbar navbar-expand-lg navbar-light bg-light"]').removeClass('navbar navbar-expand-lg navbar-light bg-light').addClass('navbar navbar-expand-lg navbar-dark bg-dark');

    }

    else {
    localStorage.removeItem('theme', 'dark-mode');
        var theme = localStorage.getItem('theme');
        $('body').addClass(theme);
        $('div[class^="card text-white bg-dark mb-3"]').removeClass('card text-white bg-dark mb-3').addClass('card bg-light mb-3')
        $('nav[class^="navbar navbar-expand-lg navbar-dark bg-dark"]').removeClass('navbar navbar-expand-lg navbar-dark bg-dark').addClass('navbar navbar-expand-lg navbar-light bg-light')

  }
}

$(document).ready(function(){
    var theme = localStorage.getItem('theme');
    $('body').addClass(theme);
    if($('body').hasClass('dark-mode')){
        $('div[class^="card bg-light mb-3"]').removeClass('card bg-light mb-3').addClass('card text-white bg-dark mb-3');
        $('nav[class^="navbar navbar-expand-lg navbar-light bg-light"]').removeClass('navbar navbar-expand-lg navbar-light bg-light').addClass('navbar navbar-expand-lg navbar-dark bg-dark');
    }
})
