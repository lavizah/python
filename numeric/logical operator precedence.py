a1=4
a2=8
a3=-5
a4=7
a5=4
a6=-2

print('Logical Operator precedence')
print('a1=',a1,'a2=',a2,'a3=',a3,'a4=',a4,'a5=',a5,'a6=',a6)
result1=not a4>=a2 and a5==a1 or a3<=a4
print('result1=not a4>=a2 and a5==a1 or a3<=a4',result1)
result2=a3*a5//a1>=a6+a1 and a5/a3%a1<=a6-a8
print('result2=a3*a5//a1>=a6+a1 and a5/a3%a1<=a6-a8',result2)
result3=not (a4%a1+a2==a5*a6 or a2//a3*a6!=a1/a2)
print('result3=not (a4%a1+a2==a5*a6 or a2//a3*a6!=a1/a2)')
result4=a3+a6*a1<a3/a5 or a2//a4*a6>=a1%a4 and a5>a6
print('result4=a3+a6*a1<a3/a5 or a2//a4*a6>=a1%a4 and a5>a6',result4)
result5=a5>=a1 or a4<=a6 and a4==a5
print('result5=a5>=a1 or a4<=a6 and a4==a5',result5)
result6=a3//a6+a1<=a4%a1 and a4*a6/a1!=a3-a2
print('result6=a3//a6+a1<=a4%a1 and a4*a6/a1!=a3-a2',result6)
result7=not (a5+a3*a1>=a5//a1 or a4/a2==a6%a3)
print('result7=not (a5+a3*a1>=a5//a1 or a4/a2==a6%a3)',result7)
result8=a3//a1+a5<=a4%a2 and a4/a3-a1==a2*a6
print('result8=a3//a1+a5<=a4%a2 and a4/a3-a1==a2*a6',result8)


