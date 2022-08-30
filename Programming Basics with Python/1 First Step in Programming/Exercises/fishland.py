skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = skumria_price * 1.6
total_palamud_price = palamud_price * palamud_kg

safrid_price = caca_price * 1.8
total_safrid_price = safrid_price * safrid_kg

midi_price = 7.50
total_midi_price = midi_price * midi_kg

total_sum = total_safrid_price + total_midi_price + total_palamud_price
print(f"{total_sum:.2f}")