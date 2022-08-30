length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = length * width * height
volume_liters = tank_volume / 1000
occupied_space = percent / 100

total_liters = volume_liters * (1 - occupied_space)

print(total_liters)
