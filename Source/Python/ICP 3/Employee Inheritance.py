class Employee():
    empCount = 0
    SumSalary =0
    Avg =0

    def __init__(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = did
        Employee.empCount += 1
        Employee.SumSalary += self.salary

    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did)
# Create a Fulltime Employeeclass and it should inherit the properties of Employee classe
class FullTimeEmp(Employee):
    def __init__(self, eid, name, salary, did, exp):
        Employee.__init__(self, eid, name, salary, did)
        self.exp = exp
    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did, ",Experience:", self.exp)



emp1 = Employee(1, "Prudhvi", 2000000, 2)
emp2 = Employee(2, "Danerys", 60000, 3)
emp3=FullTimeEmp(3, "Tyrion", 4000, 5, 6)

# Total employee and average salary
print("Total Employees %d" % Employee.empCount)
print("Average salary of the employees is", (Employee.SumSalary/Employee.empCount))
print(emp1.displayEmployee())
print(emp2.displayEmployee())
print(emp3.displayEmployee())