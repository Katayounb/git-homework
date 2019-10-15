salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = list(salsa)      # <-- makes a *copy* of the list
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_salsa)
print('-----')
date = "Monday 4 January 2016"
day = date[0:6]
print("Using 0 to begin range:", day)
day = date[:6]
print("Omitting beginning index:", day)
print('-----')
