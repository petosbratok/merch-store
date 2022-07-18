$(window).scroll(function(){
  var window_height = $(window).innerHeight()

  var a = 100;
  var pos = $(window).scrollTop();
  if(pos > a) {
      $("header").css({
                  background: 'black'
              });
  }
  else {
      $("header").css({
                  background: 'none',
              });
  }
  if(pos > (window_height-70)) {
      $(".filter").css({
                  position: 'fixed',
                  top: '120px',
              });
  }
  else {
      $(".filter").css({
                  position: 'absolute',
                  top: 'auto',
              });
  }
});

function filter(type){
  $('.good').each(function(i, obj) {
    if (!obj.classList.contains(type)){
      obj.style.display = "none";
    } else {
      obj.style.display = "block";
    }
});
}

function scrollSmoothTo(elementId) {
  var element = document.getElementById(elementId);
  element.scrollIntoView({ block: 'start',  behavior: 'smooth' });
}
