print("hey kunal")
hour =input("Enter Hours: ")
rate=input("Enter Rate: ")
hour=float(hour)
rate=float(rate)
if hour<40: 
    pay=round(hour*rate,2)
else: 
    overtime =hour-40
    pay=round(40* rate+overtime*rate*1.5,2)

#  print(f"Pay: {pay}")
print(f"Pay : {pay}")

year=int(input("Enter Year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not leap yr")
    else:
        print("Leap yr")
else: 
    print("Not leap yr")


#love calculator
    
    name1=(input('Enter ur name :'))
    name2=(input('Enter ur crush name :'))
compbined_name=name1+name2
compbined_name.lower()x
t=compbined_name.count("t")
r=compbined_name.count("r")
u=compbined_name.count("u")
e=compbined_name.count("e")
l=compbined_name.count("l")
o=compbined_name.count("o")
v=compbined_name.count("v")
e=compbined_name.count("e")

true=t+r+u+e
Love=l+o+v+e
Love_score=int(str(true)+str(Love))
print(Love_score)
