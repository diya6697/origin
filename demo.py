# print("hello")
# print(input("enter something:"))

#Finding simpleInterest SI=PTR/100

# amount = int(input("enter amount:"))
# time = int(input("enter time:"))
# rate = int(input("enter rate of interest:"))
# si = ((amount*time*rate)/100)
# print("simple interest for given amount is",si)

#Finding CompondInterest CI=P(1+r/100)t
# principle = int(input("enter principle amount:"))
# rate = int(input("enter rate of interest:"))
# total_year = int(input("enter no of years:"))
# a = principle*(pow((1+rate/100),total_year))
# ci=a-principle
# print("compound interest for given amount is",ci)


#ATM
name="divya"
pwd ="123456"
u_name=input("enter the username:")
password=input("enter password:")
s="""" 
1.creditcard
2.debitcard
3.ministatement
4.exit
"""
Amount = 1000
if name==u_name and pwd==password:
 while True:
  print(s)
  option=int(input("enter option: "))
  if option==1:
       cr=int(input("enter amount to credit: "))
       Amount=cr+Amount
       print("amount after credit:",Amount)
  elif option==2:
   dr=int(input("enter amount to debit: "))
   Amount=Amount-dr
   print("amount after debit:",Amount)
  elif option==3:
   print("###&&Amount&&###",Amount,'###&&Amount&&###')
  elif option==4:
    break
else:
  print("invalid credentials")




