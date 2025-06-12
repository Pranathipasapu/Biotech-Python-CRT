Prog_Lang=['Java','Python','C','C++','SQL']
print(Prog_Lang)
print(type(Prog_Lang))
print("Accessing list elements using +ve elements")
print(Prog_Lang[0])
print(Prog_Lang[1])
print(Prog_Lang[2])
print(Prog_Lang[3])
print(Prog_Lang[4])
print("Accessing list elements using -ve elements")
print(Prog_Lang[-5])
print(Prog_Lang[-4])
print(Prog_Lang[-3])
print(Prog_Lang[-2])
print(Prog_Lang[-1])

List=['Black','Green','Red','Yellow','White']
print(List)
List[1]='Purple'
List[4]='Grey'
print('After modfication')
print(List)

IPL_List=['CSK','MI','RCB','SRH','PBKS','GT']
print("Accessing list elements without index")
for i in IPL_List:
    print(i)
print("Accessing list elements with index")
for i in range(len(IPL_List)):
    print(IPL_List[i])
#WHILE-LOOP
print("Accessing list elements with index using while loop")
i=0
while(i<len(IPL_List)):
    print(IPL_List[i])
    i+=1
#DELETION
IPL_List=['CSK','MI','RCB','SRH','PBKS','GT']
print(IPL_List)
print("After Deletion:")
del IPL_List[1]
print(IPL_List)
del IPL_List
#APPEND
front_end=['HTML','CSS','Javascript','Reactjs']
print(front_end)
front_end.append('Angular js')
front_end.append('Express js')
print(front_end)
#INSERT
front_end.insert(2,'Tailwind')
front_end.insert(3,'BootStrap')
print(front_end)
#POP
front_end.pop()
print(front_end)
front_end.pop(2)
print(front_end)
#REMOVE
front_end.remove('HTML')
print(front_end)
#INDEX
front_end=['HTML','CSS','Javascript','Reactjs']
print(front_end.index('HTML'))
print(front_end.index('CSS'))
#REVERSE
n=[1,2,3,4,5,6,7,8,9,10]
print(n)
n.reverse()
print(n)
#EXTEND
num1=[1,2,3,4,5,6,7,8,9,10]
print(num1)
num2=[15,14,13,12,11]
print(num2)
num1.extend(num2)
print(num1)
#SORT
num1.sort()
print(num1)
#EXAMPLE-PARTY CODE
Guest_list=[]
print("Welcome to party project")
while(True):
    print("1.Enter 1 to add a guest")
    print("2.Enter 2 to remove a guest who cancels")
    print("3.Enter 3 to check a friend is on the list or not")
    print("4.Enter 4 to sort and print the final guest list")
    print("5.Enter 5 to exit")
    choice=int(input("Enter your choice-"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            Name=input("Enter the guest name:")
            Guest_list.append(Name)
            print(f"{Name} is added to the guest list")
        elif(choice==2):
            cancelled_name=input("Enter the name of the guest who cancelled")
            if cancelled_name in Guest_list:
                Guest_list.remove(cancelled_name)
                print(f"{cancelled_name} is Removed from Guest List")
            else:
                print(f"{cancelled_name} is not present in Guest List")
        elif(choice==3):
            check_guest=input("Enter the guest name")
            if check_guest in Guest_list:
                print(f"{check_guest} is attending the party")
            else:
                print(f"{check_guest} is not attending the party")
        elif(choice==4):
            Guest_list.sort()
            print("Here's the final list of guests")
            print(Guest_list)
    else:
        print("Enjoy the party")
    break

                
    
            
        
        

    
