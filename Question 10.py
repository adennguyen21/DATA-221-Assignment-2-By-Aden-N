# Question 10 - Reusable function for searching within text files.
#=================================================================================

def find_lines_containing(filename, keyword):
    # Opens the file, and finds lines containing the given keyword.
    matching_results = []

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                # Compares the lowercase version of the keyword, to the lowercase version to the line.
                matching_results.append((line_number, line.strip()))

    return matching_results

def print_matching_results(matching_lines):
    # Prints the results of matching lines to the keyword.
    print(f"Number of matching lines: {len(matching_lines)}")
    print()

    if matching_lines == []: # If there's no matching lines
        print("No matching lines found.")

    else:
        print("First 3 matching lines:")
        for line_number, line in matching_lines[:3]:
            print(f"Line {line_number}: {line}")

# ============================================================================

def main():
    test_file = "sample-file.txt"
    test_keyword = ("lorem")

    matching_lines = find_lines_containing(test_file, test_keyword)

    print_matching_results(matching_lines)

main()
