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

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function uuidv2() {
  return 'xxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}




let order_id = getCookie('order_id')

if (order_id == null || order_id == undefined){
  order_id = uuidv2()
}

document.cookie = 'order_id=' + order_id + ";domain=;path=/"

function scrollSmoothTo(elementId) {
  var element = document.getElementById(elementId);
  element.scrollIntoView({ block: 'start',  behavior: 'smooth' });
}
