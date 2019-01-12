#Program to calculate Weight to Height ratio.
my_age = 0
my_height = 0
my_weight = 0
my_genderV = "male"
#End of variables.
#Determine Ratio.
def result_ratio(height, weight, gender):
    status = "null"
    if gender == "Female":
        if height <= 46:
            if weight >= 63 and weight <= 77:
                status = "You're Fit!"
        if height == 47:
            if weight >= 68 and weight <= 83:
                status = "You're Fit!"
        if height == 48:
            if weight >= 72 and weight <= 88:
                status = "You're Fit!"
        if height == 49:
            if weight >= 77 and weight <= 94:
                status = "You're Fit!"
        if height == 50:
            if weight >= 81 and weight <= 99:
                status = "You're Fit!"
        if height == 51:
            if weight >= 86 and weight <= 105:
                status = "You're Fit!"
        if height == 52:
            if weight >= 99 and weight <= 121:
                status = "You're Fit!"
        if height == 53:
        if height == 54:
            if weight >= 108 and weight <= 132:
                status = "You're Fit!"
        if height == 55:
        if height == 56:
            if weight >= 117 and weight <= 143:
                status = "You're Fit!"
        if height == 57:
        if height == 58:
            if weight >= 126 and weight <= 154:
                status = "You're Fit!"
        if height == 59:
        if height == 60:
            if weight >= 144 and weight <= 176:
                status = "You're Fit!"
        if height == 61:
        if height == 62:
            if weight >= 153 and weight <= 187:
                status = "You're Fit!"
        if height == 63:
        if height == 64:
            if weight >= 162 and weight <= 198:
                status = "You're Fit!"
        if height == 65:
        if height == 66:
            if weight is >= 171 and weight <= 209:
                status = "You're Fit!"
        if height == 67:
        if height == 68:
            if weight >= 180 and weight <= 220:
                status = "You're Fit!"
        if height == 69:
        if height == 70:
            if weight >= 198 and weight <= 242:
                status = "You're Fit!"
    return status
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
