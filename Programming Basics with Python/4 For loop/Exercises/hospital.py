period = int(input())

treated = 0
untreated = 0
doctors = 7

for i in range(1, period + 1):
    patients = int(input())
    if i % 3 == 0:
        if untreated > doctors:
            doctors = doctors + 1

    if patients <= doctors:
        treated = treated + patients
    elif patients > doctors:
        diff = patients - doctors
        untreated = untreated + diff
        treated = treated + doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
