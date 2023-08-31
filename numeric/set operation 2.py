#set operation
s1={1,2,3,4}
print('s1=',s1,len(s1))
s2=set()
print('s2=',s2,len(s2))

print()
print('add')
s2.add(1)
print('s2=',s2,len(s2))
s2.add(354)
print('s2=',s2,len(s2))
s2.add(355)
s2.add(356)
print('s2=',s2,len(s2))

print()
print('copy')
s3=s2.copy()
print('s3=',s3,len(s3))

print()
print('discard')
s2.discard(356)
print('s2=',s2,len(s2))
s2.discard(365)
print('s2=',s2,len(s2))

print()
print('pop')
s4=s1.pop()
print('s1=',s1,len(s1),s4)
s5=s2.pop()
print('s2=',s2,len(s2))

print()
print('Remove')
s1.remove(2)
print('s1=',s1,len(s1))
s1.remove(5)
#print('s1=',s1,len(s1))



