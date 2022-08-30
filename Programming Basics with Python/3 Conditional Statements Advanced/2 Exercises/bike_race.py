juniors_count = int(input())
seniors_count = int(input())
track_type = input()

tax_junior = 0
tax_senior = 0
total_sum = 0
expenses_sum = 0
donation_sum = 0

if track_type == "trail":
    tax_junior = 5.50
    tax_senior = 7
    total_sum = (juniors_count * tax_junior) + (seniors_count * tax_senior)
    expenses_sum = total_sum * 0.05
    donation_sum = total_sum * 0.95
elif track_type == "cross-country":
    if juniors_count + seniors_count >= 50:
        tax_junior = 8 * 0.75
        tax_senior = 9.50 * .75
        total_sum = (juniors_count * tax_junior) + (seniors_count * tax_senior)
        expenses_sum = total_sum * 0.05
        donation_sum = total_sum * 0.95
    else:
        tax_junior = 8
        tax_senior = 9.50
        total_sum = (juniors_count * tax_junior) + (seniors_count * tax_senior)
        expenses_sum = total_sum * 0.05
        donation_sum = total_sum * 0.95
elif track_type == "downhill":
    tax_junior = 12.25
    tax_senior = 13.75
    total_sum = (juniors_count * tax_junior) + (seniors_count * tax_senior)
    expenses_sum = total_sum * 0.05
    donation_sum = total_sum * 0.95
elif track_type == "road":
    tax_junior = 20
    tax_senior = 21.50
    total_sum = (juniors_count * tax_junior) + (seniors_count * tax_senior)
    expenses_sum = total_sum * 0.05
    donation_sum = total_sum * 0.95

print(f"{donation_sum:.2f}")