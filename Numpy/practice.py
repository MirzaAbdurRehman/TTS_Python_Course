
import numpy as np

arr = np.array([
    [123456, 234567, 345678, 456789, 567890, 678901, 789012],
    [890123, 901234, 112345, 223456, 334567, 445678, 556789],
    [667890, 778901, 889012, 990123, 101234, 212345, 323456],
    [434567, 545678, 656789, 767890, 878901, 989012, 109123],
    [210234, 321345, 432456, 543567, 654678, 765789, 876890],
    [345678, 456789, 567890, 678901, 789012, 890123, 901234],
    [567890, 678901, 789012, 890123, 901234, 112345, 223456]
])


year_arr = np.array([1951,2013,2000,2021,1980,2007,20016])


cities = np.array([
    "Karachi",
    "Lahore",
    "Islamabad",
    "Rawalpindi",
    "Faisalabad",
    "Multan",
    "Peshawar",
])


total_per_year = arr.sum(axis=0)
print('Total Population per year wise')
print(total_per_year)


avg_population = arr.mean(axis=1)
for i, city in enumerate(cities):
    print(f"{city}: {avg_population[i]:,.0f}")
