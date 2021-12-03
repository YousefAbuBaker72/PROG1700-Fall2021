



tons = float(input("enter the amount of tons :"))
stone = float(input("enter the amount of stone :"))
pounds = float(input("enter the amount of pounds :"))
ounces = float(input("enter the amount of ounces :"))



total_ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
kilos = total_ounces / 35.274
metric_tons =  kilos / 1000

print("Imperial To Metric Conversion")


print("the total ounces are : {0:.4F} " .format(total_ounces))
print("The total kilos are : {0:.4f}" .format( kilos ))
print("The total metric tons :{0:.4F} " .format( metric_tons))





