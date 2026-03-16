quote=input("enter the string:")
num=eval(input("enter the no:"))
me=eval(input("enter the f.no:"))  # eval evaluates a string as a Python expression and returns the result.


print("below datatypes as per your data")
num=str(num)                        # to convert int into str
me=str(me)                          # to convert float into str

print(type(quote))
print(type(num))
print(type(me))

print("your string value is this:" + quote)
print("your int value is this:" + num)
print("your float value is this:" + me)

