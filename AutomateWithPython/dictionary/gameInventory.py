'''
Created on Oct 12, 2019

@author: Umang Bhatia
'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    total_items = 0
    
    for item,count in inventory.items():
        print(str(count) + ' ' + item)
        total_items += count
        
    print('Total number of items: ' + str(total_items))

def addToInventory(inventory, addedItems):
    for each_item in addedItems:
        inventory[each_item] = addedItems.count(each_item)
    
addToInventory(stuff, dragon_loot)
displayInventory(stuff)