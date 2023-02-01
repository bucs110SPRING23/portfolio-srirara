rate = float(input("What is the exchange rate?"))
amount = float((input("How much do you want to exchange?")))
total = amount * rate

print("A $3 service fee was deducted")
result = total - 3
print("You get $", result)
