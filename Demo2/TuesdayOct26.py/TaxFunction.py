def claculateTax(price):
    result= price*1.15
    return result

productPrice = float(input("Enter the product price"))
totalPrice = claculateTax(productPrice)
print("The product's price after tax is {0:.2f}".format(totalPrice))

productOnePrice = float(input("Enter the product price"))
totalPrice = claculateTax(productOnePrice)
print("The product's price after tax is {0:.2f}".format(totalPrice))


