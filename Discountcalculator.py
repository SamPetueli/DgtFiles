def force_number(message):
      while True:
        try:
          number = float(input(message))
          break
        except ValueError:
          print("Please enter a number!")


def calc_discount(price, discount):
    discount_value = discount / 100
    discounted_price = price * discount_value
    new_price = price - discounted_price
    print("The price now comes to ${}".format(new_price))
    print("You have saved ${}!".format(discounted_price))
    
price = float(input("Enter a price for the program to discount"))
discount = float(input("Now enter a value that will discount from the original price"))
calc_discount(price, discount)

