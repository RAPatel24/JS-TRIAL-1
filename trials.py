"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

#output_all_items([1, 'hello', True])

def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

#print(get_all_evens([7, 8, 10, 1, 2, 2]))

def get_odd_indices(items):
    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    
    return result

#print(get_odd_indices([1, 'hello', True, 500]))


def print_as_numbered_list(items):
   i = 1

   for item in items:
        print(f'{i}. {item}')
        i += 1

#print_as_numbered_list([1, 'hello', True])

def get_range(start, stop):
    nums = []
    num = start
    while num < stop:
        nums.append(num)
        num += 1
    
    return nums

#print(get_range(0, 5))  

def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else: 
            chars.append(letter)
    
    return ''.join(chars)

#print(censor_vowels('hello world'))

def snake_to_camel(string):
    camel_case = []

    for word in string.split("_"):
        #camel_case.append(word.capitalize())
        camel_case.append(f"{word[0].upper()}{word[1:]}")

    return "".join(camel_case)

#print(snake_to_camel('hello_world'))

def longest_word_length(words):
    longest = len(words[0])
    
    for word in words:
        if len(word) > longest:
            longest = len(word)
    
    return longest

#print(longest_word_length(['jellyfish', 'zebra','ruchipatel']))

def truncate(string):
    result = []

    for char in string:
        if not result or char != result[-1]:
            result.append(char)
    
    return "".join(result)

#print(truncate('aaaabbbbcccca'))


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        
            if parens < 0:
                return False

    return parens == 0
#print(has_balanced_parens('(Oh no!)('))

def compress(string):
    compressed = []

    current_char = ""
    char_count = 0
    for char in string:
        if char != current_char:
            compressed.append(current_char)

            if char_count > 1:
                compressed.append(str(char_count))
            
            current_char = char
            char_count = 0
        
        char_count += 1
    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))
    
    return "".join(compressed)

#print(compress("'Hello, world! Cows go moooo...'"))

def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
      Since "bagon" ends with n, find the *first* word starting
      with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
      been used, it can't be used again --- so we'll never get to
      use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
      Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Get first word and remove from consideration; add it to our output
    output = [names.pop(0)]

    first_letter_to_words = {}

    # Make a dictionary of {first-letter: [words-starting-with-that-letter]}
    # Note that we could also use .setdefault here
    for name in names:

        if name[0] not in first_letter_to_words:
            first_letter_to_words[name[0]] = [name]

        else:
            first_letter_to_words[name[0]].append(name)

    # Chain together words until we run out
    while True:

        # Our starting letter will be the last letter of last word
        start_letter = output[-1][-1]

        # If there are no candidate words, we're done
        if not first_letter_to_words.get(start_letter):
            break

        # Get the first word with that letter and remove it
        word = first_letter_to_words[start_letter].pop(0)
        output.append(word)

    return output
print(kids_game(["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "booger"]))