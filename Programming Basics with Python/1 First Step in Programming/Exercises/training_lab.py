w = float(input())
h = float(input())

real_h = (h * 100) - 100
desk_per_h = real_h // 70
broi_redove = (w * 100) // 120
broi_mesta = (desk_per_h * broi_redove) - 3
print(int(broi_mesta))