function increase(id, price){
  var this_ = $(this)
  $.ajax({
    url: '/increase-order-item/' + id,
    method: "get",
    data: {},
    success: function(data){

      let id_quantity = '#id' + id + '_quantity'
      $(id_quantity).val(parseInt($(id_quantity).val()) + 1)
      $('#count').text(parseInt($('#count').html()) + 1)
      console.log(price)
      $('#price').text((parseFloat($('#price').html()) + price).toFixed(2))

    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
}

function decrease(id, price){
  let item_id = "#item_" + id
  var this_ = $(this)
  $.ajax({
    url: '/decrease-order-item/' + id,
    method: "get",
    data: {},
    success: function(data){

      let id_quantity = '#id' + id + '_quantity'
      $(id_quantity).val(parseInt($(id_quantity).val()) - 1)
      $('#count').text(parseInt($('#count').html()) - 1)
      $('#price').text((parseFloat($('#price').html()) - price).toFixed(2))


      if ($(id_quantity).val() == '0'){
        $(item_id).addClass("hidden")
        let deleted_item = document.getElementById(item_id)
        let start = false
        $(".item").each(function( index ) {
          if ($(this).hasClass("hidden")){
            start = true
          } else {
            if (start){
              $(this).addClass("move-up")
              $(this).on(
                "animationend MSAnimationEnd webkitAnimationEnd oAnimationEnd",
                function() {
                  $(this).removeClass("move-up");
                  $(".hidden").remove()
                }
              );

            }
          }
        });
      }


    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
}

function delete_(id, price){
  var this_ = $(this)
  $.ajax({
    url: '/delete-order-item/' + id,
    method: "get",
    data: {},
    success: function(data){
      let quantity = parseInt($('#id' + id + '_quantity').val())
      $('#count').text(parseInt($('#count').html()) - quantity)
      $('#price').text((parseFloat($('#price').html()) - quantity*price).toFixed(2))
      let item_id = "#item_" + id
      $(item_id).addClass("hidden")
      let deleted_item = document.getElementById(item_id)
      let start = false
      $(".item").each(function( index ) {
        if ($(this).hasClass("hidden")){
          start = true
        } else {
          if (start){
            $(this).addClass("move-up")
            $(this).on(
              "animationend MSAnimationEnd webkitAnimationEnd oAnimationEnd",
              function() {
                $(this).removeClass("move-up");
                $(".hidden").remove()
              }
            );

          }
        }
      });
    }, error: function(error){
      console.log(error)
      console.log("error")

    }
  })
}
