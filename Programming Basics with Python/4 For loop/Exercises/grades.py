students_count = int(input())

fail_student = 0
between_3_399 = 0
between_4_499 = 0
top_students = 0
avg_grade = 0

for i in range(1, students_count + 1):
    grade = float(input())
    if grade <= 2.99:
        fail_student = fail_student + 1
    elif grade <= 3.99:
        between_3_399 = between_3_399 + 1
    elif grade <= 4.99:
        between_4_499 = between_4_499 + 1
    elif grade >= 5:
        top_students = top_students + 1
    avg_grade = avg_grade + grade

top_students_percent = top_students / students_count * 100
between_3_399_percent = between_3_399 / students_count * 100
between_4_499_percent = between_4_499 / students_count * 100
fail_student_percent = fail_student / students_count * 100
avg_grade = avg_grade / students_count

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_499_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_399_percent:.2f}%")
print(f"Fail: {fail_student_percent:.2f}%")
print(f"Average: {avg_grade:.2f}")