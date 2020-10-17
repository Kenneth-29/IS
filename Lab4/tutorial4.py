class Employee: # Class name is Employee
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary): #class constructor
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


num_emp = int(input("The number of employees: "))
employees = []
for x in range(num_emp):
    new_name = input("Name: ")
    while new_name in employees:
        new_name = input("Please enter another name: ")
    employees.append(Employee(new_name, 0))
print("Total Employee %d" % Employee.empCount)
for x in range(len(employees)):
    print(employees[x])


#Kenneth