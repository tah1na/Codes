print("Hello, I'm a calculator and I can give you the gravitational force between any two objects")
G = 6.67* (10 ** -11)
m1 = float(input("Enter mass of the first object : "))
m2 = float(input("Enter mass of second object : "))
r = float(input("Enter distance : "))
F = (G * m1 * m2) / (r ** 2)
result = F 
print(result)