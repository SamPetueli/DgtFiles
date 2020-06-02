amount_of_pizzas = float(input("How many pizzas would you like to order?"))
pizza_price = 12.50
delivery = 7
order_price = (pizza_price * amount_of_pizzas) + delivery
print("Your order will cost ${}.".format(order_price))
if amount_of_pizzas >=4:
    discounted_order_price = order_price - delivery
    print("Since you are ordering more than three pizzas, the delivery will be free of charge.")
    print("The total order price now comes to ${}.".format(discounted_order_price))
