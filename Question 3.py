# Question 3 - Identifying nearly identical lines.
#======================================================================

def open_and_read_file(file_name):
    # Opens and reads the file, returning the contents as a list.
    line_list = []

    with open(file_name, "r") as line_file:
        for line_number, line in enumerate(line_file, start=1): # Puts a index for each line.
            stripped_line = line.strip()
            if stripped_line != "": # Filters any empty lines.
                line_list.append((line_number, stripped_line))

    return line_list


def clean_lines(line):
    # Cleans the line so that it's lowercase and there is no whitespaces or punctuation.
    clean_line = ""
    for letter in line:
        if letter.isalnum():  # Keep only letters and numbers
            clean_line += letter.lower() # Lowercase

    return clean_line


def group_near_duplicates(line_list):
    # Puts the clean line as a key with its values as the line number and original line.
    # Also groups together near duplicate lines in a list.
    near_duplicates_dictionary= {}

    for line_number, line in line_list:
        key = clean_lines(line)

        if key not in near_duplicates_dictionary:
            near_duplicates_dictionary[key] = []

        near_duplicates_dictionary[key].append((line_number, line))

    return near_duplicates_dictionary


def find_duplicate_lines(near_duplicates_dictionary):
    # Finds the groups that have two or more lines that are duplicates of each other.
    near_duplicate_lines = []

    for group in near_duplicates_dictionary.values():
        if len(group) > 1:
            near_duplicate_lines.append(group)

    return near_duplicate_lines # Final list with all the duplicate sets.


def print_duplicate_sets(near_duplicate_sets):
    # Prints out number of near-duplicate sets, and the first two duplicating sets.
    print(f"Number of near-duplicate sets: {len(near_duplicate_sets)}")
    print()

    for set_number, duplicate_lines in enumerate(near_duplicate_sets[:2], start=1):
        print(f"Set {set_number}:")
        for line_number, line in duplicate_lines:
            print(f"line {line_number}: {line}")
        print()

# ====================================================================================

def main():
    text_file = "sample-file.txt"

    file_list = open_and_read_file(text_file)

    near_duplicates_groups = group_near_duplicates(file_list)

    near_duplicate_sets = find_duplicate_lines(near_duplicates_groups)

    print_duplicate_sets(near_duplicate_sets)


main()

