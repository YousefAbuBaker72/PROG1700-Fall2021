country_name=input("enter your country")
cost_order=int(input("enter your order's cost"))
def PriceWithTax():
  if country_name.lower()== "canada" :
    province_name=input("enter your province")
    if province_name.lower()=="alberta":
        total_order= cost_order+((5/cost_order)*100)
    elif province_name.lower()=="ontario" or "ns" or "nb":
        total_order= cost_order+((15/cost_order)*100)
    else:
        total_order=  total_order= cost_order+((11/cost_order)*100)
  else: total_order = cost_order
  return total_order
total_order=PriceWithTax()
print("your total order is %s"%total_order)

   
    


