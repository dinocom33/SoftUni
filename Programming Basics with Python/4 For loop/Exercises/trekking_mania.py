groups_count = int(input())

musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_people = 0

for i in range(1, groups_count + 1):
    people_count = int(input())
    total_people = total_people + people_count

    if people_count <= 5:
        musala_count = musala_count + people_count
    elif people_count <= 12:
        montblanc_count = montblanc_count + people_count
    elif people_count <= 25:
        kilimanjaro_count = kilimanjaro_count + people_count
    elif people_count <= 40:
        k2_count = k2_count + people_count
    else:
        everest_count = everest_count + people_count

musala_percentage = musala_count / total_people * 100
montblanc_percentage = montblanc_count / total_people * 100
kilimanjaro_percentage = kilimanjaro_count / total_people * 100
k2_percentage = k2_count / total_people * 100
everest_percentage = everest_count / total_people * 100

print(f"{musala_percentage:.2f}%")
print(f"{montblanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
