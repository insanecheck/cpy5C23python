#Input
k = input("Enter Number: ")
a = int(k)
b = a % 10
c = (( a % 100 ) - b) // 10
d = ( a - ( a % 100 )) // 100
e = b + c + d
print()

#Answer
print(e)
print()

#Acknowledgements
print ("\u00A9"+" Neo Wei Lu 2013") 
