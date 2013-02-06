running = True
while running:
    a = int(input("Enter number: "))
    print()
    if a%2 == 0:
        print(str(a) + " is even")
        running = False
    else:
        print(str(a) + " is odd")
        running = False
print()

#Acknowledgements
print ("\u00A9"+" Neo Wei Lu 2013") 
