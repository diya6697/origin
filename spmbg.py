#supermarker bill generation
from datetime import datetime
name = input("enter your name:")


s="""
     Rice    Rs   20/kg
     Sugar   Rs   30/kg
     Salt    Rs   20/kg
     oil     Rs   80/liter
     paneer  Rs   110/kg
     maggie  Rs   50/kg
     Boost   Rs   90/each
     colgate Rs   85/each
 """
its={"rice":20,"sugar":30,"salt":20,"oil":80,"paneer":110,"maggie":50,"boost":90,"colgate":85}
pricelist=[]
ilist=[]
plist=[]
qlist=[]
price=0
totalPrice=0
finalAmount=0
lst = int(input("for list of items press 1:"))
if lst==1:
    print(s)
#for i in range(len(its)):
    ch=int(input("if you want to buy press 1 or press 2 for exit:"))   
#    if ch==2:
#       break 
    if ch==1:
       it=input("Enter your Items:")
       qty=int(input("Enter Quantity:"))
       if it in its.keys():
        price=qty*(its[it])
        pricelist.append((it,qty,its,price))
        totalPrice+=price
        ilist.append(it)
        qlist.append(qty)
        plist.append(price)
        gst=(totalPrice*5)/100
        finalAmount=gst+totalPrice
    else:
        print("Item is out of stock")
else:
   print("invalid")     
bill=input("Can i bill the items yes or no:")
if bill=="yes":
    pass
    if finalAmount!=0:
       print("calculate bill")
       print(25*"=","more super market",25*"=")
       print(28*"=","@nizampet",28*"=")
       print("Name:",name,20*" ","date:",datetime.now())
       print(75*"-")
       print("sno",8*" ","items",8*" ","quantity",3*" ","price")
       for i in range(len(plist)):
          print(i,10*" ",ilist[i],9*" ",qlist[i],10*" ",plist[i])
       print(75*"-")
       print('Totalamount:',50*" ",'Rs',totalPrice)
       print('gst amount:',51*" ",'Rs',gst)
       print(75*"-")
       print(50*" ",'FinalAmount:','Rs',finalAmount)
       print(75*"-")
       print(20*"*","thanks for visisting revisist again",20*"*")
       print(75*"-")
          
    
         
      
       
         

