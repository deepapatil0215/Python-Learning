ph = int(input("enter the phonenumner"))
name = input("enter your name")
amount = float(input("enter the purchase amount"))
print(name)
print(ph)



def disc(amount):
 if amount >= 500:
  disc_rate = 0.20 
 elif amount >= 200:
  disc_rate = 0.10
 elif amount >= 100:
  disc_rate = 0.05
 else:
  disc_rate = 0.0

 discount = amount * disc_rate
 final_price = amount - discount
 return discount, final_price

discount,final_price = disc(amount)
print(discount)
print(final_price)
