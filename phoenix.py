import csv
import numpy as np
import keras
from keras.utils import np_utils

#function definitions
def get_complaints():
	complaint_list = []
	with open('propertymaintenance.csv', encoding='utf8') as complaints:
		csv_reader = csv.reader(complaints)

		for row in csv_reader:
            # 5 is the index of the comment in the report for each row
			ree = ""
			if(row[5].strip() != ""):
				ree = row[5].lower()
				complaint_list.append(ree)
			
			#optional trimming and length shortening
			#ree = row[5].replace(" ", "")
			#if(len(ree) > 100):
			#	ree = ree[0:100]
			#print(ree)
			

	return complaint_list

#program begins
dataX = []
dataY = []

c_list = get_complaints()
chars = sorted(list(set("".join(c_list))))
char_to_int = dict((c, i) for i, c in enumerate(chars))
print(char_to_int)
longest = 0
for complaint in c_list:
	if(len(complaint) > longest):
		longest = len(complaint)
	dataX.append([char_to_int[char] for char in complaint])
	dataY.append(complaint[-1])

for index in dataX:
	#pad string with spaces
	str(index).ljust(longest)

n_patterns = len(dataX)
X = np.reshape(dataX, (n_patterns, longest, 1))
X = X/float(len(chars))
y = np_utils.to_categorical(dataY)