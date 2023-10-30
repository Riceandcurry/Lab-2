def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    value = calculate_bmi(weight=2, height=1.68)
    print(value)



def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    if bmi < 18.5:
        print("Under Weight")
        return (-1)
    elif (bmi > 25):
        print("Over weight")
        return(0)
    else:
        print("Normal weight")
        return(1)


if __name__ == "__main__":
    main()