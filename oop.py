"""Task #03
Create a class that describes a Product of online store. As a Product fields you can use a price, description
and product's dimensions.
Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
Create a class that describes an Order.
- the order must contain data about the customer who carried it out and products.
Implement a method for calculating the total order value. """

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

print(obj.dimensions)