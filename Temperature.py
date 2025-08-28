def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    # Convert from input unit to Celsius first
    if from_unit == 'celsius' or from_unit == 'c':
        celsius = value
    elif from_unit == 'fahrenheit' or from_unit == 'f':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == 'kelvin' or from_unit == 'k':
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError("Invalid from_unit. Choose from Celsius, Fahrenheit, Kelvin.")

    # Convert from Celsius to target unit
    if to_unit == 'celsius' or to_unit == 'c':
        return celsius
    elif to_unit == 'fahrenheit' or to_unit == 'f':
        return celsius_to_fahrenheit(celsius)
    elif to_unit == 'kelvin' or to_unit == 'k':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError("Invalid to_unit. Choose from Celsius, Fahrenheit, Kelvin.")

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    from_unit = input("Convert from (Celsius, Fahrenheit, Kelvin): ")
    to_unit = input("Convert to (Celsius, Fahrenheit, Kelvin): ")

    try:
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.2f} {to_unit}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
