'''
############
# Lab 5.04 #
############
In this lab we will use our word-counting code from Lab 6.02 to create a program that 
determines the top 5 most commonly used words in a passage of text. After processing 
the passage, it prints the top 5 words and the number of times each occurs.

Here's one strategy for completing this lab:

Repackage some of your code from Lab 6.02 to make two functions: 
text_to_word_list(), that  takes a single passage of text and splits into a list of words; 
and count_frequencies(), that takes in a list of words and returns a dictionary of word 
frequencies

Write a new function, find_max_valued_key(), that takes a dictionary as an argument, and 
returns the key that is associated with the largest value in that dictionary. Internally, 
this function loops through the dictionary while keeping track of the largest value it's 
seen so far and the key that goes along with that value.

Run find_max_valued_key() once on the dictionary of word counts, print out the key/value 
of word it returns.

Remove that key from the dictionary.

Repeat steps 3-4 four more times: Call find_max_valued_key(), print out the key/value pair, 
and remove the key.

If there is a tie within find_max_valued_key(), choose among the tied items however you like 
and return just one of them.

Example
--------
Here's an example of the program output with the text passage set to the opening lines of Dr. 
Seuss's poem Green Eggs and Ham:

I am Sam. I am Sam. Sam-I-am.

That Sam-I-am! That Sam-I-am!
I do not like that Sam-I-am!

Would you like green eggs and ham?

I do not like them, Sam-I-am.
I do not like green eggs and ham.

Would you like them here or there?

I would not like them here or there.
I would not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.

Would you like them in a house?
Would you like them with a mouse?

I do not like them in a house.
I do not like them with a mouse.
I do not like them here or there.
I do not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.
>>> python3 most_frequent_words.py
i, 22
like, 17
not, 13
do, 11
them, 12

Bonus
----------
The process of finding the largest element, printing it, and removing it from the dictionary 
is a way to sort items. Write a function that will return a sorted list of all the words from 
most frequent to least frequent.

Change the code to find the least frequent words.
'''

# passage
example_paragraph = """ It was a beautiful day in New York City. Our hero Ariana Grande was on a walk 
from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in 
New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided 
to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande 
decides to go to Times Square instead. What a beautiful day in New York."""

# functions
def text_to_word_list(passage):
    passage_lower = passage.lower()
    passage_lower_no_punctuation = passage_lower.replace(".", "")
    passage_lower_no_punctuation = passage_lower.replace(",", "")
    passage_lower_no_punctuation = passage_lower.replace("?", "")
    passage_lower_no_punctuation = passage_lower.replace("!", "")
    passage_word_list = passage_lower_no_punctuation.split(" ")
    return(passage_word_list)

def count_frequencies(list_of_words):
    word_count = {}
    for word in list_of_words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return(word_count)

my_dict = count_frequencies(text_to_word_list(example_paragraph))


new_dict = []
for i in range(5):
    max_value = 0
    max_key = ""
    for key in my_dict:
        if my_dict[key] > max_value:
            max_value = my_dict[key]
            max_key = key
    print(max_key, my_dict[max_key])
    del my_dict[max_key]