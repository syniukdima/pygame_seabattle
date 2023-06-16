"""
Create a class that describes a Product of online store. As a Product fields you can use a price, description
and product's dimensions.
Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
Create a class that describes an Order.
- the order must contain data about the customer who carried it out and products.
Implement a method for calculating the total order value. """

obj1count = 2
obj2count = 5
obj3count = 1



class Product:

    def __init__(self, price, desc, dimensions):
        if isinstance(price, (int, float)):
            self.price = price
        else:
            self.price = 0

        if isinstance(desc, str):
            self.desc = desc
        else:
            self.desc = ""


        if all(isinstance(dim, int) for dim in dimensions):
            self.dimensions = dimensions
        else:
            self.dimensions = [0, 0, 0]


obj = Product(30, "opys", [40, 34, 30])
obj1 = Product(40, "opys", [40, 34, 30])
obj2 = Product(50, "opys", [40, 34, 30])


class User():
    def __init__(self, name, second_name, mobile_phone):
        if isinstance(name, str):
            self.name = name
        else:
            self.name = " "
        if isinstance(second_name, str):
            self.second_name = second_name
        else:
            self.second_name = " "
        if isinstance(mobile_phone, str):
            self.mobile_phone = mobile_phone
        else:
            self.mobile_phone = " "

user = User("Johnny", "Marshal", "+7864576857")

class Order:
    def obj_count(self, obj, obj1, obj2, obj1count, obj2count, obj3count):
        return sum((obj.price * obj1count, obj1.price * obj2count, obj2.price * obj3count))

    def __init__(self, user, products):
        if isinstance(user, User):
            self.user = user
        else:
            self.user = None

        if all(isinstance(product, Product) for product in products):
            self.products = products
        else:
            self.product = None





order1 = Order(user, [obj, obj1, obj2])
print(order1.obj_count(obj, obj1, obj2, obj1count, obj2count, obj3count))


order1.obj_count(obj, obj1, obj2, obj1count, obj2count, obj3count)


