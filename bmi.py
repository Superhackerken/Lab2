def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))
    if (bmi < 18.5):
        print("User is under weight!")
        return -1
    elif (bmi <= 25): 
        print("User has normal weight!")
        return 0
    else:
        print("User is over weight!!!")
        return 1

calculate_bmi(90, 1.73)
