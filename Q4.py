"""4) Get the height from the user in cms and display the user height back to console
in foot/feet and inches"""

height_cm = float(input("Enter your height in centimeters:"))
#1 foot = 30.48 cm
height_feet = int(height_cm // 30.48)
#inch = 2.54 cm
height_inches = int((height_cm % 30.48)/2.45)
print(f"Your height is {height_feet} feet {height_inches} inches")