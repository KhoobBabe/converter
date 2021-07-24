print("a) Miles to Km")
print("b) Celcius to Fahrenheit")
print("c) Feet to Meters")
print("d) Yards to Meters")
print("e) Exit Program")

         
def miles_to_km(y):
    print(y*0.621371)
    return

def cel_to_fahr(y):
    print((y*1.8)+32)
    return

def feet_to_m(y):
    print(y/3.28)
    return

def yard_to_m(y):
    print(y*0.9144)
    return

def end_program(y):
    break
    print("exit the program")


def conv(x):
    x = input("Choose the program for conversion:")
    while x==(a, b, c, d, e):
        if x==a:
            miles_to_km(x)
        elif x==b:
            cel_to_fahr(x)
        elif x==c:
            feet_to_m(x)
        elif x==d:
            yard_to_m(x)
        elif x==e:
            end_program(x)



y= float(input("Enter the value to be converted:"))
