print("\n\n\t ========== BMI Calculator ==========")
cm = int(input("\n\t Enter your height in cm: ")) #Convert to meters
m = cm / 100
h2 = m ** 2
weight = int(input("\n\t Enter your weight in kg: "))

BMI = weight / h2 
exact = round(BMI, 2)
print(f"\n\t Your BMI is {BMI} or {exact}")
if exact < 18.5:
    print("\n\t You are underweight. \n")
elif (exact >= 18.5) and (exact < 25):
    print("\n\t You have a healthy/normal weight. \n")

elif (exact >= 25) and (exact < 30):
    print("\n\t You are overweight. \n")
elif exact >= 30:
    print("\n\t That's under the classification of obesity. \n")
else:
    print("\n\t Eat properly and drink enough amount of water 0^0 \n")