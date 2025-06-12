JobRole={101:'Front-End Developer',102:'Back_End Developer',103:'SQL Administration'}
print(JobRole)
print(type(JobRole))
#Accessing using key values
print(JobRole[101])
print(JobRole[102])
print(JobRole[103])
JobRole[101]='UI/UX Developer'
print(JobRole)
#Add an element to dict
JobRole[104]='Data Engineer'
print(JobRole)
#POP
JobRole.pop(101)
print(JobRole)
#Deletion
del JobRole[103]
print(JobRole)
#Length
print(len(JobRole))
#KEYS
print(JobRole.keys())
#VALUES METHOD
print(JobRole.values())
#ITEMS METHOD
print(JobRole.items())
#COPY METHOD
print(JobRole.keys())
#UPDATE
JobRole.update({105:'HTML'})
print(JobRole)


