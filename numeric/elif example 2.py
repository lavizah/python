m1=int(input('m1:'))
m2=int(input('m2:'))
m3=int(input('m3:'))
m4=int(input('m4:'))
m5=int(input('m5:'))
total=m1+m2+m3+m4+m5
per=(total/500)*100
print('total:',total)
print('per:',per)

if per>=85:
    print('A+')
elif per>=75 and per<85:
    print('A')
elif per>=60 and per<75:
    print('B')
elif per>=45 and per<60:
    print('C')
elif per>=35 and per<45:
    print('D')
else:
    print('F')
    
