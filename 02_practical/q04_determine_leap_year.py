r = int(input("Enter year: "))
if r % 400 == 0:
    print("Leap year.")
elif r% 4 == 0:
    if r% 100 == 0:
        print("Non-leap year.")
    else:
        print("Leap year.")
print()

#Acknowledgements
print ("\u00A9"+" Neo Wei Lu 2013") 

