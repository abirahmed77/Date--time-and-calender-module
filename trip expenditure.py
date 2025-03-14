def hotelCost(nights):
    return 140 * nights

def planeRideCost(city):
    if city == "Dhaka":
        return 222
    
    elif city == "Chattogram":
        return 475
    
    elif city == "Jashore":
        return 183
    
    elif city == "Feni":
        return 220
    
def rentalCarCost(days):
    if days >= 7:
        return (40 * days) - 50
    elif days >= 3:
        return (40 * days) - 20
    else:
        return (40 * days)
    
def tripCost(city, days):
    hC = hotelCost(days)
    rC = rentalCarCost(days)
    pC = planeRideCost(city)
    
    sum = hC + rC + pC
    
d = int(input("Enter the amount of days you will stay(in digit) : "))
c = input("Enter the city ou are going to : ")

print()

print(f"Hotel Cost : ${hotelCost}")
print(f"Car Cost : ${rentalCarCost}")
print(f"Plane Cost : ${planeRideCost}")
print(f"Total Cost : ${tripCost(c, d)}")