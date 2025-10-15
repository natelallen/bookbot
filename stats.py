# count total number of words in the book
def count_words(book):
    return len(book.split())

# get a list of unique characters in the book and their counts. adds them to a dictionary. counts are case insensitive but displays only uppercase.
def char_count(book):
    counts = {}
    for ch in book.lower():
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts
            
# helper function of sort_char_count to sort the list
def sort_key_helper(counts):
    return counts["num"]


# calls counts dictionary, creates new list (sorted), loop statement to iterate through counts dictionary,  creates new dictionary for each character and its count, appends to sorted list. 
# sorts list by count in descending order, returns sorted list.
def sort_char_count(counts):
    sorted = []
    for key in counts:
        new_dict = {"char": key, "num": counts[key]}
        sorted.append(new_dict)
    sorted.sort(key=sort_key_helper, reverse=True)
    return sorted



