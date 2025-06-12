set={'python','c','c++','javascript','HTML','AngulaR js'}
print(set)
print(type(set))
print('python' in set)
#ADD
set.add('jython')
print(set)
set.add('nodejs')
print(set)
#UPDATE
set.update(['pypy','iron python'])
print(set)
#REMOVE
set.remove('c')
print(set)
#POP METHOD
set.pop()
print(set)
#DISCARD METHOD
set.discard('c++')
print(set)
#CLEAR
#set.clear()
#print(set)
#UNION
set1={'cython','css','javascript'}
print(set | set1)
#INTERSECTION
print(set & set1)
#DIFFERENCE
diff=set.difference(set1)
print(diff)
#ISSUBSET METHOD
issub=set.issubset(set1)
print(issub)
#ISSUPERSET METHOD
issuper=set.issuperset(set1)
print(issuper)


