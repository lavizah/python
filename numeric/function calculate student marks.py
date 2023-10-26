
def cal_marks(name,rollno,m1,m2,m3,m4,m5):
    print('Name: ',name)
    print('Rollno: ',rollno)
    total=m1+m2+m3+m4+m5
    print('total',total)
    per=(total/500)*100
    print('percentage',per)

name=input('name:')
rollno=int(input('rollno:'))
m1=int(input('m1:'))
m2=int(input('m2:'))
m3=int(input('m3:'))
m4=int(input('m4:'))
m5=int(input('m5:'))
cal_marks(name,rollno,m1,m2,m3,m4,m5)
