# main.py
# BookBot: A simple book analysis tool

# import sys module to handle command-line arguments
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# function to read the book file and return its content as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


# main function to orchestrate the analysis
def main():

# import count_words function from stats.py, get book text from command-line argument, call function, store result in variable
    from stats import count_words
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)

# import char_count function from stats.py, call function, store result in variable
    from stats import char_count
    char_counts = char_count(book)

# print results
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count --------")

# import sort_char_count function from stats.py, call function, store result in variable, loop through sorted list and print each character and its count
    from stats import sort_char_count
    sorted_counts = sort_char_count(char_counts)
    for sorted in sorted_counts:
        if sorted["char"].isalpha():  # only print letters
            print(f"{sorted["char"]}: {sorted["num"]}")
    print("============= END ===============")
    

main()