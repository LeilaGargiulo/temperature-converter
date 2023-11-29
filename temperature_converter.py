print("Welcome to Temperature Converter, a lightweight utility for converting temperatures. ")
# create variables for units being converted and the temperature
unit = input("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature you want converted: "))

# Function that converts C to F
def c_to_f(temp_C):
    converted_c = temp_C * (9/5) + 32
    return converted_c

# Function that converts F to C
def f_to_c(temp_F):
    converted_f = (temp_F - 32) * (5/9)
    return converted_f

# Function that converts F to K
def f_to_k(temp_F):
    converted_k = (temp_F - 32) * (5/9) + 273.15
    return converted_k

# Function that converts K to F
def k_to_f(temp_K):
    converted_f = (temp_K - 273.15) * (9/5) + 32
    return converted_f

# Main function using conditionals that decides which convert function to select
def main():
    if(unit == "C"):
        celcius_to_fahrenheit = c_to_f(value)
        return celcius_to_fahrenheit
    elif(unit == "F"):
        fahrenheit_to_celcius = f_to_c(value)
        fahrenheit_to_kelvin = f_to_k(value)
        return fahrenheit_to_celcius, fahrenheit_to_kelvin
    elif(unit == "K"):
        kelvin_to_fahrenheit = k_to_f(value)
        kelvin_to_celsius = value - 273.15
        return kelvin_to_fahrenheit, kelvin_to_celsius
    else:
        warning = "Please enter C, F or K to specify the unit: "
        return warning

# Print results
result = main()
if isinstance(result, tuple):
    print("Your value in Celsius is: " + str(result[1]))
    print("Your value in Fahrenheit is: " + str(result[0]))
else:
    print("Your value is: " + str(result))