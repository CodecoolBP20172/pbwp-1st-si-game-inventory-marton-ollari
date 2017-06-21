import csv
# Displays the inventory.
def display_inventory(inventory):
    print('Inventory:')
    for key, value in inventory.items():
        print(value, key)
    print('Total number of items: ', sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        if added_items[i] in inventory.keys():
            inventory[added_items[i]] += 1
        else:
            inventory[added_items[i]] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print('Inventory:')
    x = 0
    max_len = 0
    for key in inventory:
        x = len(key)
        if max_len < x:
            max_len = int(x)
    count_list = list(inventory.items())
    print(count_list)
    t = 0
    if order == 'count,asc':
        for l in range(len(count_list)):
            for i in range(len(count_list)-1):
                if count_list[i][1] > count_list[i+1][1]:
                    t = count_list[i]
                    count_list[i] = count_list[i+1]
                    count_list[i+1] = t
                    print(count_list)
    elif order == 'count,desc':
        for l in range(len(count_list)):
            for i in range(len(count_list)-1):
                if count_list[i][1] < count_list[i+1][1]:
                    t = count_list[i]
                    count_list[i] = count_list[i+1]
                    count_list[i+1] = t

    print('count'.rjust(5), 'item name'.rjust(max_len+3))
    print('-------------------')
    for i in range(len(count_list)):
        print(str(count_list[i][1]).rjust(5), str(count_list[i][0]).rjust(max_len+3))
    print('-------------------')
    print('Total number of items: ', sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    open(filename, 'rb')
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#display_inventory(inv)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
#display_inventory(inv)
#print_table(inv, order='count,asc')
#print_table(inv, order='count,desc')
#print_table(inv)
import_inventory(inv, filename="test_inventory.csv")