#Write a program that accepts a student name and GPA
#Test to see whether the student makes Dean's List or Honor Roll

def main():

    while True:
        last_name = input("Enter student's last name (enter 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()





