import csv


def get_complaints():
    complaint_list = []
    complaintstr = ""
    with open('propertymaintenance.csv', encoding='utf8') as complaints:
        csv_reader = csv.reader(complaints)

        i = 0
        for row in csv_reader:
            # 5 is the index of the comment in the report for each row
            complaintstr += row[5] + str(" ")
            if i > 50:
                break
            i += 1
            # complaint_list.append(row[5])

    with open('bigstring.txt', "w", encoding='utf8') as writefile:
        writefile.write(complaintstr)


get_complaints()