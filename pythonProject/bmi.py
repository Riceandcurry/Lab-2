def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print(bmi)
    if bmi < 18.5:
        print("Under Weight")
    elif (bmi > 25):
        print("Over weight")
    else:
        print("Normal weight")
calculate_bmi(weight=2, height=1.68)

