
# School Grades System

This project is a simple Python program that allows you to register students’ grades and calculate each student's average.
The program runs in the terminal and accepts multiple grades per student, ending the input when the user types **-1**.

## ✅ Features

* Asks the user for the number of students.
* For each student:

  * Allows input of grades from **0 to 10**.
  * Ends grade input when **-1** is entered.
  * Calculates the average using the `calcular_media` function.
* Displays each student’s average formatted to two decimal places.

## 📌 Code Structure

The project contains a single Python file with:

* `calcular_media(notas)`:
  Takes a list of grades and returns the average. Returns **0** if the list is empty.

* `obter_notas_aluno()`:
  Reads grades from user input, validates the values, and returns the list of grades.

* `main()`:
  Controls the main program flow, asking for the number of students and printing each average.

## ▶️ How to Run

1. Make sure Python is installed.
2. Save the file (for example, `grades.py`).
3. Run it in the terminal:

```bash
python grades.py
```

4. Follow the on-screen instructions.

## 📝 Example Output

```
School Grades System
Enter the number of students: 2

Student 1:
Enter a grade (or -1 to finish): 8
Enter a grade (or -1 to finish): 7
Enter a grade (or -1 to finish): -1
The average for Student 1 is: 7.50

Student 2:
Enter a grade (or -1 to finish): 10
Enter a grade (or -1 to finish): 6
Enter a grade (or -1 to finish): -1
The average for Student 2 is: 8.00
```

## 📄 License

This project is free to use and study.
