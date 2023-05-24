def print_upper_words(words, must_start_with):
    """
    1. Given a list of words, 
        for words that start with one of the letters in must_start_with,
        print out each word in all uppercase on a separate line. 
    
    For example: 
    
        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
            # "HELLO"
            # "HEY"
            # "YO"
            # "YES"
    
    
    """
    
    for word in words:
        for letter in must_start_with: 
                if word.lower().startswith(letter.lower()):
                    print(word.upper())
    


# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})