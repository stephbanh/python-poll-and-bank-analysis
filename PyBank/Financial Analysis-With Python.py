#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary modules
import os
import csv


# In[2]:


# create a path to reference the spreadsheet
cpath = os.path.join('..', 'Resources', 'budget_data.csv')


# In[3]:


# create variable to hold the imported values 
report = {"Dates":[],"Profits/Losses":[],"Differences":[]}

with open(cpath) as profits:
    reader = csv.reader(profits, delimiter = ',')
    next(reader, None)
    storage = 0
       
    # use it to fill in the dictionary values for dates and profits/losses
    for row in reader:
        
        report["Dates"].append(row[0])
        report["Profits/Losses"].append(int(row[1]))
        diffs = int(row[1]) - storage 
        report["Differences"].append(diffs) # need to remove the first value
        storage = int(row[1])


# In[4]:


# the length of dates will be the length of months 
total_months = len(report["Dates"])


# In[5]:


# add up all the values in profits/losses
total_earned = sum(report["Profits/Losses"])


# In[6]:


# remove the first value of the differences dictionary 
# since it has no previous row to reference and is using a defaulted value of 0 it will skew the data
report["Differences"].pop(0)
diff_sums = sum(report["Differences"])
average_change = round(diff_sums/len(report["Differences"]),2)


# In[7]:


# calculate greatest mon and value here
greatest_increase_val = max(report["Differences"])
greatest_decrease_val = min(report["Differences"])


# In[8]:


# use conditionals to match them and a loop to iterate through the differences list to search for them
i = 0 
while i < len(report["Differences"]):
    if report["Differences"][i] == greatest_increase_val:
        # match with i + 1 as differences list is off by one (has one less value for computation reasons)
        greatest_increase_mon = report["Dates"][i+1]
    if report["Differences"][i] == greatest_decrease_val:
        # match with i + 1 as differences listis off by one (has one less value for computation reasons)
        greatest_decrease_mon = report["Dates"][i+1]
    i += 1


# In[9]:


#print results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_earned))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_mon) + " ($" + str(greatest_increase_val) + ")" )
print("Greatest Decrease in Profits: " + str(greatest_decrease_mon) + " ($" + str(greatest_decrease_val) + ")" )


# In[10]:


# final formatting/expected results
#  ```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12 
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```

# this should all be exported to a txt file sent to the Analysis folder
opath = os.path.join("..", "Analysis", "results.txt")

with open(opath, 'w') as new: 
    #write and format the results
    
    new.write("Financial Analysis\n")
    new.write("----------------------------\n")
    new.write("Total Months: " + str(total_months) + "\n")
    new.write("Total: $" + str(total_earned) + "\n")
    new.write("Average Change: $" + str(average_change) + "\n")
    new.write("Greatest Increase in Profits: " + str(greatest_increase_mon) + " ($" + str(greatest_increase_val) + ")\n" )
    new.write("Greatest Decrease in Profits: " + str(greatest_decrease_mon) + " ($" + str(greatest_decrease_val) + ")\n" )


# In[ ]:




