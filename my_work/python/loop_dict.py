#!/usr/bin/python3
breakfast = {
    'drink': 'milk',
    'eat': 'nuts'
}

#print only key in the list
for key in breakfast:
    print(key)
#print only value in the 
for value in breakfast:
    print(breakfast[value])

# It is mandatory to use the keyword items in the 
for key,value in breakfast.items():
    print(f'breakfast rule is {key} the {value}')