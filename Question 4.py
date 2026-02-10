# Question 4 - Filtering tabular data and saving the results to a new file.
#==============================================================================

import pandas as pd
import csv


def convert_csv_as_dataframe(student_file):
    student_dataframe = pd.read_csv(student_file)

    return student_dataframe


def filter_high_engagement_students(student_dataframe):
    high_engagement_list = []

    for row in student_dataframe.itertuples():
        if row[3] >= 3 and row[4] ==1 and row[2] <= 5:
            high_engagement_list.append(list(row))

    return high_engagement_list


def create_high_engagement_csv(high_engagement_list):
    with open("high_engagement.csv", "w", newline = "") as high_engagement_file:
        high_engagement_writer = csv.writer(high_engagement_file)
        high_engagement_writer.writerow(["Student index", "Grade", "Absences", "Study time", "Internet", "Activities"])
        high_engagement_writer.writerows(high_engagement_list)
    high_engagement_file.close()


def calculate_high_engagement_average_grade(high_engagement_list):
    summation_of_grades = 0
    for student_info in high_engagement_list:
        summation_of_grades += student_info[1]

    average_grade = summation_of_grades / len(high_engagement_list)

    return average_grade


def print_information_of_high_engagement_students(high_engagement_list, average_grade):
    print("Number of high engagement students:", len(high_engagement_list))
    print(f"Average grade of the high engagement students: {average_grade}%")


def main():
    with open("student.csv","r") as student_information_file:

        student_dataframe = convert_csv_as_dataframe(student_information_file)

        filtered_high_engagement_list = filter_high_engagement_students(student_dataframe)

        create_high_engagement_csv(filtered_high_engagement_list)

        high_engagement_average_grade = calculate_high_engagement_average_grade(filtered_high_engagement_list)

        print_information_of_high_engagement_students(filtered_high_engagement_list, high_engagement_average_grade)

main()