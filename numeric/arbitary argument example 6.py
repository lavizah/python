def f1(*args):
    print(args)

f1(1,2,3,4,5)

print()
list1=[1,2,3,4,5]
list2=[80,60,70,90,10]
list3=['Ashfiya','Lavizah']

f1(list1,list2,list3)

print()

dict1={
    'name':'Ashfiya',
    'skill':['Python','java','c']
    }

dict2={
    'name':'Lavizah',
    'skill':['Python','java','c','.net']
    }

f1(dict1,dict2,)


list4=[x for x in range(10)]
print('list4:',list4)

f1(list4)
