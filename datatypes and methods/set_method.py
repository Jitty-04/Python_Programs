#add()
s={1,3,5,9}
s.add(7)
print(s)
#result {1, 3, 5, 7, 9}
s.add(9)
print(s)
#result {1, 3, 5, 7, 9} no effect

#pop()
s1={1,2,3,4}
s1.pop()
print(s1)
#result first pop {2, 3, 4}
s1.pop()
print(s1)#{3, 4}
print(s1.pop())
print(s1)#{4}

#remove()
s.remove(3)
print(s) #{1, 5, 7, 9}

#union() |
s2={1,2,3,4}
s3={4,5,6,7}
print(s2.union(s3)) #{1, 2, 3, 4, 5, 6, 7}

#intersection() &
print(s2.intersection(s3))#{4}

#symmetric() ^
print(s2.symmetric_difference(s3))
#{1, 2, 3, 5, 6, 7}

#clear()
s4={4,6,7}
s4.clear()
print(s4) #set()
for i in s3:
    print(i,end=' ')
#4 5 6 7