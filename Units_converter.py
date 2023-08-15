# Converting weight between pounds and kilograms

weight = input('\nPlease enter how much you weigh:\n ')
units = input('Is it in KG or L : ')

if units.upper() == "L":
    converter = (int(weight)*0.45)
    print(f"\nYour weight is {weight} pounds") 
    print(f"\nYour weight { converter}  kg\n")

else:
    converter = (int(weight)/0.45)
    print(f" \nYour weight is {weight} kg ")
    print(f"\nYour weight is {converter} in pounds\n ")

print('Thank you for your time\n')