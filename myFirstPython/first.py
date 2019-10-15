result = 1

mylist = list(range(0, 3))
print(f'Number of iterations {mylist}')

for i in mylist:
    print(f'Result before calculation {result}')
    result = result * 5
    print(f'Result after calculation {result}')


print(result)
