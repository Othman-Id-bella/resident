age=int(input("enter the age of resident:"))
sex=str(input("enter the sex of resident:"))

if (sex=="Man" and age>=20) or (sex=="Woman" and age>=18 and age<=30):
    print("the resident is taxable")
else:
    print("the resident is not taxable")