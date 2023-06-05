#Convert a temperature from Fahrenheit to Celsius.
tem = float(input("Enter temperature in Fahrenheit "))

if tem >= -459.67:
    cels = round((tem - 32)*(5/9),2)
    print(f"{tem}F son {cels}°C")
else:
    print("Temperature below absolute zero")