var=99
def local():
    var=0
    
def glob1():
    global var
    var+=1

def glob2():
    var=0
    import thismod
    thismod.var+=1

def test():
    print(var)
    glob1()
    print('after glob1 call:var',var)
    glob2()
    print('after glob2 call:var',var)

test()
    
