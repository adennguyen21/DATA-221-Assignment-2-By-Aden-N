# Question 5 - Creating a new categorical variable and a grouped summary table.
#=======================================================================

import csv

def open_csv_as_list(student_csv_file):
    with open(student_csv_file, "r") as student_information_file:

        student_csv_reader = csv.reader(student_information_file)

        student_information_list = list(student_csv_reader)

    student_information_list.pop(0)

    return student_information_list


def create_new_column_grade_band(student_list):
    grade_band_dictionary = {"Low": [], "Medium": [], "High": []}


    for student in student_list:

        if int(student[0]) <= 9:
            grade_band_dictionary["Low"].append(student)
        elif 10 <= int(student[0]) <= 14:
            grade_band_dictionary["Medium"].append(student)
        elif int(student[0]) >= 15:
            grade_band_dictionary["High"].append(student)

    return grade_band_dictionary


def number_of_students_each_band(grade_band_dictionary):
    student_count_dictionary = {}
    low_list = grade_band_dictionary["Low"]
    medium_list = grade_band_dictionary["Medium"]
    high_list = grade_band_dictionary["High"]

    student_count_dictionary["Low"] = len(low_list)
    student_count_dictionary["Medium"] = len(medium_list)
    student_count_dictionary["High"] = len(high_list)

    return student_count_dictionary


def calculate_average_absences_each_band(grade_band_dictionary):
    absences_dictionary = {}
    low_list = grade_band_dictionary["Low"]
    medium_list = grade_band_dictionary["Medium"]
    high_list = grade_band_dictionary["High"]

    absence_summation = 0
    for absence in low_list:
        absence_summation += int(absence[1])
        absence_average = absence_summation / len(low_list)
        absences_dictionary["Low"] = absence_average

    absence_summation = 0
    absence_average = 0

    for absence in medium_list:
        absence_summation += int(absence[1])
        absence_average = absence_summation / len(medium_list)
        absences_dictionary["Medium"] = absence_average

    absence_summation = 0
    absence_average = 0

    for absence in high_list:
        absence_summation += int(absence[1])
        absence_average = absence_summation / len(high_list)
        absences_dictionary["High"] = absence_average

    return absences_dictionary


def calculate_percentage_internet_access_each_band(grade_band_dictionary):
    low_list = grade_band_dictionary["Low"]
    medium_list = grade_band_dictionary["Medium"]
    high_list = grade_band_dictionary["High"]
    internet_access_dictionary = {}

    internet_counter = 0
    for internet_access in low_list:
        if int(internet_access[3]) == 1:
            internet_counter += 1
    percentage_internet_access = internet_counter / len(low_list) * 100
    internet_access_dictionary["Low"] = percentage_internet_access

    internet_counter = 0
    percentage_internet_access = 0

    for internet_access in medium_list:
        if int(internet_access[3]) == 1:
            internet_counter += 1
    percentage_internet_access = internet_counter / len(medium_list) * 100
    internet_access_dictionary["Medium"] = percentage_internet_access

    internet_counter = 0
    percentage_internet_access = 0

    for internet_access in high_list:
        if int(internet_access[3]) == 1:
            internet_counter += 1
    percentage_internet_access = internet_counter / len(high_list) * 100
    internet_access_dictionary["High"] = percentage_internet_access

    return internet_access_dictionary


def combine_all_into_list(student_counts, absence_averages, internet_access_percentages):
    finished_grade_band_list = []

    final_low_list = ["Low", student_counts["Low"], absence_averages["Low"], internet_access_percentages["Low"]]
    final_medium_list = ["Medium", student_counts["Medium"], absence_averages["Medium"], internet_access_percentages["Medium"]]
    final_high_list = ["High", student_counts["High"], absence_averages["High"], internet_access_percentages["High"]]

    finished_grade_band_list.append(final_low_list)
    finished_grade_band_list.append(final_medium_list)
    finished_grade_band_list.append(final_high_list)

    return finished_grade_band_list


def create_student_bands_csv(final_grade_band_list):
    with open("student_bands.csv", "w", newline="") as student_bands_file:
        student_bands_writer = csv.writer(student_bands_file)
        student_bands_writer.writerow(["grade_band", "number_of_students", "average_absences", "percentage_with_internet"])
        student_bands_writer.writerows(final_grade_band_list)
    student_bands_file.close()

#======================================================================
def main():
    student_information_file = open_csv_as_list("student.csv")

    grade_band_dictionary = create_new_column_grade_band(student_information_file)

    student_counts = number_of_students_each_band(grade_band_dictionary)

    average_averages = calculate_average_absences_each_band(grade_band_dictionary)

    internet_access_percentages = calculate_percentage_internet_access_each_band(grade_band_dictionary)

    finalized_list = combine_all_into_list(student_counts, average_averages, internet_access_percentages)

    create_student_bands_csv(finalized_list)

main()
