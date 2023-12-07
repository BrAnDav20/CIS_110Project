print(f"\nWelcome to Bee's Ice Cream!")
print(f"\nHi, I am Kelly your virtual assistant! How may we serve you today!")   

size = input("\nWhat size ice cream will you be getting? Enter cone or cup: ")
while size.lower() not in ["cone", "cup"]:
    size = input("Invalid value! Please enter cone or cup: ")

flavor = input("Which flavor has your eye? Enter a flavor: ")
while len(flavor) ==0:
    flavor = input("Flavor cannot be blank! Please a flavor: ")
    
toppings = input("Will you be adding toppings? Enter yes or no: ")
while toppings not in ["yes", "no"]:
    toppings = input("Invalid answer! Please enter yes or no: ")
    
quantity = input("How many of these do you want? Enter a numeric value: ")
while not quantity.isdigit():
    quantity = input("\nValue not recognized. Please enter a numeric value! ")
    
    quanity =int(quantity)
method = input("\nWill this be dine in or carry out: ")
while method not in ["dine in", "carry out"]:
    method = input("Invalid value! Please enter dine in or carry out: ")

salesTax = 0.5

if size.lower() == "cone":
    icecreamCost = 1.25
elif size.lower() == "cup":
    icecreamCost = 2.50
    
total = (icecreamCost * quantity) * salesTax 
print("-" * 10)
print(f"Thank you, for your order.")
print(f"Your {quantity} {size} {flavor} iceCream costs ${total:,.2f}. ")

if total >=5:
    print("\nCongratulations! You've been awarded a $1 Off coupon for your next order! ")
else:
     print("\nCongratulations! You will receive a free cone! ")
     
     
    