## Part 1

p=int(input("Enter principle amount : "))
n=int(input("Enter loan term in years : "))
r=int(input("Enter the interest rate : "))

ans = ((p*n*r)/100)
print(ans)


## Part 2
print("Part 2\n")

food = ["Steak", "Asparagus", "Taco Soup", "Salmon", "Chicken"]

print(food[2])
print("\n")

food.append("Brussel Sprouts")

for i in food:
    print(i + "\n")

food.insert(3, "tacos")

for i in food:
    print(i + "\n")

## Part 3

for i in range(5):
    print("I am a programmer\n")

for i in range(1, 10):
    x = i*i
    ans = "{} : {}\n".format(i, x)
    print(ans)

input("Press enter to exit...")
