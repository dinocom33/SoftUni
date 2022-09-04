stadium_capacity = int(input())
fens_count = int(input())

fens_sector_a = 0
fens_sector_b = 0
fens_sector_v = 0
fens_sector_g = 0

for i in range(1, fens_count + 1):
    sector = input()
    if sector == "A":
        fens_sector_a = fens_sector_a + 1
    elif sector == "B":
        fens_sector_b = fens_sector_b + 1
    elif sector == "V":
        fens_sector_v = fens_sector_v + 1
    elif sector == "G":
        fens_sector_g = fens_sector_g + 1

fens_sector_a_percent = fens_sector_a / fens_count * 100
fens_sector_b_percent = fens_sector_b / fens_count * 100
fens_sector_v_percent = fens_sector_v / fens_count * 100
fens_sector_g_percent = fens_sector_g / fens_count * 100
total_fens_percent = fens_count / stadium_capacity * 100

print(f"{fens_sector_a_percent:.2f}%")
print(f"{fens_sector_b_percent:.2f}%")
print(f"{fens_sector_v_percent:.2f}%")
print(f"{fens_sector_g_percent:.2f}%")
print(f"{total_fens_percent:.2f}%")
