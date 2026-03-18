
from models import MenuItem, Food, Drink, Dessert, Order
def main():
    print()
    Menu = []

    Menu.append(Food("Beshbarmak", 3500, "Food", True, True, 70))
    Menu.append(Food("Plov", 2800, "Food", True, False, 50))
    Menu.append(Food("Lagman", 2200, "Food", True, True, 40))
    Menu.append(Drink("Cola", 800, "Drink", True, "M", True))
    Menu.append(Drink("Green Tea", 600, "Drink", True, "S", False))
    Menu.append(Drink("Latte", 1200, "Drink", True, "S", False))
    Menu.append(Dessert("ChakChak", 1500, "Dessert", True, 450, True))
    Menu.append(Dessert("Baursak", 800, "Dessert", True, 200, False))
    Menu.append(Dessert("Medovik", 1800, "Dessert", True, 500, True))

    Menu[0].set_describtion("Traditional Kazakh Dish")
    print("===== Restaurant Menu =====")
    for i in range(9):
        print(f"{Menu[i].get_name()} - {Menu[i].get_price()} KZT {Menu[i].get_category()}")
    
    print("===== Creating Orders =====")
    order1 = Order(1, [])
    order1.addItem(Menu[0])
    print(f"Order #001: Adding Beshbarmak - Successful")
    order1.addItem(Drink("Cola", 800, "Drink", True, "L", True))
    print(f"Order #001: Adding Cola (Large) - Success")
    order1.addItem(Menu[6])
    print(f"Order #001: Adding Chak-Chak - Success")
    
    Colas = []
    Colas.append(Drink("Cola", 800, "Drink", True, "S", True))
    Colas.append(Drink("Cola", 800, "Drink", True, "M", True))
    Colas.append(Drink("Cola", 800, "Drink", True, "L", True))
    print("===== Drink Price Variation =====")
    for i in range(3):
        print(f"{Colas[i].get_name()} ({Colas[i].get_size()}): {Colas[i].get_price()} KZT")
    
    print("===== Item Describtions =====")
    for i in range(3):
        item = order1.getItem(i)
        print(f"{item.get_name()}: {item.get_describtion()}")
    
    
    
    print("===== Order Summary =====")
    print("Order #001:")
    for i in range(3):
        item = order1.getItem(i)
        print(f"- {item.get_name()}: {item.get_price()} KZT")
    print(f"Total: {order1.getTotal()} KZT ({order1.getItemCount()} items)")
if __name__ == "__main__":
    main()
