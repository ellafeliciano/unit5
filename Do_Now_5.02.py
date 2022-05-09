'''
############
Do Now 5.02
############

1. In your Console
------------------
Type the following:

my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'p. cute'
print(my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what the 2nd line does.
the 2nd line defines kittens as p. cute

2. In your Console
------------------
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print(my_dictionary)

Continue in your Notebook
-------------------------
Respond to the following prompt
Write down what the 2nd line does.
it adds puppies: baby dogs to the dictionary

3. In your Console
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}
​
my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)
Continue In your Notebook
Write down what the second line does.
we get an error because there is no key called bunnies

What is different between my_dictionary.pop('bunnies') and my_dictionary.pop('bunnies', None)?
pop bunnies would remove it from the dictionary
pop bunnies none would return nothing if it doesnt exist
'''