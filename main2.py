from database import Product

try:
    product_name = input('enter product name\n')
    product_quantity = input('enter product quantity\n')
    product_price = input('enter product price\n')
    Product.create(name=product_name, quantity=product_quantity, price=product_price)
    print('Data saved successfully')
except:
    print('Sorry an error occured')
