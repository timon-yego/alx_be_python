#Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Function to convert fahrenheit to celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR

#Function to convert celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt user for temperature and unit
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ")

        # Convert based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is {converted_temp:.2f} degrees Fahrenheit.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature} degrees Fahrenheit is {converted_temp:.2f} degrees Celsius.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()