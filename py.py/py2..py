
"""


name=input("Enter your name : ")
print (f"hello {name}.")
print("Wlcm bro")

print("group name generator")
color=input("Yur fav coolor \n")
animal=input("whats ur fav animal \n")
print(animal)
print(color)


hour =input("enter hour")
rate=input("Enter rate")
hour=float(hour)
rate=float(rate)
#print((hour*rate))
#print(newHour*newrate)

pay=round(hour*rate,2)
print(f"Pay: {pay}")

Celcius = input("Enter Temperature in Celcius: ")
celcius =int(Celcius)
farenheit=celcius* 9/5+32
print(f"{celcius} Celcius={farenheit}Farenheit")


print("Welcome to the trip cost calculator")
day=int(input("How many days will u stay? "))
hotel_price=float(input("How much does hotel cost per night? $"))
flight_price=float(input("How much does flight cost? $"))
car_price=float(input("If u need rental car please enter the price otherwise enter zero. $"))
other_expenses=float(input("Enter other possible expenses $" ))
total_cost=round((day*(hotel_price)+day*(flight_price)+day*(car_price)+day*(other_expenses)),2)
print(f" Total COst : ${total_cost}")


"""

input_Score=input("Enter score:  ")
score =float(input_Score)
try:
    score=float(input_Score)
except ValueError:
    print("Bad score")
    quit()

if score>0.0 and score<=1.0:
    if score>=0.9:
        print("A")
    elif  score>0.8:
        print("B")
    elif score>0.7:
        print("c")
    elif score>0.6:
        print("C")
    else:
        print("NULLa")

else:
    print("very Bad !")