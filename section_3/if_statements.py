age: int = 30

if age > 21:
    print("You may enter the club!")
else:
    print("You are not allowed to enter the club!")

weather: str = "cloudy"

if weather == "clear":
    print("It is a nice day!")
elif weather == "cloudy":
    print("It is a bit gloomy today!")
elif weather == "rainy":
    print("It is raining today!")
else:
    print("I don't know what the weather is like today!")

# original if statement
number: int = 0

if number > 0:
    result: str = "Above 0"
else:
    result: str = "0 and below"

# shortend if statement
result: str = "Above 0" if number > 0 else "0 and below"
print(result)

# original if statement

condition: bool = True
if condition:
    var: str = "True"
else:
    var: str = "False"

var: str = "True" if condition else "false"
print(var)
