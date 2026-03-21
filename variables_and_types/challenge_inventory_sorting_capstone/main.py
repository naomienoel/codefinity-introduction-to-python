# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

category1 = categories[0:11]
category2 = categories[13:]

candy1_price = "$1.50"
candy2_price = "$2.00"
candy3_price = "$5.40"

print(f"We have {candy1} for {candy1_price} in the {category1}")
print(f"We have {candy2} for {candy2_price} in the {category1}")
print(f"We have {dry_goods} for {candy3_price} in the {category2}")
