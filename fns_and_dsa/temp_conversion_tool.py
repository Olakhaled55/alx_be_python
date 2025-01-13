# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # This line should contain 9/5 for the Celsius to Fahrenheit conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global conversion factor for Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global conversion factor for Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User input for temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # User input for unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            # If the input is in Celsius, convert it to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        elif unit == "F":
            # If the input is in Fahrenheit, convert it to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle invalid input if the temperature is not a number
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
