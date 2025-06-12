n=int(input("Enter the number of employees:"))
employees={}
for i in range(n):
    print(f"Enter details for employee {i+1}:")
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    desg = input("Designation: ")
    sal = float(input("Salary: "))
    deptnum = input("Department number: ")
    deptname = input("Department name: ")
    mgr = input("Reporting Manager: ")
emp_deatils={"name":name,"emp_id":emp_id,"desg":desg,"sal":sal,"deptnum":deptnum,"deptname":deptname,"mgr ":mgr }
print

