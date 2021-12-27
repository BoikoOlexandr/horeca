jQuery(document).ready(function($){
          $('#slow_nav ').hover(
              function () {
                  $('ul', this).stop().slideDown(400);
              },
              function () {
                  $('ul', this).stop().slideUp(400);
              }
          );
      });