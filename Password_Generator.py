import random
import string

def generate_password(min_length, numbers=True, special_characters=True):

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits

    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd)< min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

print('LENGTH OF PASSWORD REQUIRED:')
n = int(input())

print('NEED NUMBERS ?: Y OR N')
a = input()

print('NEED SPECIAL CHARACTERS ? : Y OR N')
b = input()

def func_1(var):
  if var.upper()=='Y':
    var = True
  else:
    var = False
  return var
pw = generate_password(n,func_1(a),func_1(b))
print("")
print("Password :", pw)



