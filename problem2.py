"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    while True:
        value = input("What is the temperature? ").strip()
        try:
            temperature = float(value)
            break
        except ValueError:
            print("Please enter a valid number for the temperature.")

    while True:
        unit = input("In C or F? ").strip().upper()
        if unit == "C":
            converted = celsius_to_fahrenheit(temperature)
            print(f"The temperature is {converted:.2f} °F")
            break
        if unit == "F":
            converted = fahrenheit_to_celsius(temperature)
            print(f"The temperature is {converted:.2f} °C")
            break
        print("Please enter 'C' or 'F'.")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()
