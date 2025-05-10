# Different ways to create tuples
Alpha=[5,10,15,"twenty"]
Bravo=100,["one", "two", "three"], 200
Charlie=tuple([1,2,3,(4,5,6,7,8,9)])
Delta=tuple("ABCDEF")
Echo=tuple(2**k for k in range(11))
# Reading elements values and getting a cut
print("Alpha:", Alpha)
print("A number of elements", len(Alpha))
print("The first:", Alpha[0])
print("The last:", Alpha[-1])
print("Bravo:", Bravo)
print("Bravo[1]:", Bravo[1])
print("Bravo[1][2]:", Bravo[1][2])
print("Charlie:", Charlie)
print("A number of elements:", len(Charlie))
print("Charlie[3]:", Charlie)
print("Charlie[3][1:4]:", Charlie[3][1:4])
print("Delta:", Delta)
print("A number of elements:", len(Delta))
print("Delta[-3]:", Delta[-3:])
print("Echo:", Echo)
Foxtrot=tuple(Echo[k] for k in range(len(Echo)) if k%2==0)
print("Foxtrot:", Foxtrot)
Golf=Echo[2:5]
print("Golf:", Golf)

