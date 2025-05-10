# The first list
#list1=[0,500,1000,1500]
list1=eval(input("Enter a list: "))
# The second list
list2=[500*k for k in range(4)]
if len(list1)==len(list2):
    print("The lists have the same length.")
    print("Checking list elements...")
    for k in range(len(list1)):
        if list1[k]==list2[k]:
            print("Elements under index №"+str(k)+" are the same: list1["+str(k)+"]=",end="")
            print(":list2["+str(k)+"]="+str(list1[k]))
        else:
            print("Elements under index №"+str(k)+" do not match.")
            print("The lists are different.")
            break
        if k==len(list1)-1:
            print("The lists are the same.")
else:
    print("Lists have a different length.")
print("Completion of the program. Bye-bye!")