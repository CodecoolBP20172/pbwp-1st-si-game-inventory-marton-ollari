from gameInventory import *

print('MENU:')
print('''1 - Display inventory \n2 - Add or remove items to inventory
3 - Display organized inventory \n4 - Import file to inventory
5 - Export inventory to file \n6 - Quit''')
while True:
    first_input = input('Choose a number (1-6): ')
    # Display
    if first_input == '1':
        display_inventory(inv)
    # Add or remove items and lists
    elif first_input == '2':
        loot_list = []
        delete_list = []
        while True:
            print('Q - Quit, P - print list names, start with "-" to remove item')
            list_or_item = input('Add list name or an item:')
            if list_or_item in ['P', 'p']:
                for value, key in lists.items():
                    print(value, key)
            elif list_or_item in lists:
                loot_list.extend(lists[list_or_item])
            elif list_or_item[0] == '-':
                list_or_item = list_or_item[1:]
                if list_or_item in lists:
                    delete_list.extend(lists[list_or_item])
                else:
                    delete_list.append(list_or_item)
            elif list_or_item in ['Q', 'q']:
                break
            else:
                loot_list.append(list_or_item)
            print('New items: ', loot_list)
            print('Lost items: ', delete_list)
        inv = add_to_inventory(inv, loot_list)
        inv = remove_from_inventory(inv, delete_list)
    # Inventory in order
    elif first_input == '3':
        print('1 - Ascensing \n2 - Descending \n3 - Random order')
        while True:
            order_input = input('Choose the order of the items (1/2/3)')
            if order_input == '1':
                order = 'count,asc'
            elif order_input == '2':
                order = 'count,desc'
            elif order_input == '3':
                order = None
            else:
                continue
            break
        print_table(inv, order)
    # Import CSV file
    elif first_input == '4':
        try:
            import_name = input('Add the name of the csv file: ')
            filename = import_name + '.csv'
            import_inventory(inv, filename)
        except FileNotFoundError:
            print('File not found')
    # Export CSV file
    elif first_input == '5':
        export_name = input('Add a name to the csv file: ')
        filename = export_name + '.csv'
        export_inventory(inv, filename)
    # Quit
    elif first_input == '6':
        break
    print('1-Display, 2-Add/Remove, 3-In order, 4-Import, 5-Export, 6-Quit')
