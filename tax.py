# individual tax liability and after tax income calculator
# the tax liabilties are calulated 

def individual_tax_liability(income):
  income=int(input("gross income: "))

  if income<= 18200:
      tax_liab=0
      a_tax= income-tax_liab
  elif (income>18200) and (income<=37000):
      tax_liab=(income-18200)*(19//100)
      a_tax= income-tax_liab
  elif (income>37000) and (income<=87000):
      tax_liab=3572+(income-37000)*(325//100)
      a_tax= income-tax_liab
  elif (income>87000) and (income<=180000):
      tax_liab=19822+(income-87000)*(37/100)
      a_tax= income-tax_liab
  elif income>180000:
      tax_liab=54532+(income-180000)*(45/100)
      a_tax= income-tax_liab
return(tax_liab)
return(a_tax)
input()
