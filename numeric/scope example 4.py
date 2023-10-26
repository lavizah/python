x=99

def func():
    global x
    x=2
    print('x:',x)

func()
print('x:',x)
