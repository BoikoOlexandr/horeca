      jQuery(document).ready(function($){
          $('#slow_nav img.menu').click(
              function () {
                  $('#slow_nav ul.super-category').slideToggle()
              }
          );
          $('#slow_nav ul>li.super-category').hover(
              function () {
                  $('ul.category', this).slideToggle(speed=50)
              }
          )
      });