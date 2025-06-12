#LIST OF CONCATENATION
a=[10,20,30]
b=[1,2,3]
result=a+b
print(result)
#REPETITION OF LIST
b=[1,2,3]
result=b*3
print(result)
#DATATYPE
Tuple=(10,20,30)
print(Tuple)
print(type(Tuple))
Tuple1=(20)
print(Tuple1)
print(type(Tuple1))
Tuple2=(20+5j)
print(Tuple2)
print(type(Tuple2))
#TUPLE PACKING
num=10,20,30,40,50,60,70,80,90,100
print(num)
print(type(num))
#TUPLE UNPACKING
a,b,c,d,e,f,g,h,i,j=num
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))
print(i,type(i))
print(j,type(j))
#QUESTION
prog_lang='HTML','css','javscript','c','dsa','python','angularjs','expressjs','cython','reactjs','java','rubypython','zython','talewind','sql'
print(prog_lang)
print(type(prog_lang))
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o=prog_lang
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))
print(i,type(i))
print(j,type(j))
print(k,type(k))
print(l,type(l))
print(m,type(m))
print(n,type(n))
print(o,type(o))
#ACCESSING TUPLE USING INDEXING
print("Accessing list elements using +ve elements")
print(prog_lang[0])
print(prog_lang[1])
print(prog_lang[2])
print(prog_lang[3])
print(prog_lang[4])
print("Accessing list elements using -ve elements")
print(prog_lang[-5])
print(prog_lang[-4])
print(prog_lang[-3])
print(prog_lang[-2])
print(prog_lang[-1])

Tuple=(5,10,15,20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160)
print(Tuple)
#Print the first 5 elements of tuple with slicing
print(Tuple[:5:])
#Print the first 10 elements of tuple with slicing
print(Tuple[:10:])
#Print the last 5 elements of tuple with slicing
print(Tuple[-5:])
#Print the last 20 elements of tuple with slicing
#Print the last 3 elements of tuple with slicing
#Print the elements of tuple from last 5th to 10th with slicing
#Print the elements of tuple from 10th to 15th with slicing
#Print the elements of tuple with slicing by skipping every 2 elements
#Print the elements of tuple with slicing by skipping every 3 elements
#Print the elements of tuple with slicing by skipping every -3 elements
