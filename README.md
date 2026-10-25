# Messy Python Code Improvement

I took a messy but working Python program and improved it with the help of AI,
making it readable, safer and easier to change. The program reads student marks,
then prints each student's total, percentage and grade, the class average and the topper.

## Files

| File | What it is |
|------|------------|
| `messy_code.py` | The original messy version (before) |
| `improved_code.py` | The cleaned-up version (after) |

## What was wrong with the messy version

- Variable names like `a`, `t`, `p`, `g`, `x`, `sm` do not say what they store
- Everything is in one long block, with no functions
- Four separate lists must be kept in sync by index
- Numbers like `300` are written directly in the code, so changing the number of subjects breaks it
- No input checking: typing a letter or marks like 500 is accepted or crashes the program
- Crashes with 0 students (division by zero)
- No comments or explanation
- Output is hard to read (raw numbers like `95.66666666666667`)

## What I improved

| Problem | Improvement |
|---------|-------------|
| Unclear names | Meaningful names such as `student`, `total`, `percentage`, `grade` |
| One long block | Small functions that each do one job: `read_int`, `calculate_grade`, `read_student`, `print_report`, `main` |
| Four parallel lists | A `Student` dataclass that keeps one student's data together |
| Hard-coded numbers | Constants at the top: `NUM_SUBJECTS`, `MAX_MARKS_PER_SUBJECT`, `GRADE_BOUNDARIES` |
| Long if/elif chain | A grade table that is looped through |
| No validation | `read_int` keeps asking until the input is a valid number in range |
| Crash on 0 students | The program requires at least 1 student |
| Manual loops for average and topper | `sum()` and `max()` |
| No documentation | A docstring on the file and on every function |
| Ugly output | Aligned columns and numbers rounded to 2 decimals |
| Code runs when imported | `if __name__ == "__main__":` guard |

## How to run

```
python messy_code.py
python improved_code.py
```

(On some systems use `python3` instead of `python`.)

## Technologies

Python, GitHub

## Author
Samriddhi Sharma
