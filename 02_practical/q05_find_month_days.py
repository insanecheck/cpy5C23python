month = [ "January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
a = int(input("Enter Month: "))
b = int(input("Enter Year: "))
print()
if a == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    print( month[a-1] +" " + str(b) + " has 31 days.")
elif a == (4 or 6 or 9 or 11):
    print(month[a-1] +" " + str(b) + " has 30 days.")
else:
    if b%400==0 or (b%4==0 and b%100!=0):
        print(month[a-1] + " " + str(b) + " has 29 days.")
    else:
        print(month[a-1] + " " + str(b) + " has 28 days.")
print()

#Acknowledgements
print ("\u00A9"+" Neo Wei Lu 2013") 

