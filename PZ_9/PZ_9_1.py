# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных стран.
# Определить какие марки машин были доставлены во все указанные страны, какие в некоторые из стран и какие не доставлены ни в одну страну.

marks = {'Lada', 'BMW', 'Toyota', 'Porsche', 'Lexus', 'Opel', 'Renault', 'Audi'}
country_1 = {'Lada', 'BMW', 'Toyota'}
country_2 = {'BMW', 'Porsche', 'Opel'}
country_3 = {'Lexus', 'BMW', 'Audi'}

all_countries = marks & country_1 & country_2 & country_3
some_countries = (country_1 | country_2 | country_3) - all_countries
none_countries = marks - (country_1 | country_2 | country_3)

print("Марки машин, доставленные во все страны:")
print(all_countries)
print("Марки машин, доставленные в некоторые страны:")
print(some_countries)
print("Марки машин, не доставленные ни в одну страну:")
print(none_countries)