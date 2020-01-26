My_sal=25000
pf=2000
Rent_allownce=5000
Travel_allownce=3000
e_name=input("Enter the name of Employee \n")
print(e_name)
c_name=input("Enter the company name \n")
print(c_name)
salary=float(input("Enter the salary of Employee \n"))
if(salary>50000):
    tax=0.15*salary
    print(My_sal)
    c=My_sal-pf
    netsalary=salary-tax
    f_sal=c+Rent_allownce+Travel_allownce
    print("The net salary of ",e_name," worked in " ,c_name, " is",netsalary)
    print(f_sal)
else:
    netsalary=salary
    print("No taxalbe Amount")
    print("The net salary of ",e_name," worked in " ,c_name+ " is",salary)

##############################################################################################################
Input = [("LAX", "JFK"), ("JFK", "LHR"), ("SFO", "LAX"), ("LHR", "CDG")]
# Output =[ ("SFO", "LAX"), ("LAX", "JFK"), ("JFK", "LHR"), ("LHR", "CDG") ]
output = []
print(Input[0][-1])
for i in range(len(Input)):
    a = Input[i][-1]#(Input[i])
    for j in range(len(Input)):
        if Input[i][0] == Input[j][-1]:
            output.append(Input[i])
for i in Input:
    if i not in output:
        output.insert(0, i)

print(output)

