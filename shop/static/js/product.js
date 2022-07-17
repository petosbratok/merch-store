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


function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}




let device = getCookie('device')
let order_id = getCookie('order_id')

if (device == null || device == undefined){
  device = uuidv4()
}

if (order_id == null || order_id == undefined){
  order_id = uuidv4()
}

document.cookie = 'device=' + device + ";domain=;path=/"
document.cookie = 'order_id=' + order_id + ";domain=;path=/"

function scrollSmoothTo(elementId) {
  var element = document.getElementById(elementId);
  element.scrollIntoView({ block: 'start',  behavior: 'smooth' });
}
