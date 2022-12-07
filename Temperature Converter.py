print("Celsius")
print("Fahrenheit")
print("Kelvin")

while True:
    unit = input("Select the temperature unit you want to convert to: ")
    if unit == "Celsius":
        temperature = input("Enter the temperature degree you want to convert: ")
        temperature_2 = input("Enter the unit of temperature you used to enter the temperature degree: ")
        if temperature_2 == "Fahrenheit":
            converted_temperature = (float(temperature) - 30) / 2
            print("Your temperature in celsius is: " + str(converted_temperature))
        elif temperature_2 == "Kelvin":
            converted_temperature = float(temperature) - 273.15
            print("Your temperature in celsius is: " + str(converted_temperature))
    if unit == "Fahrenheit":
        temperature = input("Enter the temperature degree you want to convert: ")
        temperature_2 = input("Enter the unit of temperature you used to enter the temperature degree: ")
        if temperature_2 == "Celsius":
            converted_temperature = (float(temperature) * 1.8) + 32
            print("Your temperature in Fahrenheit is: " + str(converted_temperature))
        if temperature_2 == "Kelvin":
            converted_temperature = (float(temperature) - 273.15) * 1.8 + 32
            print("Your temperature in Fahrenheit is: " + str(converted_temperature))
    if unit == "Kelvin":
        temperature = input("Enter the temperature degree you want to convert: ")
        temperature_2 = input("Enter the unit of temperature you used to enter the temperature degree: ")
        if temperature_2 == "Celsius":
            converted_temperature = float(temperature) + 273.15
            print("Your temperature in Kelvin is: " + str(converted_temperature))
        elif temperature_2 == "Fahrenheit":
            converted_temperature = (float(temperature) - 32) * 1.8 + 273.15
            print("Your temperature in Kelvin is: " + str(converted_temperature))
    ask = input("Restart the program to do another conversion? (Y)es or (N)o ")
    if ask.upper() == "N":
        break
