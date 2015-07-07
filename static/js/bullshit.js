function slowDecorate() {
    var timeout = 400,
    time_per_block = 550;
    var spans = $(".highlight span")
    var timeout_amount = Math.max(time_per_block / spans.length, 2);
    console.log(spans.length + " found for highlighting.")

    spans.each(function() {
        console.log(timeout);
        timeout += timeout_amount;
        var span = $(this);
        setTimeout(function() {
            span.addClass('animate');
        }, timeout)
    });
}

function bannerSize(startingSize) {
      var scrollTop = $(window).scrollTop();
      scrollRemaining = startingSize - scrollTop;
      size = (scrollRemaining / 5) - 10;
      if (size < 1) {
        size = 0  // Some browsers don't like very small or negative font sizes.
      }
      $('#banner-title').css('font-size', size + "px");
    }


function textColor() {
  var scrollTop = $(window).scrollTop();
  var totalHeight = document.body.scrollHeight;

  if (scrollTop < (totalHeight / 2) - 200) {
    $('#page-wrapper').css('color', '#FCAC5B').css('text-shadow', '1px 1px 1px black');
  } else {
    $('#page-wrapper').css('color', '#4F2800').css('text-shadow', '0px 0px 1px #86969C');
  }

  if (scrollTop < (totalHeight / 2) - 200) {
    $('#page-wrapper a').css('color', '#C7BFBF');
  } else {
    $('#page-wrapper a').css('color', '#6166FF');
  }
  if (scrollTop < (totalHeight / 2) - 200) {
    $('h2, h3, h4, h5, h6, .h2, .h3, .h4, .h5, .h6').css('color', '#C7BFBF');
  } else {
    $('h2, h3, h4, h5, h6, .h2, .h3, .h4, .h5, .h6').css('color', '#593E22');
  }
}


  $(document).ready(function() {
  bannerSize();
  textColor();

    $('#twitter-handles a').hover(
        function() {
            $(this).addClass('hover');
        }, function() {
            $(this).removeClass('hover');
        }
    );

    $(window).scroll(function() {
      if (album != true) {
        bannerSize(heroFontSize);
      }

      textColor();
    });
  bannerSize(heroFontSize);
  slowDecorate();

});

//Swipebox

;( function( $ ) {

	$( '.swipebox' ).swipebox();

} )( jQuery );