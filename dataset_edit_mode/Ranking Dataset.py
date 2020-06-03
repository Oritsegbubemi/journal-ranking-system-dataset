"""
This is the pythonic version of the ranking dataset jupyter notebook
"""

# In[1]: Import Libraries
import numpy as np
import pandas as pd


# In[2]: Insert the csv file
journal = pd.read_csv('Ranking Dataset.csv')


# In[3]: Subject Area
def user__switch_subject_area(arg):
    switcher = {
        1: "General Computer Science",
        2: "Computer Science (miscellaneous)",
        3: "Artificial Intelligence",
        4: "Computational Theory and Mathematics",
        5: "Computer Graphics and Computer-Aided Design",
        6: "Computer Networks and Communications",
        7: "Computer Science Applications",
        8: "Computer Vision and Pattern Recognition",
        9: "Hardware and Architecture",
        10: "Human-Computer Interaction",
        11: "Information Systems",
        12: "Signal Processing",
        13: "Software"
    }
    return switcher.get(arg, "You entered an invalid input")

user_subject_area = int(input("Please Enter a number which represent a computer science sub-subject area: "))
subject_area = user__switch_subject_area(user_subject_area)
not_suject_area = journal.loc[journal['subject_area'] != subject_area]
journal=journal.drop(not_suject_area.index, axis=0)


# In[4]: Index
index = dict()
def user_index():
    print("Kindly input rank: \n1 for Scopus journals \n2 for Others")
    dict_index = { 1: "Scopus", 2: "Others" }
    list_index = ["first", "second"]
    rank_index = [1.0, 0.5]
    for (x, y) in zip(list_index, rank_index):   
        user_text_index = "Enter the {} journal index ranking number: ".format(x)
        user_index = int(input(user_text_index))
        for key in dict_index.keys():
            if user_index == key:
                index[dict_index[key]] = y 
            elif user_index not in dict_index.keys():
                return ("Please enter either 1 or 2")
    return index

user_index()
rank_index = journal['index']
for i in rank_index:
    for key in index.keys():
        if (i == key):
            a = rank_index.replace(i,index[key], inplace=True)
            

# In[5]: Publisher
publisher = dict()
def user_publisher():
    print("Kindly input rank: \n1 for Springer \n2 for Elsevier \n3 for IEEE \n4 for Taylor and Francis \n5 for Inderscience\n6 for ACM \n7 for Others")
    dict_publisher = { 1: "Springer", 2: "Elsevier", 3: "IEEE", 4: "Taylor and Francis", 5: "Inderscience", 6: "ACM", 
                      7: "Others" }
    list_publisher = ["first", "second", "third", "forth", "fifth", "sixth", "seventh"]
    rank_publisher = [1.0, 0.85, 0.7, 0.55, 0.4, 0.25, 0.1]
    for (x, y) in zip(list_publisher, rank_publisher):   
        user_text_publisher = "Enter the {} publisher ranking number: ".format(x)
        user_publisher = int(input(user_text_publisher))
        for key in dict_publisher.keys():
            if user_publisher == key:
                publisher[dict_publisher[key]] = y  
            elif user_publisher not in dict_publisher.keys():
                return ("Please enter a number between 1 to 7")
    return publisher
user_publisher()

rank_publisher = journal['publisher']
for i in rank_publisher:
    for key in publisher.keys():
        if (i == key):
            a = rank_publisher.replace(i,publisher[key], inplace=True)


# In[6]: Grouping the Percentile
percent = journal['percentile']
for i in percent:
    if(i>=0 and i<=25):
        a = percent.replace(i, 4, inplace=True)
for i in percent:
    if(i>=25 and i<=49):
        a = percent.replace(i, 3, inplace=True)    
for i in percent:
    if(i>=50 and i<=74):
        a = percent.replace(i, 2, inplace=True)
for i in percent:
    if(i>=75 and i<=99):
        a = percent.replace(i, 1, inplace=True)


# In[7]: Percentile
percentile = dict() 
def user_percentile(): 
    print("Kindly input rank: \n1 for 99 - 75 \n2 for 74 - 50 \n3 for 49 - 25 \n4 for 24 - 0") 
    dict_percentile = { 1: 1, 2: 2, 3: 3, 4: 4} 
    list_percentile = ["first", "second", "third", "forth"] 
    rank_percentile = [1.0, 0.7, 0.5, 0.3]
    for (x, y) in zip(list_percentile, rank_percentile):   
        user_text_percentile = "Enter the {} percentile ranking number: ".format(x)
        user_percentile = int(input(user_text_percentile))
        for key in dict_percentile.keys():
            if user_percentile == key:
                percentile[dict_percentile[key]] = y
            elif user_percentile not in dict_percentile.keys():
                return ("Please enter a number between 1 to 4")
    return percentile

user_percentile()
rank_percentile = journal['percentile']
for i in rank_percentile:
    for key in percentile.keys():
        if (i == key):
            a = rank_percentile.replace(i,percentile[key], inplace=True)


# In[8]: Frequency
frequency = dict()
def user_frequency():
    print("Kindly input rank: \n1 for Monthly \n2 for Bi-monthly \n3 for Quarterly \n4 for Bi-annually \n5 for Annually")
    dict_frequency = { 1: "Monthly", 2: "Bi-monthly", 3: "Quarterly", 4: "Bi-annually", 5: "Annually" }
    list_frequency = ["first", "second", "third", "forth", "fifth"]
    rank_frequency = [1.0, 0.8, 0.6, 0.4, 0.2]
    for (x, y) in zip(list_frequency, rank_frequency):   
        user_text_frequency = "Enter the {} frequency ranking number: ".format(x)
        user_frequency = int(input(user_text_frequency))
        for key in dict_frequency.keys():
            if user_frequency == key:
                frequency[dict_frequency[key]] = y   
            elif user_frequency not in dict_frequency.keys():
                return ("Please enter a number between 1 to 5")
    return frequency

user_frequency()
rank_frequency = journal['frequency']
for i in rank_frequency:
    for key in frequency.keys():
        if (i == key):
            a = rank_frequency.replace(i,frequency[key], inplace=True)


# In[10]: Open Access
open_access = dict()
def user_open_access():
    print("Do you want open access journal input: \n1 for Yes \n2 for No")
    dict_open_access = { 1: "YES", 2: "NO" }
    list_open_access = ["first", "second"]
    rank_open_access = [1.0, 0.5]
    for (x, y) in zip(list_open_access, rank_open_access):   
        user_text_open_access = "Enter the {} open access ranking number: ".format(x)
        user_open_access = int(input(user_text_open_access))
        for key in dict_open_access.keys():
            if user_open_access == key:
                open_access[dict_open_access[key]] = y
            elif user_open_access not in dict_open_access.keys():
                return ("Please enter either 1 or 2")
    return open_access

user_open_access()
rank_open_access = journal['open_access']
for i in rank_open_access:
    for key in open_access.keys():
        if (i == key):
            a = rank_open_access.replace(i,open_access[key], inplace=True)


# In[11]: Review Time
review_time = dict()
def user_review_time():
    print("Kindly input rank: \n1 for 4 weeks \n2 for 6 weeks \n3 for 10 weeks \n4 for 12 weeks \n5 for 18 weeks")
    dict_review_time = { 1: "4 weeks", 2: "6 weeks", 3: "10 weeks", 4: "12 weeks", 5: "18 weeks" }
    list_review_time = ["first", "second", "third", "forth", "fifth"]
    rank_review_time = [1.0, 0.8, 0.6, 0.4, 0.2]
    for (x, y) in zip(list_review_time, rank_review_time):   
        user_text_review_time = "Enter the {} review time ranking number: ".format(x)
        user_review_time = int(input(user_text_review_time))
        for key in dict_review_time.keys():
            if user_review_time == key:
                review_time[dict_review_time[key]] = y
            elif user_review_time not in dict_review_time.keys():
                return ("Please enter a number between 1 to 5")
    return review_time

user_review_time()
rank_review_time = journal['review_time']
for i in rank_review_time:
    for key in review_time.keys():
        if (i == key):
            a = rank_review_time.replace(i,review_time[key], inplace=True)



#Export to csv
journal.to_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-dataset\dataset_edit_mode\User_Dataset.csv', index=False) 
               
print("File has been exported")
print("End of the code")



