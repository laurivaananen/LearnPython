

try:
    impossible = 5 / 0
    print("This is not possible")
except ZeroDivisionError:
    print("Can't divide by zero")


short_list = [0, 1, 2]

try:
    fourth_item = short_list[3]
    print(fourth_item)
except IndexError:
    print("Too short list")