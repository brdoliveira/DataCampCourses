# wrong
pop = [30.55,2.77,39.21]
countries = ["afghanistan","albania","algeria"]
ind_alb = countries.index("albania")
print(f'population = {pop[ind_alb]}')

# correct
world = {"afghanistan":30.55,
"albania":2.77,
"algeria":39.21}

print(f'population = {world["albania"]}')