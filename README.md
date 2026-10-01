# Student Grade Calculator

A simple beginner-friendly Python project that calculates a student's total marks, percentage, grade, and pass/fail result.

## 📌 Project Description

The Student Grade Calculator is a command-line Python application.

The user enters the student's name and marks for five subjects. The program then calculates:

- Total marks
- Percentage
- Grade
- Pass/Fail result

The project also validates the entered marks and handles invalid inputs.

## 🚀 Features

- Enter student name
- Enter marks for multiple subjects
- Marks validation (0–100)
- Calculate total marks and percentage
- Calculate grade
- Determine pass/fail result
- Display formatted result
- Handle invalid numerical input

## 🛠️ Technologies Used

- Python 3
- VS Code
- Git & GitHub

## 🐍 Python Concepts Used

- Variables and data types
- Strings and lists
- Functions
- `input()` and `print()`
- `if`, `elif`, `else`
- `for` and `while` loops
- Exception handling (`try-except`)
- `range()` and `sum()`
- String formatting
- Conditional expressions

## 📂 Project Structure

```text
student-grade-calculator-python/
│
├── main.py
├── README.md
└── .gitignore
```

## ▶️ How to Run

1. Install Python 3 from the official Python website.

2. Clone the repository:

```bash
git clone https://github.com/yourusername/student-grade-calculator-python.git
```

3. Open the project:

```bash
cd student-grade-calculator-python
```

4. Run the program:

```bash
python main.py
```

On Windows, if `python` doesn't work, try:

```bash
py main.py
```

## 📊 Grading System

| Percentage | Grade |
|------------|-------|
| 90–100%    | A+    |
| 80–89%     | A     |
| 70–79%     | B     |
| 60–69%     | C     |
| 50–59%     | D     |
| Below 50%  | F     |

A percentage of 40% or above is considered **PASS**.

## 💻 Example

```text
========================================
       STUDENT GRADE CALCULATOR
========================================

Enter student name: Om

Enter marks out of 100:
Python: 85
Mathematics: 72
Electronics: 81
English: 78
Physics: 69

========================================
             RESULT
========================================
Student Name : Om
Python         : 85.00
Mathematics    : 72.00
Electronics    : 81.00
English        : 78.00
Physics        : 69.00
----------------------------------------
Total Marks  : 385.00/500
Percentage   : 77.00%
Grade        : B
Result       : PASS
========================================
```

## 🔮 Future Improvements

- Add more subjects
- Store student results in a file
- Support multiple student records
- Add a graphical user interface
- Generate result reports
- Add student ID and ranking

## 👨‍💻 Author

Om Shinde
B.Tech Electronics & Telecommunication Engineering

## 📄 License

This project is created for educational and learning purposes.
