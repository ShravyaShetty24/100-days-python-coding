#dictionary comprehension
#find the length of the names
names={"shravya","sanvi","khushi"}
d={name:len(name) for name in names}
print(d)
#find the largest cities population should be greater than 10
common_population={"Banglore":84,"mysuru":11,"Hubballi":9,"mangaluru":5}
largest_cities={city:population for city,population in common_population.items() if population>10}
print(largest_cities)
