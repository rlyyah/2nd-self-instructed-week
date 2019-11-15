def display_inventory(inventory):
    for item in inventory:
        print(f'{item}: {inventory[item]}')


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    display_inventory(inventory)

def print_table(inventory, order=""):
    
    item_name = 'item name'
    count = 'count'
    length = len(item_name)
    lengthbis = len(count)
    for item in inventory.items():
        if length < len(item[0]):
            length = len(item[0])
        if lengthbis < len(str(item[1])):
            lengthbis = len(str(item[1]))
    amount_of_spaces = length + lengthbis + 3
    spacer = '-'*amount_of_spaces
    print(spacer)
    print(f'{item_name.rjust(length," ")} | {count.rjust(lengthbis," ")}')
    print(spacer)
    if order == "count,desc":
        for i in sorted(inventory.items(), key=lambda item:(item[1], item[0]),reverse=True):
            print(f"{i[0].rjust(length,' ')} | {str(i[1]).rjust(lengthbis,' ')}")
    elif order == "count,asc":
        for i in sorted(inventory.items(), key=lambda item:(item[1], item[0])):
            print(f"{i[0].rjust(length,' ')} | {str(i[1]).rjust(lengthbis,' ')}")
    else:
        for i in inventory.items():
            print(f"{i[0].rjust(length,' ')} | {str(i[1]).rjust(lengthbis,' ')}")
    print(spacer)    


def import_inventory(inventory, filename):
    try:
        read_items = open(filename,'r')
        items = read_items.read()
        read_items.close()
        items = items.replace('\n','')
        items_list = items.split(',')
        for item in items_list:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('no permission')


def export_inventory(inventory, filename):
    item_string = ''
    item_list = []
    for item in inventory:
        for i in range(inventory[item]):
            item_list.append(item)
    item_string = ','.join(item_list)
    try:
        write_items = open(filename,'w+')
        write_items.write(item_string)
        write_items.close()
        print('Saving success!')
    except FileNotFoundError:
        print("File 'no_such_file.csv' not found!")
    except PermissionError:
        print('no permision')



inv = {'rope': 1, 'torch': 6, 'gold coin': 10, 'dagger': 1, 'arrow': 12}

display_inventory(inv)
print('==')
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragon_loot)





print_table(inv,"count,desc")

print_table(inv,"count,asc")
print_table(inv)
kek = {}
print('=-==================')
import_inventory(inv,'/home/ubuntuwanderer/local-repo/code/2nd-self-instruced-week/code/project/import_inventory.csv')
print('AFTER IMPORTING')
print_table(inv, "count,desc")
export_inventory(inv,'/home/ubuntuwanderer/local-repo/code/2nd-self-instruced-week/code/project/export_inventory.csv')
