import math

print(50+50)
print(100-10)

print(30+6, 6^6, 6**6, 6+6+6+6+6+6)

print("Hello World")
print("Hello World: 10")

print("Enter the relevant data (Principal, interest Rate, payment period): ")
data = input().split()
loan = int(data[0])
rate = int(data[1]) / 1000.0
period = int(data[2])

M = loan / ((((1 + rate) ** period) - 1) / (rate * (1+rate) ** period))

print(math.ceil(M), "is the monthly payment")

