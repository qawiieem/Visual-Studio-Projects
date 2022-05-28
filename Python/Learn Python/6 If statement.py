is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
else:
    print("You are either not male or not tall or both")

# If statements with comparisons

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    
print(max_num(45,56,52))
