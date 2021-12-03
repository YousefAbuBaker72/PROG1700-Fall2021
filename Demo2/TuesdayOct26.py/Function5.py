def claculateTax(price,taxRate):
    result= price*taxRate #result is a local variable
    return result

productPrice = float(input("Enter the product price"))
theTax = float(input("Enter the tax rate : "))
totalPrice = claculateTax(productPrice, theTax)
print("The product's price after tax is {0:.2f}".format(totalPrice))

productOnePrice = float(input("Enter the product price"))
theTax = float(input("Enter the tax rate : "))
totalPrice = claculateTax(productOnePrice, theTax)
print("The product's price after tax is {0:.2f}".format(totalPrice))