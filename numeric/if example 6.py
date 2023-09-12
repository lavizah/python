basic_salary=int(input('basic_salary:'))
if basic_salary<1500:
    hra=basic_salary*(10/100)
    da=basic_salary*(90/100)
    gs=basic_salary+hra+da
    print('Gross salary:',gs)
else:
    hra=500
    da=basic_salary*(98/100)
    gs=basic_salary+hra+da
    print('Gross salary:',gs)
