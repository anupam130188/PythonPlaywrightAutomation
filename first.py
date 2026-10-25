# var="Hello"
# # while i<10:
# #     print(var)
# #     i=i+1;

# # for x in var:
# #     print(x);

# for x in range(10):
#     print(x);
#     x=x+1;


# def helloProg():
#     print("Hello")
    
# def helloProg(message):
#     print("Hello")
#     print(message)
    
# helloProg("Human")

# def sum(*values):
#     total=0
#     for i in values:
#         total+=i;
#     print(total)

# sum(1,2,3,4,6,6)


# dict_list={
#     "name": "Anupam",
#     "age" : 13,
#     "DOB": 1988,
#     "City": "Gurdaspur",
#     "NRI" : False
# }

# def func(**kwargs):
#     for key, value in dict_list.items():
#         print(f"{key} -> {value}")
# #print(dict_list)

# func(**dict_list)


class Human:
    species="Vegetarian"
    tricks=[]
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    
    def shout(self):
        print(f"one who shouted is {self.name} ")
        

class Male(Human):
    def purr(self):
       return f"name of person is {self.name}"

p1=Male("Anupam",36)
print(p1.purr(), p1.name, p1.age, Male.species)
# p1=Human("Anupam",36);
# p1.tricks.append('Laugh')
# print(p1.name, p1.age)
# p1.shout()
# print(p1.tricks)

# p2=Human("Ank",30);
# p2.tricks.append('Smile')
# print(p2.name, p1.age)
# p2.shout()
# print(p2.tricks)
