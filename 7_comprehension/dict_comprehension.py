'''
 syntax for dict comprehension
 new_dict = {new_key:new_value for item in list}
 new_dict = {new_key:new_value for (key,value) in dict.items()}

'''
import random 


names = ["Alex","Beth","caroline","Dave","Elanor","Freddie"]

student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
passed_studemts = {student:score for (student,score) in student_scores.items() if score >= 60 }
# print(passed_studemts)


# ITERATE OVER PANDA DATAFRAME
student_dict = {
    "student": ["Angela","James","Lily"],
    "score":[56,78,89]
}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows in data frame 

for (index,row ) in student_data_frame.iterrows():
    # print(index)
    print(row.student)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}