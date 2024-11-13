#V00701756 Morgan Morris
year=0
delta=0
population= 337139390
BIRTH_RATE= 8
DEATH_RATE= 11
IMMIGRATION_RATE = 27
year = int(input("How Many Years: "))
# fill thus section with your code - begin
multiplier = (year * 365 * 24 * 60 *60)
births = multiplier // 8
deaths = multiplier // 11
immigrants = multiplier // 27
delta = births + immigrants - deaths
population = population + delta
# fill this section with your code - end
print(f"New population in {year} years will change by {delta} to be {population}.")
