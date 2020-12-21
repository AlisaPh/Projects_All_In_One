num=int(input("Enter a number between 1 to 99: "))
digit=int(input("Enter a number: "))
if(num>99 or num<1):
    print("EROR")
else:
    print(num.count(digit))