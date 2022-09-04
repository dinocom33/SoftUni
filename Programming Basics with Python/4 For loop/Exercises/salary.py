tabs_count = int(input())
salary = int(input())

copy_salary = salary

for i in range(1, tabs_count + 1):
    website_name = input()
    if website_name == "Facebook":
        copy_salary = copy_salary - 150
    elif website_name == "Instagram":
        copy_salary = copy_salary - 100
    elif website_name == "Reddit":
        copy_salary = copy_salary - 50

    if copy_salary <= 0:
        break

if copy_salary <= 0:
    print("You have lost your salary.")
else:
    print(copy_salary)
