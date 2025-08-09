# Student Marks & Grade Calculator

print("=== Student Marks & Grade Calculator ===")

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i} (out of 100): "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

# Output results
print("\n=== Results ===")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
