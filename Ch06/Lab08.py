# Converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32


# Converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


print(
    format("Celsius", "20s"), "Fahrenheit",
    " | ", format("Fahrenheit", "20s"),
    format("Celsius", ">10s"), end="\n\n"
)

celsius = 40
fahrenheit = 120
for degree in range(0, 10):
    print(format(celsius, "<20.1f"), format(celsiusToFahrenheit(celsius), "10.2f"),
          " | ", format(fahrenheit, "<20.1f"), format(fahrenheitToCelsius(fahrenheit), ">10.2f"))
    celsius -= 1
    fahrenheit -= 10
