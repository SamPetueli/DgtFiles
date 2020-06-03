def calc_area(length, width):
    area = length * width
    print("The area is: {}cm²".format(area))

length = float(input("What is the length of the rectangle in cm?"))
width = float(input("What is the width of the rectangle in cm?"))
calc_area(length, width)
