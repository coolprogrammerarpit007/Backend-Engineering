# # class Employee:
# #     def __init__(self,name,age,salary,employee_code):
# #         self.name = name
# #         self.age = age
# #         self.salary = salary
# #         self.employee_code = employee_code
        
        
# #     def show_details(self):
# #         print(f"************* Employee Details of Employee {self.employee_code} *************")
# #         print("********************************************")
# #         print(f"Employee Name: {self.name}")
# #         print(f"Employee Age: {self.age}")
# #         print(f"Employee Salary: {self.salary}")
# #         print(f"Employee Code: {self.employee_code}")
# #         print("********************************************\n")
        
        
# # emp1 = Employee("John",30,50000,"E001")
# # emp2 = Employee("Jane",28,60000,"E002")
# # emp3 = Employee("Doe",35,70000,"E003")
# # emp4 = Employee("Smith",40,80000,"E004")

# # # emp1.show_details()
# # # emp2.show_details() 
# # # emp3.show_details()
# # # emp4.show_details()


# import random

# class Employee:
    
#     company_name = "Zoho Corporation"
#     def __init__(self,name,designation,age) -> None:
#         self.name = name
#         self.designation = designation
#         self.age = age
#         self.employee_id = self.generate_employee_id()
        
#     def generate_employee_id(self):
#         return f"Emp-{random.randint(100,999)}"
    
    
#     def get_employee_details(self):
#         return f"Employee Id: {self.employee_id}\nEmployee Name: {self.name}\nEmployee Designation: {self.designation}\nEmployee Age: {self.age}"
    
    
#     @classmethod
#     def get_company_name(cls):
#         new_company_name = random.choice(["Google","Microsoft","Apple","Amazon","Facebook"])
#         cls.company_name = new_company_name
    
    
# employee1 = Employee("John Doe","Software Engineer",30)
# # print(employee1.get_employee_details())
# # print(f"Company Name: {employee1.company_name}")

# # Employee.get_company_name()
# # print(f"Updated Company Name: {employee1.company_name}")


# # class Vehicle:
# #     def __init__(self):
# #         self.vehicle_name = "Tata Naxon"
        
        
# #     def car_ride(self):
# #         print("I am riding a car")
    
# # class Car(Vehicle):
    
    
# #     def get_car_name(self):
# #         print("GET CAR NAME")
        
        
# # car = Car()
# # # print(car.vehicle_name)
# # car.car_ride()
# # car.get_car_name()


# # Inheritance In Python


# # class Vehicle:
# #     def __init__(self,type_of_vehicle,brand,model,year):
# #         self.type_of_vehicle = type_of_vehicle
        
# #         self.brand = brand
# #         self.model = model
# #         self.year = year
        
# # class Car(Vehicle):
# #     def __init__(self,type_of_vehicle,brand,model,year,name,color,price):
# #         super().__init__(type_of_vehicle,brand,model,year)
# #         self.name = name
# #         self.color = color
# #         self.price = price
# #         self.is_electric = True if self.name in ["Tesla","Nissan Leaf","Chevrolet Bolt","BYD"] else False
        
        
# #     def get_car_details(self):
# #         return f"Car Name: {self.name}\nCar Color: {self.color}\nCar Price: {self.price}\nIs Electric: {self.is_electric}"
    
    
# # car1 = Car("Car","Tesla","Model S",2022,"Tesla","Red",80000)
# # # print(car1.get_car_details())
    
    
