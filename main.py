import pandas as pd
import numpy as np

from functions import calculate_grade
from functions import check_result
from functions import get_performance_level


# Load student dataset
df = pd.read_csv("students.csv")


# Display project title
print("=" * 60)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)


# Display student data
print("\nSTUDENT DATA")
print("-" * 60)
print(df.to_string(index=False))


# Display basic information
print("\n\nDATASET INFORMATION")
print("-" * 60)

print("Number of Students:", len(df))
print("Number of Columns:", len(df.columns))

print("\nColumns:")
print(list(df.columns))

# Calculate total and average marks

subjects = ["Python", "DBMS", "Data_Structures"]

df["Total_Marks"] = df[subjects].sum(axis=1)

df["Average_Marks"] = np.round(
    df["Total_Marks"] / len(subjects), 2
)


# Display total and average
print("\n\nMARKS ANALYSIS")
print("-" * 60)

print(
    df[
        ["Student_ID", "Name", "Total_Marks", "Average_Marks"]
    ].to_string(index=False)
)

# Assign grades to students

df["Grade"] = df["Average_Marks"].apply(calculate_grade)


# Display grades
print("\n\nGRADE ANALYSIS")
print("-" * 60)

print(
    df[
        ["Student_ID", "Name", "Average_Marks", "Grade"]
    ].to_string(index=False)
)

# Check pass or fail

df["Result"] = df["Average_Marks"].apply(check_result)


# Display pass/fail result
print("\n\nPASS / FAIL ANALYSIS")
print("-" * 60)

print(
    df[
        ["Student_ID", "Name", "Average_Marks", "Grade", "Result"]
    ].to_string(index=False)
)

# Count passed and failed students

pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\nNumber of Passed Students:", pass_count)
print("Number of Failed Students:", fail_count)

# Class performance analysis

highest_average = df["Average_Marks"].max()
lowest_average = df["Average_Marks"].min()
class_average = np.mean(df["Average_Marks"])


print("\n\nCLASS PERFORMANCE ANALYSIS")
print("-" * 60)

print("Highest Average:", highest_average)
print("Lowest Average:", lowest_average)
print("Overall Class Average:", round(class_average, 2))

# Find top 5 performing students

top_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)


print("\n\nTOP 5 PERFORMING STUDENTS")
print("-" * 60)

print(
    top_students[
        ["Student_ID", "Name", "Average_Marks", "Grade"]
    ].to_string(index=False)
)

# Subject-wise performance analysis

print("\n\nSUBJECT-WISE PERFORMANCE")
print("-" * 60)

for subject in subjects:
    average = np.mean(df[subject])
    highest = np.max(df[subject])
    lowest = np.min(df[subject])

    print("\n" + subject)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


    # Find the best performing subject

subject_averages = df[subjects].mean()

best_subject = subject_averages.idxmax()
best_subject_average = subject_averages.max()


print("\n\nBEST PERFORMING SUBJECT")
print("-" * 60)

print("Subject:", best_subject)
print("Average Marks:", round(best_subject_average, 2))

# Attendance analysis

average_attendance = np.mean(df["Attendance"])

print("\n\nATTENDANCE ANALYSIS")
print("-" * 60)

print("Average Attendance:",
      round(average_attendance, 2), "%")

# Students with attendance above 90%

high_attendance = df[df["Attendance"] > 90]

print("\nSTUDENTS WITH ATTENDANCE ABOVE 90%")
print("-" * 60)

print(
    high_attendance[
        ["Student_ID", "Name", "Attendance"]
    ].to_string(index=False)
)

# -----------------------------------------
# FINAL PROJECT SUMMARY
# -----------------------------------------

print("\n")
print("=" * 60)
print("              FINAL PROJECT SUMMARY")
print("=" * 60)

print("Total Students:", len(df))
print("Class Average:", round(class_average, 2))
print("Highest Average:", highest_average)
print("Lowest Average:", lowest_average)
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)
print("Best Subject:", best_subject)
print("Best Subject Average:", round(best_subject_average, 2))
print("Average Attendance:", round(average_attendance, 2), "%")

print("\nTop Performer:")
top_student = df.loc[df["Average_Marks"].idxmax()]

print("Name:", top_student["Name"])
print("Average Marks:", top_student["Average_Marks"])
print("Grade:", top_student["Grade"])

print("\n" + "=" * 60)
print("       STUDENT PERFORMANCE ANALYSIS COMPLETED")
print("=" * 60)