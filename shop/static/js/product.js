function choose_size(size){
  $('.size').each(function(i, obj) {
    var this_ = $(this)
    if (this_.hasClass("chosen")){
      this_.removeClass("chosen")
    }
    if (this_.attr('id') == ("size_"+size)){
      this_.addClass("chosen")
      $('#input-size').val(size)
    }
  });
}

if (document.getElementById('size_m')){
  choose_size('m')
} else {
  choose_size('one size')
}

function scrollSmoothTo(elementId) {
  var element = document.getElementById(elementId);
  element.scrollIntoView({ block: 'start',  behavior: 'smooth' });
}
