s1={1,2,3,4,5,6}
print('s1=',s1,len(s1))
s2={4,6,7,8,9}
print('s2=',s2,len(s2))
s3=s1.union(s2)
print('s3=',s3,len(s3))
s4=s1.intersection(s2)
print('s4=',s4,len(s4))
s5=s1.difference(s2)
print('s5=',s5,len(s5))
s6=s2.difference(s1)
print('s6=',s6,len(s6))
s7=s1.symmetric_difference(s2)
print('s7=',s7,len(s7))
s8=set()
print('s8=',s8,len(s8))
s8.add(10)
print('s8=',s8,len(s8))
s8.add(35)
s8.add(50)
s8.add(55)
s8.add(100)
print('s8=',s8,len(s8))
s8.discard(35)
print('s8=',s8,len(s8))
s8.discard(60)
print('s8=',s8,len(s8))
s8.remove(50)
print('s8=',s8,len(s8))
#s8.remove(70)
print('s8=',s8,len(s8))
s9=s8.pop()
print('s9=',s9)




