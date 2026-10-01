# Student Grade Calculator


def calculate_result():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("\nEnter student name: ").strip()

    subjects = [
        "Python",
        "Mathematics",
        "Electronics",
        "English",
        "Physics"
    ]

    marks = []

    # Get marks
    print("\nEnter marks out of 100:")

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    # Calculate total and percentage
    total = sum(marks)
    percentage = total / len(subjects)

    # Calculate grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Calculate result
    result = "PASS" if percentage >= 40 else "FAIL"

    # Display result
    print("\n" + "=" * 40)
    print("             RESULT")
    print("=" * 40)

    print(f"Student Name : {name}")

    for i in range(len(subjects)):
        print(f"{subjects[i]:15}: {marks[i]:.2f}")

    print("-" * 40)
    print(f"Total Marks  : {total:.2f}/500")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")
    print("=" * 40)


# Run the program
if __name__ == "__main__":
    calculate_result()
