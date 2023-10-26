def f1(*args):
    print(len(args))
    print(args)

f1(1,2,3,20,30,40,50,60,70,80,90,10)


def f2(**args):
    print(args)

f2(name='lavizah',age=21,mobile=9987257302)
