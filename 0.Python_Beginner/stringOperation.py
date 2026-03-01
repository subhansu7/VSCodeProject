#String
print ("###String Operations###")
s = "Hello World"
print ("Original String =>" +  s)
print (type(s))
print ("Length of string"+ " " +str(len(s)))
print (s[0], s[10])
#Start, stop, step
#start → included, stop → excluded, Default step = +1
#Python always slices left → right when step is positive
print (s[0:5])
print (s[1:6:2])

#backward slicing
print (s[-1])
print (s[-5:-1])
print (s[-1:-5:-2])
print (s[-5:-1:-2])

#slicing and till end of string"
print("###slicing and till end of string###")
print (s[6:])
print (s[-3:])

#slicing from beginning of string
print("###slicing from beginning of string###")
print (s[:5])
print (s[:-6])

#String Unpacking
print ("###String Unpacking###")
a,b,c,d,e,f,g,h,i,j,k = s
print (a)
print (b)

