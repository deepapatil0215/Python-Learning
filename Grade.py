# grade calulator

studid = int(input(" Enter student id"))
studname = input(" Enter student name")
sub1 = int(input(" Enter English marks "))
sub2 = int(input(" Enter Tamil marks "))
sub3 = int(input(" Enter science marks "))
sub4 = int(input(" Enter maths marks "))
sub5 = int(input(" Enter computerscience marks "))
print(studname)
print("english marks"+str(sub1))
print("Tamil marks"+str(sub2))
print("science marks"+str(sub3))
print("maths marks"+str(sub4))
print("Computer science marks"+str(sub5))
total = sub1+sub2+sub3+sub4+sub5
print("Total Marks for the student"+str(total))
per = int(total*100/500)
print("percenatge of student"+str(per))

def grade(per):
 if 90 <= per <= 100:
   return "A"
 elif 80 <=per <= 90:
   return "B"
 elif 70 <=per <= 80:
   return "B"
 else:
  return "fail"


gradecalc = grade(per)

print(gradecalc)




