#Darrian Woodard
#1593984

# Type code for classes here
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def get_total_price(self):
       return self.item_quantity*self.item_price 

    def print_item_cost(self):
        return '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, self.item_quantity*self.item_price)

if __name__ == "__main__":
    # Type main section of code here
    item = ItemToPurchase()
    item1 = ItemToPurchase()

    print('Item 1')
    item_name = input("Enter the item name:\n")
    item_price = int(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    item.item_name = item_name
    item.item_price = item_price
    item.item_quantity = item_quantity

    print('\nItem 2')
    item_name = input("Enter the item name:\n")
    item_price = int(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    item1.item_name = item_name
    item1.item_price = item_price
    item1.item_quantity = item_quantity

    print('\nTOTAL COST')
    print(item.print_item_cost())
    print(item1.print_item_cost())
    print('\nTotal: ${}'.format(item.get_total_price()+item1.get_total_price()))