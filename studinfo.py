
def grade(per):
   if per >90 and per<100:
       print("A")
   elif per >80 and per<70:
       print("B")
   elif per >70 and per<60:
       print("c")
   else:
       print("fail")

def totalmarks(stsub1, stsub2,stsub3,stsub4,stsub5):
 totalmarks = stsub1+stsub2+stsub3+stsub4+stsub5
 per = int(totalmarks * 100 / 500)
 print(int(per))

 grade(per)

stname = input("enter your name")
stid = int(input("enter student id"))
stsub1 = int(input("enter tamil marks"))
stsub2 = int(input("enter english marks"))
stsub3 = int(input("enter science marks"))
stsub4 = int(input("enter maths marks"))
stsub5 = int(input("enter computerscience marks"))
totalmarks(stsub1, stsub2,stsub3,stsub4,stsub5)


