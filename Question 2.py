# Question 2 - Reading and processing bigrams:
# ======================================================================

def open_and_read_file(file_name): # Opens and reads the file, returning the contents as a list.
    file_handler = open(file_name, "r")
    return file_handler.readlines()


def split_file_into_tokens(file_list): # Splits the contents of the file into individual words, which are then put into another list.
    word_list = []
    unfinished_word = " "

    for line in file_list:
        for letter in line:
            if letter in [" ", "\n", ".", ",", "!", "?"]: # Stops connecting letters when it detects whitespace, "/n", or punctuation. (This forms the individual words)
                word_list.append(unfinished_word) # Appends the word to word_list.
                unfinished_word = " "
            else:
                unfinished_word = unfinished_word + letter # Connects letters to form words, until the if-condition is true.

    return word_list


def convert_and_clean_tokens(unfinished_word_list): # Converts all the words into lowercase, removes whitespaces, and filters out words that contain less than 2 letters.
    finished_word_list = []

    for i in range(len(unfinished_word_list)): # Removes whitespaces next to words, and converts them to lowercase.
        unfinished_word_list[i] = unfinished_word_list[i].strip().lower()

    while "" in unfinished_word_list: # Removes any empty elements from the list.
        unfinished_word_list.remove("")

    for word in unfinished_word_list: # Filters out any words that are less than 2 letters in length.
        if len(word) >= 2:
          finished_word_list.append(word) # Appends the cleaned up word into a list.

    return finished_word_list


def construct_bigrams(word_list): #
    bigram_list = []
    for i in range(len(word_list) - 1):
        bigram_list.append((word_list[i], word_list[i + 1]))

    return bigram_list

def calculate_bigram_frequency(bigram_list):
    bigram_frequencies_dictionary = {}
    for bigram in bigram_list:
        bigram_count = 0

        for comparing_bigram in bigram_list:
            if bigram == comparing_bigram:
                bigram_count += 1

        bigram_frequencies_dictionary[bigram] = bigram_count

    sorted_bigram_frequencies = dict(sorted(bigram_frequencies_dictionary.items(), key=lambda item: item[1], reverse=True))

    return sorted_bigram_frequencies

def print_top_5_most_frequent_bigrams(bigram_frequencies): # Prints out the top ten most frequent words.
    top_5_count = 0 # Once this count reaches 10, this function stops printing.

    for item in bigram_frequencies.items(): # Goes through each element in the frequencies' library.
        if top_5_count < 5:
            bigram, frequency = item # Separates the word (key) and frequency number (value) as two different variables.
            print(f"{bigram[0] + " " + bigram[1]} -> {frequency}") # Prints out the result.
            top_5_count += 1

        else:
            break

# =================================================================================

def main(): # Main function to call the other functions in.
    text_file = "sample-file.txt"

    unfinished_file_list = open_and_read_file(text_file)

    unfinished_word_list = split_file_into_tokens(unfinished_file_list)

    finished_word_list = convert_and_clean_tokens(unfinished_word_list)

    bigram_list = construct_bigrams(finished_word_list)

    bigram_frequency_dictionary = calculate_bigram_frequency(bigram_list)

    print_top_5_most_frequent_bigrams(bigram_frequency_dictionary)

main()