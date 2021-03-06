import csv
import sys


def display_inventory(inventory):
    print('Inventory:')
    for key, value in inventory.items():
        print(value, key)
    print('Total number of items: ', sum(inventory.values()))
# Displays the inventory.


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        if added_items[i] in inventory.keys():
            # Add 1 to item in inventory
            inventory[str(added_items[i])] += 1
        else:
            # Create new item in inventory
            inventory[str(added_items[i])] = 1
    return inventory
# Adds to the inventory dictionary a list of items from added_items.


def print_table(inventory, order=None):
    print('Inventory:')
    x = 0
    max_len = 0
    # Find the longest item name
    for key in inventory:
        x = len(str(key))
        if max_len < x:
            max_len = int(x)
    count_list = list(inventory.items())
    t = 0
    # Ascending order
    if order == 'count,asc':
        for l in range(len(count_list)):
            for i in range(len(count_list) - 1):
                if count_list[i][1] > count_list[i + 1][1]:
                    t = count_list[i]
                    count_list[i] = count_list[i + 1]
                    count_list[i + 1] = t
    # Descending order
    elif order == 'count,desc':
        for l in range(len(count_list)):
            for i in range(len(count_list) - 1):
                if count_list[i][1] < count_list[i + 1][1]:
                    t = count_list[i]
                    count_list[i] = count_list[i + 1]
                    count_list[i + 1] = t
    # Print organized inventory
    print('count'.rjust(5), 'item name'.rjust(max_len + 3))
    print('-'.rjust(max_len + 8, '-'))
    for i in range(len(count_list)):
        print(str(count_list[i][1]).rjust(5),
              str(count_list[i][0]).rjust(max_len + 3))
    print('-'.rjust(max_len + 8, '-'))
    print('Total number of items: ', sum(inventory.values()))
# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def import_inventory(inventory, filename="import_inventory.csv"):
    import_list = []
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in range(len(row)):
                import_list.append(str(row[i]))
        add_to_inventory(inventory, import_list)
    csvfile.closed
# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    count_list = list(inventory.items())
    inventory_list = []
    for i in range(len(count_list)):
        for t in range(count_list[i][1]):
            inventory_list.append(str(count_list[i][0]))
    s = ",".join(inventory_list)
    with open(filename, 'w') as writecsv:
        writecsv.write(s)
    writecsv.close
# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def remove_from_inventory(inventory, deleted_items):
    for i in range(len(deleted_items)):
        if deleted_items[i] in inventory.keys():
            inventory[str(deleted_items[i])] -= 1
            if inventory[deleted_items[i]] <= 0:
                del inventory[deleted_items[i]]
        else:
            print(deleted_items[i], 'is not in the inventory')
    return inventory
# Remove items from inventory


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
lists = { 
    'dragon_loot': ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'], 
    'treasure_chest': ['gold coin', 'dagger', 'gold coin'], 
    'gnome_gift': ['mushroom', 'poison', 'diamond'],
}