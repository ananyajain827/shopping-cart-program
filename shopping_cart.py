
menu={'pizza':20,
      'burger':30,
      'patties':86.9,
      'petha':56.97,
      'sandwich':43.34,
      'tortilla':78.6}

cart=[]
total=0

print("-----------MENU--------------")
for key,value in menu.items():
     print(f"{key:10}: ${value:}",end="\n")

while True:
     food=input("select item(q to quit): ").lower()
     if food=="q":
          break
     elif menu.get(food) is not None:
         cart.append(food)
     else:
        print("***item not available***")

price=0
print("\n\n--------your order----------")

for food in cart:
    total+=menu.get(food)
    price=menu.get(food)
    print(f"{food:10}",end=" ")
    print(f"{price}")
print("\n\n--------your total----------")
print(f"your total is ${total:.2f}")
