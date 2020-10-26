from main import*

min_temp = min_max_value()[0]
max_temp = min_max_value()[1]
print("min_temp=", min_temp)
print("max_temp=", max_temp)
plot_average_temp()
plot_average_temp_through_years()
sr_temp = average_temp_through_years()[0]
odch_sta = average_temp_through_years()[1]
print("Srednia temperatura dla poszczególnych miesięcy: ", sr_temp)
print("Odchylenie standardowe: ", odch_sta)


