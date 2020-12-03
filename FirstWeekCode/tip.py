# tip recomendation program
# yo enter the bill amount
# the program recommends the tip in dollars acording to a %
# 18%, 20% and 25%
# by Daniel Rosas

bill_acount = float(input(" how much is the account? "))
print (f"for USD {bill_acount} the tip you have to pay is")
print (f"USD {bill_acount*.18:.2f}\tfor 18%")
print (f"USD {bill_acount*.20:.2f}\tfor 20%")
print (f"USD {bill_acount*.25:.2f}\tfor 25%")

print ("\n---end of the program----\n")
