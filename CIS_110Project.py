print(f"\nWelcome to Bee's Ice Cream!")
print(f"\nHi, I am Kelly your virtual assistant! How may we serve you today!")   

size = input("\nWhat size ice cream will you be getting? Enter small or large: ")
while size.lower() not in ["small", "large"]:
    size = input("Invalid value! Please enter small or large: ")

flavor = input("Which flavor has your eye? Enter a flavor: ")
while len(flavor) ==0:
    flavor = input("Flavor cannot be blank! Please a flavor: ")
    
toppings = input("Will you be adding toppings? Enter yes or no: ")
while toppings not in ["yes", "no"]:
    toppings = input("Invalid answer! Please enter yes or no: ")
    
quantity = input("How many of these do you want? Enter a numeric value: ")
while not quantity.isdigit():
    quantity = input("\nValue not recognized. Please enter a numeric value! ")
    
quantity =int(quantity)
method = input("\nWill this be dine in or delivery: ")
while method not in ["dine in", "delivery"]:
    method = input("Invalid value! Please enter dine in or delivery: ")

if method.lower() == "delivery":
    deliveryFee = 1
else:
    deliveryFee = 0

salesTax = 1.5

if size.lower() == "small":
    iceCreamCost = 3.25
elif size.lower() == "large":
    iceCreamCost = 6.50
    
total = (iceCreamCost * quantity) * salesTax + deliveryFee
print("-" * 10)
print(f"Thank you, for your order.")
print(f"Your {quantity} {size} {flavor} iceCream costs ${total:,.2f}. ")

if total >=5:
    print("\nCongratulations! You've been awarded a $1 Off coupon for your next order! ")
else:
     print("\nCongratulations! You will receive a free cone! ")
     
print("-" * 10)

print("Order has been received. ETA 3 minutes!" )
for min in range(3, 0, -1):
    print(min, "minutes remaining")
    for seconds in range(60, 0, -1):
        print(seconds, end = "\r")
        import time
        time.sleep(1)
print("Order is ready!")

keepGoing = input("Do you want to place another order? Enter y or n: ")
while keepGoing.lower() not in ["y", "n"]:
    keepGoing - input("Invalid value! Enter y or n: ")