visochina_house = float(input())
daljina_house = float(input())
vis_triagalna_stena_pokriv = float(input())

kvadratura_stena = (visochina_house * daljina_house) - 2.25
total_kvadratura_steni = kvadratura_stena * 2

zadna_stena_kvadratura = visochina_house * visochina_house
total_zadna_stena_kvadratura = (zadna_stena_kvadratura * 2) - 2.4

total_kvadratura = total_kvadratura_steni + total_zadna_stena_kvadratura

pokriv_prav_kvadratura = (visochina_house * daljina_house) * 2
pokriv_triag_kvadratura = (visochina_house * (vis_triagalna_stena_pokriv / 2) * 2)
total_pokriv_kvadratura = pokriv_prav_kvadratura + pokriv_triag_kvadratura

green_paint = total_kvadratura / 3.4
print(f"{green_paint:.2f}")
red_paint = total_pokriv_kvadratura / 4.3
print(f"{red_paint:.2f}")