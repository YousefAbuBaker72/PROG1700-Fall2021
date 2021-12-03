def calculateTax(price):
    productWithTax = price*1.15
    return productWithTax

productPrice = float(input("Enter thr product's price: $"))
totalCost=calculateTax(productPrice)
print("The product price is ${0:.2f}".format(totalCost))
