pen_count = int(input())
markers_count = int(input())
detergent_count = int(input())
discount = int(input())

pen_price = 5.80
markers_price = 7.20
detergent_price = 1.20

total_pen_price = pen_count * pen_price
total_markers_price = markers_count * markers_price
total_detergent_price = detergent_count * detergent_price
total_price = total_pen_price + total_markers_price + total_detergent_price
total_disc_price = total_price - (total_price * (discount / 100))

print(total_disc_price)
