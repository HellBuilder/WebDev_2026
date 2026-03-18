class MenuItem:
    def __init__(self, name, price, category, is_available):
        self.name = str(name)
        self.price = float(price)
        self.category = str(category)
        self.is_available = bool(is_available)
        self.describtion = ""
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category
    
    def set_describtion(self, describtion):
        self.describtion = describtion
        
    def get_describtion(self):
        return self.describtion
    
    def toggle_availability(self):
        if self.is_available:
            self.is_available = False
        else:
            self.is_available = True
    
    def __str__(self):
        return f"MenuItem:(Name: {self.name}, Price: {self.price}, Category: {self.category}, Availability: {self.is_available})"


class Food(MenuItem):
    def __init__(self, name, price, category, is_available, is_spicy, cooking_time_mins):
        super().__init__(name, price, category, is_available)
        self.is_spicy = bool(is_spicy)
        self.cooking_time_mins = int(cooking_time_mins)
        
        
    def get_describtion(self):
        if self.is_spicy:
            return super().get_describtion() + f" Beware, as this food is indeed spicy! And cooks for {self.cooking_time_mins} minutes"
        else:
            return super().get_describtion() + f" This food will cook for {self.cooking_time_mins} minutes"
    
    
class Drink(MenuItem):
    def __init__(self, name, price, category, is_available, size, is_cold):
        super().__init__(name, price, category, is_available)
        self.size = str(size)
        self.is_cold = bool(is_cold)
        
    def get_price(self):
        ind = 0
        if self.size == "S": ind = 0.8
        if self.size == "M": ind = 1.0
        if self.size == "L": ind = 1.3
        return self.price * ind
    
    def get_size(self):
        return self.size
    
    def get_describtion(self):
        if self.is_cold:
            return super().get_describtion() + f"Beware, as this is a cold drink! And it's size is {self.size}!"
        else:
            return super().get_describtion() + f"This is drink is warm, and it's size is {self.size}!"
        
class Dessert(MenuItem):
    def __init__(self, name, price, category, is_available, calories, contains_nuts):
        super().__init__(name, price, category, is_available)
        self.calories = int(calories)
        self.contains_nuts = bool(contains_nuts)
        
    def get_describtion(self):
        if self.contains_nuts:
            return super().get_describtion() + f" Beware, as this dessert contains nuts and has {self.calories} calories!"
        else:
            return super().get_describtion() + f" This dessert contains {self.calories} calories!"
        
    
class Order:
    def __init__(self, order_id, items):
        self.order_id = int(order_id)
        self.items = list(items)
    
    def addItem(self, new_item):
        self.items.append(new_item)
        return True
        
    def removeItem(self, old_item):
        if self.items.remove(old_item):
            return True
        else:
            return False
    
    def getTotal(self):
        total = 0
        for i in range(len(self.items)):
            total += self.items[i].get_price()
        return total
    
    def getItemCount(self):
        return len(self.items)
    
    def getItem(self, id):
        return self.items[id]
    
    def __str__(self):
        return f"Order(OrderID: {self.order_id}, Items: {self.items}, Total: {self.getTotal})"
            
            
        
    