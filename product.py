

def common_products(warehouse1, warehouse2):
    return warehouse1.intersection(warehouse2)

warehouse1_inventory = {"apple", "banana", "cherry"}
warehouse2_inventory = {"banana", "cherry", "dragonfruit"}

common = common_products(warehouse1_inventory, warehouse2_inventory)
print("Common products in both inventories:", common)
