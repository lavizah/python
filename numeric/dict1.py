dict1={
    'name':'lavizah',
    'mobile':9987252302,
    'age':20,
    'skill':['python','java','html'],
    'hobbies':['reading','cycling'],
    'school':{
            'ssc':'msb',
            'hsc':'msb',
            'ty':'uom',
        }, 
    }
print('dict1=',dict1,len(dict1))
a1=dict1['name']
print('a1=',a1)
a2=dict1['mobile']
print('a2=',a2)
a3=dict1['age']
print('a3=',a3)
a4=dict1['skill'][-1]
print('a4=',a4)
a5=dict1['hobbies']
print('a5=',a5)
a6=dict1['school']['ty']
print('a6=',a6)
print()
dict2={
    'name':'ashfiya',
    'mobile':983345838,
    'age':20.6,
    'skill':['python','java','html','c++'],
    'job':'jr. programmer',
    'salary':80000,
    'hobbies':['reading','singing'],
    
    }
print('dict2=',dict2,len(dict2))
a7=dict2['skill'][1]
print('a7=',a7)
a8=dict2['hobbies'][-1]
print('a8=',a8)
a9=dict2['job'][4:7]
print('a9=',a9)
a10=dict2['salary']
print('a10=',a10)
