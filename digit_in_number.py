num=input("Enter a number between 1 to 99: ")
digit=input("Enter a number: ")
if(int(num)>99 or int(num)<1):
    print("EROR")
else:
    print(num.count(digit))
