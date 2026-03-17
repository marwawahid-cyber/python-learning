# my mini project of completing three lectures in python

store_name="python gadgets:"

item1_name="keyboard"
item1_price=1000

item2_name="mouse"
item2_price=500

item3_name="adapter"
item3_price=100

total= item1_price + item2_price + item3_price

header= "\t--- my mini shop receipt  ---\t"
divider= "\t -----------------------------\t"
body=(f"\t{item1_name} {item1_price}\n\t{item2_name}\t{item2_price}\n\t{item3_name}\t{item3_price}")


print(header)
print(divider)
print(store_name)
print(body)
print(divider)
print("total price:" ,total)
print("\n\t *** thank you ***")