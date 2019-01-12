#Program to calculate Weight to Height ratio.
my_age = 0
my_height = 0
my_weight = 0
my_genderV = "male"
#End of variables.
#Determine Ratio.
def result_ratio(height, weight, gender):
    if gender == "Female":
        if height <= 46:
            if weight >= 63 and weight <= 77:
        if height == 47:
            if weight >= 68 and weight <= 83:
        if height == 48:
            if weight >= 72 and weight <= 88:
        if height == 49:
            if weight >= 77 and weight <= 94:
        if height == 50:
            if weight >= 81 and weight <= 99:
        if height == 51:
            if weight >= 86 and weight <= 105:
        if height == 52:
            if weight >= 99 and weight <= 121:
        if height == 53:
        if height == 54:
            if weight >= 108 and weight <= 132:
        if height == 55:
        if height == 56:
            if weight >= 117 and weight <= 143:
        if height == 57:
        if height == 58:
            if weight >= 126 and weight <= 154:
        if height == 59:
        if height == 60:
            if weight >= 144 and weight <= 176:
        if height == 61:
        if height == 62:
            if weight >= 153 and weight <= 187:
        if height == 63:
        if height == 64:
            if weight >= 162 and weight <= 198:
        if height == 65:
        if height == 66:
            if weight is >= 171 and weight is <= 209:
        if height == 67:
        if height == 68:
            if weight >= 180 and weight <= 220:
        if height == 69:
        if height == 70:
            if weight >= 198 and weight <= 242:
#Determine Gender.
def my_gender(value):
    if value == "Male":
        return male
    if value == "Female":
        return female
#End of gender function.
value = input("Are you a Male or Female?")
#Set gender variable.
my_genderV = my_gender(value)
print(my_gender)
