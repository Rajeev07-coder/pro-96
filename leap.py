year=int(input("Enter year to be checked:"))

if(year % 4 ==0 and year % 100 !=0 or year % 400 ==0 ):
    print("The Year is a leap year")
else:
    print("The YEAR is not a leap year")    