from string import Template

class MyTempalte(Template):
    dalimiter = "#"

def Main():
    cart = []

    cart.append(dict(item = "Books", price = 90, qty = 5))
    cart.append(dict(item = "Mobile", price = 100, qty = 100))
    cart.append(dict(item = "Laptop", price = 100, qty = 2))
    cart.append((dict(item = "i-pad", price = 300, qty = 3)))

    cart_template = MyTempalte("qty x item = price")
    total = 0

    print("My cart :")

    for cart_data in cart:
        print(cart_template.substitute(cart_data))
        total += cart_data["price"]
        print("Total Price:" + str(total))

if __name__ == '__main__':
    Main()

