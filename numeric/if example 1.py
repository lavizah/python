quantity=int(input('quantity:'))
price=int(input('price:'))
total=quantity*price
if total>1000:
    final_total=total-(total*(10/100))
    print('final_total',final_total)
else:
    final_total=total
    print('final_total',final_total)

    

