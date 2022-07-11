var order = JSON.parse(sessionStorage.getItem('order'))
if (!order){
  order = []
}

function add_to_cart(item_id){
  order.push(item_id)
  sessionStorage.setItem('order', JSON.stringify(order))
  console.log("new order: ", order)
}
