def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()


if __name__ == "__main__":
    main()


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

