running = True
while running:
    z = int(input("Enter length of side: "))
    y = int(input("Enter length of side: "))
    x = int(input("Enter length of side: "))
    print()
    if z+y>x and z+x>y and x+y>z :
        perimeter = int(z + y + x)
        print("Perimeter = " + str(perimeter))
        running = False
    else:
        print("Invalid triangle! Try again")
print()

#Acknowledgements
print ("\u00A9"+" Neo Wei Lu 2013")

