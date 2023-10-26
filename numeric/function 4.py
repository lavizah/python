def factorial (num):
    result=1
    for i in range(num,0,-1):
        result=result*i
    print('result:',result)
while True:
    num=int(input('num:'))
    factorial(num)
    
