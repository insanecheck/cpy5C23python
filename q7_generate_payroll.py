#Input
name = input("Enter name: ")
hours = input("Enter number of hours worked weekly: ")
rate = input("Enter hourly pay rate: ")
CPF = input("Enter CPF contribution rate(%): ")
print()

#Conversion
h = float(hours)
r = float(rate)
gross = float( h * r )
c = float(CPF)
p = float( c / 100 )
f = float( p * gross )
n = "{0:<.2f}".format(float( gross - f))

#Answer
print("Payroll statement for " + str(name))
print("Number of hours worked in this week: " + str(hours))
print("Hourly pay rate: $" + str(rate))
print("Gross pay: $" + str(gross))
print("CPF contribution at " + str(CPF) + "%= $" + str(f))
print()
print("Net pay = $" + str(n))
print()

#Acknowledgements
print ("\u00A9"+" Neo Wei Lu 2013") 
