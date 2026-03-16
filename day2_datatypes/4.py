quote=input("enter the string:")
num=eval(input("enter the no:"))
me=eval(input("enter the f.no:"))  


print("below datatypes as per your data")
num=str(num)                        
me=str(me)

print(type(quote))
print(type(num))
print(type(me))

#several ways:

#print("your string value is:" + quote + "\n your int value is:" + num + "\n your float value is:"+ me )
print(f"str value: {quote} \nint value: {num}  \nfloat value: {me} ")

#print("your string value {} \n your int valye {}" .format(quote,num)
#print("your string is %s \n your num is %d \n your float value %f" %(quote,num,me)) #for this we have to remove the convertion part otherwise it will give error