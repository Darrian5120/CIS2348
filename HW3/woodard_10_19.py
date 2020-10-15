#Darrian Woodard
#1593984

# Type code for classes here
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_description = 'none', item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        cost  = self.item_quantity*self.item_price 
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, cost)
        return string, cost

    def print_item_description(self):
        return '{}: {}'.format(self.item_name, self.item_description)


class ShoppingCart:
    #cart_items = []

    def __init__(self, customer_name = '', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, string):
        flag = False
        for items in self.cart_items:
            if items.item_name == string:
                self.cart_items.remove(items)
                flag = True
                break
        if flag == False:
            print("Item not found in cart. Nothing removed.")


    def modify_item(self, ItemToPurchase):
        flag = False
        print('CHANGE ITEM QUANTITY')
        string = str(input("Enter the item name:\n"))
        qty = int(input("Enter the new quantity:\n"))
        for ItemToPurchase in self.cart_items:
            if (ItemToPurchase.item_name == string):
                ItemToPurchase.item_quantity = qty
                flag = True
                break
        if flag == False:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        numItems = 0
        for items in self.cart_items:
            numItems = numItems + items.item_quantity
        return numItems

    def get_cost_of_cart(self):
        total_cost = 0
        for items in self.cart_items:
            total_cost += (items.item_quantity * items.item_price)
        return total_cost


    def print_total(self):
        total = self.get_cost_of_cart()
        if total == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            self.output_cart()

    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS\n{}\'s Shopping Cart - {}\n\nItem Descriptions'.format(self.customer_name, self.current_date))
        for items in self.cart_items:
            print('{}: {}'.format(items.item_name, items.item_description), end='\n')

    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))    
        print('Number of Items:', self.get_num_items_in_cart(), end='\n\n')
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        tc = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,item.item_price, (item.item_quantity * item.item_price)), end='\n')
            tc += (item.item_quantity * item.item_price)
        print('\nTotal: ${}'.format(tc), end='\n')


def print_menu(ShoppingCart):

    menu = ('\nMENU\n'
    'a - Add item to cart\n'
    'r - Remove item from cart\n'
    'c - Change item quantity\n'
    'i - Output items\' descriptions\n'
    'o - Output shopping cart\n'
    'q - Quit\n')

    command = ''

    while(command != 'q'):
        print(menu, end='\n')
        command = input('Choose an option:\n')

        while(command != 'a' and command != 'o' and command != 'i' and command != 'r' and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')

        if command == 'a':
            print('ADD ITEM TO CART')
            item_name = str(input('Enter the item name:\n'))
            item_description = str(input('Enter the item description:\n'))
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            items = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            ShoppingCart.add_item(items)

        if command == 'o':
            ShoppingCart.output_cart()

        if command == 'i':
            ShoppingCart.print_descriptions()

        if command == 'r':
            print('REMOVE ITEM FROM CART')
            string = str(input('Enter name of item to remove:\n'))
            ShoppingCart.remove_item(string)
            
        if command == 'c':
            ShoppingCart.modify_item(ItemToPurchase)


if __name__ == "__main__":
    # Type main section of code here
    customer_name = str(input("Enter customer's name:\n"))
    current_date = str(input("Enter today's date:\n"))

    print("\nCustomer name: {}\nToday's date: {}".format(customer_name, current_date))

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

