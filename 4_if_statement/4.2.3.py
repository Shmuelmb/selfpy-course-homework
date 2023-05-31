# Temperature Conversion
# This code converts a temperature value from Fahrenheit to Celsius or vice versa.

# Get the temperature input from the user
x = input("Enter temperature: ")

# Check if the input contains "f" or "F" to determine the conversion type
if "f" in x.lower():
    # Fahrenheit to Celsius conversion
    c = (float(x[:-1]) - 32) * 5 / 9
    print(f"The temperature in Celsius is: {c:.2f}C")
if "c" in x.lower():
    # Celsius to Fahrenheit conversion
    f = (float(x[:-1]) * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is: {f:.2f}F")
