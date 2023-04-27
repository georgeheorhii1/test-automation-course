# Describe 1 be-any class, for mind you will use only one instance of this class.
# describe part of the functionality of the restaurant.

# OrderPart class has a method that rotates a single dish.
# You can have different dishes, for example, Risotto, Pasta, Pizza,
# These are inherited from the same parent abstract class Dish(Factory).


class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)


class Pizza(Dish):
    def __init__(self):
        super().__init__('Pizza')


class Pasta(Dish):
    def __init__(self):
        super().__init__('Pasta')


class Risotto(Dish):
    def __init__(self):
        super().__init__('Risotto')


class OrderPart:
    def __init__(self, dish):
        self.dish = dish

    def rotate(self, ):
        print(f"Rotating the {self.dish.name} ")


class Restaurant:
    def __init__(self):
        self.available_dishes = [Pizza(), Pasta(), Risotto()]
        self.order = []

    def menu(self):
        print("Available dishes:")
        for dish in self.available_dishes:
            print(f"- {dish.name}")

    def place_order(self, dish_name):
        for dish in self.available_dishes:
            if dish.name == dish_name:
                self.order.append(OrderPart(dish))
                print(f"Placed order for {dish_name}")
                break
        else:
            print(f"Sorry, {dish_name} is not available.")

    def cancel_order(self, dish_name):
        for order_part in self.order:
            if order_part.dish.name == dish_name:
                self.order.remove(order_part)
                print(f"Cancelled order for {dish_name}")
                break
        else:
            print(f"No order found for {dish_name}")

    def prepare_order(self):
        for order_part in self.order:
            dish = order_part.dish
            dish.add_ingredient("Salt")
            dish.add_ingredient("Pepper")
            dish.add_ingredient("Olive oil")

    def serve_order(self):
        for order_part in self.order:
            dish = order_part.dish
            print(f"Serving {dish.name}...")
            order_part.rotate(45)
            order_part.heat(180)
