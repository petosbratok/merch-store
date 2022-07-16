function choose_size(size){
  $('.size').each(function(i, obj) {
    var this_ = $(this)
    console.log(this_)
    if (this_.hasClass("chosen")){
      this_.removeClass("chosen")
    }
    if (this_.attr('id') == ("size_"+size)){
      this_.addClass("chosen")
      $('#input-size').val(size)
    }
  });
}

choose_size('m')
