from collections import namedtuple

Product = namedtuple('Product', 'name price')

class ShoppingBasket:

    def __init__(self, items=[]):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        return ShoppingBasket(self._items + other._items)

    def __repr__(self):
        return f"ShoppingBasket([{self._items}])"

    def __str__(self):
        return "ShoppingBasket({})".format([(x.name, x.price) for x in self._items])

    
class Register:

    def __init__(self):
        self._bank = None
        self.basket = None
        self.bills = (500, 200, 100, 50, 20, 10, 5, 2, 1)

    def payment(self, basket):
        self.basket = basket

    def give_change(self, total):
        left_to_give = total
        change = {}
        for bill in self.bills:
            while bill < left_to_give:
                change[bill] = change.get(bill, 0) + 1
                left_to_give -= bill
        return change
    
    def receipt(self):
        for product in self.basket._items:
            print("{:20}{:>4}".format(*product))
        total = sum(x[1] for x in self.basket._items)
        print('-'*22)
        print("{:20}{:>4}".format("Total price", total))
        print("{:*^24}".format("Thank you"))
        change = self.give_change(total)
        print("\nHere is your change\n")
        for money, amount in change.items():
            print("{:4} x {:>}".format(money, amount))
        self.basket = None

if __name__ == '__main__':

    my_basket = ShoppingBasket(
        [Product('Apple', 5),
         Product('Grapefruit', 90)]
    )

    gift_basket = ShoppingBasket(
        [Product('Chocolate', 2),
         Product('Coffee', 100)]
    )

    stolen_basket = my_basket + gift_basket

    print(stolen_basket)

    supermarket = Register()
    supermarket.payment(stolen_basket)
    supermarket.receipt()