store1_sales = [101, 102, 103, 104, 105]
store2_sales = [103, 104, 106, 107, 108]


unique_sales = set(store1_sales).symmetric_difference(set(store2_sales))


print("Items sold in only one store:", unique_sales)