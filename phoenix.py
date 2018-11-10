import csv


def get_complaints():
    complaint_list = []
    with open('propertymaintenance.csv', encoding='utf8') as complaints:
        csv_reader = csv.reader(complaints)

        for row in csv_reader:
            # 5 is the index of the comment in the report for each row
            complaint_list.append(row[5])

    return complaint_list
