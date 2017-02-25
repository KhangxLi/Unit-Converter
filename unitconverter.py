import time

def main_menu():
    print("\n What would ou like to do? Here are your converters:")
    print("\n 1. Convert between Celsius (C), Fahrenheit (F) and Kelvin(K) temperatures.")
    cmd = input("\n Select by entering the converter's number: ")
    if cmd == '1':
        tempcon()

def tempcon():
    print("\n Temperature Converter \n 'c' for Celsius \n 'f' for Fahrenheit \n 'k' for Kelvin")
    cmd = input("\n Enter the letter corresponding to your temperature: ")
    if cmd == 'c':
        converting_cel()
    if cmd == 'f':
        converting_fah()
    if cmd == 'k':
        converting_kel()

def converting_cel():
    C = float(input("\n Enter your temperature: "))
    F = round((C * 1.8) + 32, 3)
    K = round(C + 273.15, 3)
    print("\n %s C is %s F and %s K" % (C, F, K))
    if C < -273.15:
        zero_note()
    afterTemp()

def converting_fah():
    F = float(input("\n Enter your temperature: "))
    C = round((F - 32) / 1.8, 3)
    K = round(C + 273.15, 3)
    print("\n %s F is %s C and %s K" % (F, C, K))
    if F < -459.67:
        zero_note()
    afterTemp()

def converting_kel():
    K = float(input("\n Enter your temperature: "))
    C = round(K - 273.15, 3)
    F = round((C * 1.8) + 32, 3)
    print("\n %s K is %s C and %s K" % (K, C, F))
    if F < -459.67:
        zero_note()
    afterTemp()

def welcome():
    print("Welcome to our ORDINARY UNIT CONVERTER.")

def zero_note():
    time.sleep(1)
    print("\n Note however that -273.15 C, -459.67 F or 0 K is the absolute zero where atoms stop moving. It cannot get colder than that.")
    
def afterTemp():
    time.sleep(1)
    print("\n 'a' for another celsius conversion \n 'b' for another temperature unit conversion \n 'c' for the main menu")
    cmd = input("\n Select your next course of action: ")
    if cmd == 'a':
        converting_cel()
    if cmd == 'b':
        tempcon()
    if cmd == 'c':
        main_menu()

welcome()
main_menu()




