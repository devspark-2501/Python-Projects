import numpy as np

marks = np.array([
    [85, 90, 78, 92],
    [88, 85, 80, 87],
    [90, 92, 85, 90],
    [82, 88, 76, 85],
    [85, 80, 82, 88]
])

total_marks = marks.sum(axis=1)
average_marks = marks.mean(axis=1)

for i in range(len(marks)):
    print(f"Student{i + 1}: Total Marks = {total_marks[i]}, Average Marks = {average_marks[i]}")


topper_index = np.argmax(total_marks)
lowest_index = np.argmin(total_marks)

print(f"\nTopper: Student{topper_index + 1} with Total Marks = {total_marks[topper_index]}")
print(f"Lowest Scorer: Student{lowest_index + 1} with Total Marks = {total_marks[lowest_index]}")


above_80 = np.sum(total_marks > 80)
print(f"\nNumber of students scoring above 80: {above_80}")


