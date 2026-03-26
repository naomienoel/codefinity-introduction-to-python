# The item's discount and stock status have been defined

item_quantity = 100
lowStock = item_quantity <= 999

discounted = item_quantity <= 999


movingProduct = discounted or lowStock
promotion = not discounted and lowStock

print("Is the item eligible for promotion?" ,promotion)
