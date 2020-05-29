# assertions are used to indicated unrecoverable errors in the program
# these are meant to check impossible conditions
# assertions can be turned off globally if python is run with -o optimize option
# asserts are not a mechanism  or handling run time errors
# never use assertions for data validation

# price in cents to avoid rounding issues
shoes = {'name': 'Fancy Shoes', 'price': 14900}


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


if __name__ == '__main__':
    print(apply_discount(shoes, 0.25))
    print(apply_discount(shoes, 2.0))

    # This evaluates to true as assert looks at truthy value of the tuple passed, which is always true
    assert (1 == 2, 'This fails')
    assert 1 == 2, 'This fails'
