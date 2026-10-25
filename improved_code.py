"""
Student Report Program (improved version).

Reads the name and marks of several students, then prints each student's
total, percentage and grade, followed by the class average and the topper.
"""

from dataclasses import dataclass

# ---------- Settings (change them here, in one place) ----------
NUM_SUBJECTS = 3
MAX_MARKS_PER_SUBJECT = 100

# (minimum percentage, grade) - checked from the top, first match wins
GRADE_BOUNDARIES = [
    (90, "A"),
    (75, "B"),
    (60, "C"),
    (40, "D"),
]
FAILING_GRADE = "F"


@dataclass
class Student:
    """Holds the result of one student."""
    name: str
    total: int
    percentage: float
    grade: str


def read_int(prompt, minimum, maximum):
    """Keep asking until the user types a whole number between minimum and maximum."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum <= value <= maximum:
            return value
        print(f"Please enter a number between {minimum} and {maximum}.")


def calculate_grade(percentage):
    """Return the grade letter for a percentage."""
    for minimum_percentage, grade in GRADE_BOUNDARIES:
        if percentage >= minimum_percentage:
            return grade
    return FAILING_GRADE


def read_student(number):
    """Ask for one student's details and return a Student."""
    name = input(f"Name of student {number}: ").strip()

    total = 0
    for subject in range(1, NUM_SUBJECTS + 1):
        total += read_int(
            f"  Marks in subject {subject} (0-{MAX_MARKS_PER_SUBJECT}): ",
            0,
            MAX_MARKS_PER_SUBJECT,
        )

    percentage = total / (NUM_SUBJECTS * MAX_MARKS_PER_SUBJECT) * 100
    return Student(name, total, percentage, calculate_grade(percentage))


def print_report(students):
    """Print every student's result, the class average and the topper."""
    print("\n--- Student Report ---")
    for student in students:
        print(
            f"{student.name:<15} Total: {student.total:<4} "
            f"Percentage: {student.percentage:6.2f}%  Grade: {student.grade}"
        )

    average = sum(s.percentage for s in students) / len(students)
    topper = max(students, key=lambda s: s.total)

    print(f"\nClass average: {average:.2f}%")
    print(f"Topper: {topper.name} ({topper.total} marks)")


def main():
    count = read_int("How many students? ", 1, 1000)
    students = [read_student(number) for number in range(1, count + 1)]
    print_report(students)


if __name__ == "__main__":
    main()
