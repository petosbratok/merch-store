function increase(id, price){
  var this_ = $(this)
  $.ajax({
    url: '/increase-order-item/' + id,
    method: "get",
    data: {},
    success: function(data){

      let id_quantity = '#id' + id + '_quantity'
      $(id_quantity).text(parseInt($(id_quantity).html()) + 1)
      $('#count').text(parseInt($('#count').html()) + 1)
      $('#price').text((parseFloat($('#price').html()) + price).toFixed(2))

    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
}

function decrease(id, price){
  var this_ = $(this)
  $.ajax({
    url: '/decrease-order-item/' + id,
    method: "get",
    data: {},
    success: function(data){

      let id_quantity = '#id' + id + '_quantity'
      $(id_quantity).text(parseInt($(id_quantity).html()) - 1)
      $('#count').text(parseInt($('#count').html()) - 1)
      $('#price').text((parseFloat($('#price').html()) - price).toFixed(2))


      if ($(id_quantity).html() == '0'){
        let item_id = "#item_" + id
        $(item_id).hide()
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
      let quantity = parseInt($('#id' + id + '_quantity').html())
      $('#count').text(parseInt($('#count').html()) - quantity)
      $('#price').text((parseFloat($('#price').html()) - quantity*price).toFixed(2))
      let item_id = "#item_" + id
      $(item_id).hide()
    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
}
