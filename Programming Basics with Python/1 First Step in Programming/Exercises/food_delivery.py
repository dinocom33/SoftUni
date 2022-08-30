chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
veg_menu_price = veg_menu * 8.15
delivery_price = 2.50
desert_price = (chicken_menu_price + fish_menu_price + veg_menu_price) * 0.20

total_sum = chicken_menu_price + fish_menu_price + veg_menu_price + delivery_price + desert_price
print(total_sum)
