#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary modules
import os
import csv

# set up a dictionary 
candidates = {}


# In[2]:


# make a path to port in the csv
cpath = os.path.join('..', 'Resources', 'election_data.csv')


# In[3]:


# open the csv
with open(cpath) as polls:
    reader = csv.reader(polls, delimiter = ',')
    next(reader, None)
    for row in reader:
        # make the dictionary to hold the candidate names as keys and increment their values
        # this is done with conditionals by checking the column where candidate names are listed
        if row[2] in candidates:
            # increase candidate vote here if they match 
            candidates[row[2]] = int(candidates[row[2]]) + 1
        else:
            # if different, then make a new row
            candidates[row[2]] = 1
# print(candidates) test here to make sure the results are as desired. Do not run again as it will skew the values. Restart instead.


# In[4]:


# use the dictionary to compute and find the values

vals = list(candidates.values()) # function to extract all the values from their keys
total_val = sum(vals) # add them up
names = list(candidates.keys()) # get the names and convert them into a list
winner = max(candidates,key=candidates.get) # used the max function to find the highest pair
percent = [] # set up as a list to be able to fill in a loop
i = 0
while i < len(vals):
    calc = vals[i]/total_val # calculation 
    formating = "{:.3%}".format(calc) # use format to write in the % value and symbol
    # https://www.kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python
    percent.append(formating) # add to the list
    i += 1 # increment to make sure loop closes


# In[5]:


# print results to the terminal    
print("Election Results\n-------------------------")
print(f"Total Votes: {total_val}")
print(f"{names[0]}: {percent[0]} ({vals[0]})")
print(f"{names[1]}: {percent[1]} ({vals[1]})")
print(f"{names[2]}: {percent[2]} ({vals[2]})")
print(f"{names[3]}: {percent[3]} ({vals[3]})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")
#https://realpython.com/python-f-strings/ for more information


# In[6]:


# write out a text file to the desired folder
opath = os.path.join("..", "Analysis", "results.txt")

with open(opath, 'w') as new: 
    # write and format the results    
    new.write("Election Results\n")
    new.write("-------------------------\n")
    new.write(f"Total Votes: {total_val}\n")
    new.write("-------------------------\n")
    new.write(f"{names[0]}: {percent[0]} ({vals[0]})\n")
    new.write(f"{names[1]}: {percent[1]} ({vals[1]})\n")
    new.write(f"{names[2]}: {percent[2]} ({vals[2]})\n")
    new.write(f"{names[3]}: {percent[3]} ({vals[3]})\n")
    new.write("-------------------------\n")
    new.write(f"Winner: {winner}\n")
    new.write("-------------------------\n")


# In[ ]:




