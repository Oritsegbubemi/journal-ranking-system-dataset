"""
This is the pythonic version of the user dataset jupyter notebook
"""

# In[1]: Import Libraries
import numpy as np
import pandas as pd


# In[2]: Insert CSV file
journal = pd.read_csv('User_Dataset.csv')


# In[3]:
number = len(journal)
columns = journal.columns[2:]


# In[4]: Mean - 4
mean = []
for i in columns:
    mean_criteria = np.mean(journal[i])
    mean.append(mean_criteria)
print("Mean: ", mean)


# In[5]: Variance - 5
variance = []
for i in columns:
    variance_criteria = np.var(journal[i])*number
    variance.append(variance_criteria)
print("Variance: ", variance)


# In[6]: Deviation - 6
deviation = []
for (i, j) in zip(columns, variance):
    deviation_criteria = 1 - j
    deviation.append(deviation_criteria)
print("Deviation: ", deviation)


# In[7]: Finding Overall preference value - 7
preference_value = []
overall = sum(deviation)
for (i, j) in zip(columns, deviation):
    preference_criteria = j/overall
    preference_value.append(preference_criteria)
print("Preference Value: ", preference_value)

sum_ = sum(preference_value)
print("Sum: ", sum_)


# In[8]: Calculating PSI - 8
for (i,j) in zip(columns, preference_value): 
    journal[i] = journal.loc[:, i] * j
    
psi_rank = journal.drop(['scopus_source_id', 'subject_area'], axis=1)
psi = []
for i in range(number):
    psi_sum = sum(psi_rank.loc[i])
    psi.append(psi_sum)

journal['PSI'] = psi

ranked_journal = journal.sort_values('PSI', ascending=False)

ranked_journal.to_csv(r'C:\Users\Gbubemi\Documents\#Project\journal-ranking-system-dataset\dataset_edit_mode\Result_Dataset.csv', index=False)

print("File has been exported")
print("End of the code")
