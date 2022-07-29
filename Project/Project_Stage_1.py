# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:48:11 2022

@author: Guillermo
"""
###############################################################################
# Copy header formatting from my scripts
###############################################################################


# This project will follow a paper published in the American Economic Review. 
# The purpose of the paper was to test for the presence of racial 
# discrimination in the mortgage approval process. The dataset provided 
# contains records of the 2,380 applicants for mortgages in Boston.


# 2. Read the paper as it provides a detailed discussion of the data and 
# insight on the determinants of the probability of being approved. 

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


os.getcwd()
git_path = 'C:\\Users\\Guillermo\\Documents\\GitHub\\ECO5445SU22\\Project\\Data'
git_path = 'C:/Users/jo585802/OneDrive - University of Central Florida/Documents/GitHub/ECO5445/Project/Data' # Needed line to test data
os.chdir(git_path)
         
# 3. Bring in the dataset provided within my repository. The variables in the 
# dataset do not have intuitive names (e.g., the meaning of S3 is unclear). 
# Referencing the data description and the AER paper, identify the qualitative 
# dependent that you will be modeling and the set of co-variates that you 
# intend to include in your various models, and rename the variables so that 
# they have (somewhat) intuitive names. Be certain that the 
# debt-to-income ratio, race, self-employed, marital status, and 
# education indicator variables are included, among other variables.

housing = pd.read_csv("hmda_sw.csv")

Data_subset = housing[["s6","s7","s13", "s15", "s17","s23a","s27a","s33","s40","s42","s45","s46","school"]]

#               s6               s7          s13    s15         s17                s23a                 s27a             s33             s40                    s42                   s45             S46       school
Col_names = ["Loan_Amount", "Action_Taken", "Race", "Sex" , "Income_Thousands", "Marital_Status", "Self_Employed", "Purchase_Price", "Approved_Credit", "Mortgage_Credit_History", "DTI_Housing", "DTI_Total", "School" ] 

Data_subset.columns = [Col_names]

###############################################################################
# Why did you choose these variables in particular? What information from the
# paper helped you decide?
###############################################################################

###############################################################################
# The categorical variables are currently being treated as numeric. You cannot
# do mean, sd, etc.
###############################################################################

# 4. Generate summary statistics on the set of variables selected, and explain 
# the composition of the sample and of the characteristics of an average 
# (representative) applicant. In the process, you should also generate
# histograms and frequency counts on particular variables of interest, which 
# can be referenced in your explanation of the composition of the sample 
# and of a representative applicant.

Summary = Data_subset.describe()

plt.hist(Data_subset["Loan_Amount"], bins = "fd")
plt.title("Loan Amounts")

plt.hist(Data_subset["Income_Thousands"])
plt.title("Income in Thousands")
plt.xlim(0, 200000)

plt.hist(Data_subset["DTI_Housing"], bins = "fd")
plt.title("Debt to Income - Housing Expenses/Income")

plt.hist(Data_subset["DTI_Total"], bins = "fd")
plt.title("Debt to Income - Total Expenses/Income")

plt.hist(Data_subset["Purchase_Price"])
plt.title("Purchase Prices")

plt.hist(Data_subset["Race"])
plt.title("Race")

plt.hist(Data_subset["Action_Taken"])
plt.title("Actions Taken")
plt.xlabel("1= Loan Originated, 2= Approved but not accepted, 3= Approved and Accepted")


# this scatter plot shows the years of education group on race. The 
# lower alpha allows us to see when a majority of data spikes in one point
plt.scatter(Data_subset["School"],Data_subset["Race"], alpha = .20)
plt.axis([0, 30, 0, 6])
plt.xlabel("Years of Education")
plt.ylabel("Race (Black = 3, White = 5")
plt.title("Years of Education: Grouped by Race")

# Similar to above, this scatter plot shows income in thousands grouped by race
# The darker points indicate a majority of people earning that income amount, 
# a lighter circle indicates little to no people earning that amount. 
plt.scatter(Data_subset["Income_Thousands"], Data_subset["Race"], alpha = .20)
plt.axis([0, 200, 0, 6])
plt.xlabel("Income in Thousands")
plt.ylabel("Race (Black=3, White =5)")
plt.title("Income in Thousands: Grouped by Race")

plt.scatter(Data_subset["DTI_Total"], Data_subset["Race"], alpha = .20)
plt.axis([0, 100, 0, 6])
plt.xlabel("Debt to Income - Total Expenses/Income")
plt.ylabel("Race (Black=3, White =5)")
plt.title("Debt to Income Ratio - TE/I: Grouped by Race")


# The composition of the data is skewed to the right. Of course this is due
# to near infinite values placed on missig data points. If we ignore that we actually 
# see a normal distribution for things like loan amounts, and debt to income ratios.
# An average applicant is applying for around $139,000. They are most likely white,
# male, around 37 years old, income of $139,000. There is an 11% chance they are self employed
# so very little chance. Their debt to income ratio for their total expenses 
# over their income is around 33%. Their average years in school are 15. 
# Some interesting things to note are that more white applicants will apply
# when their income is lower than that of a black applicant. It seems as though
# White applicants are more confident even though their income is lower, 
# this could be due to multiple reasons such as co signers, or even having 
# support from family.  



# 5. What is the baseline probability of an individual being approved 
# for a mortgage?

Loans = Data_subset["Action_Taken"]

Loans.value_counts()

###############################################################################
# This next part requires you to look at a table, then manually input values.
# We can extract values from the tables instead of hand typing them
###############################################################################

Loans_Approved = 2025
Loans_Denied = 285
Loans_Approved_Not_Accepted = 70
Total = 2025 + 285 + 70 
Total_Approved = 2025 + 70

Probability_of_Approval = Total_Approved/Total

print(round(Probability_of_Approval, 2))

Percent_Chance = Probability_of_Approval * 100
print(round(Percent_Chance))
# From above we see that the probability of an individual being approved for a mortgage
# is around 88%


# 6. Based on the data you read in, create a table with the following 
# structure (values will not be the same as the example): 


Race_Subset = (Data_subset["Race"])
Actions_Subset = Data_subset["Action_Taken"]

A = Race_Subset.to_numpy()
B = Actions_Subset.to_numpy()

C = np.concatenate((A, B), axis=1)
# I have been working on this for a long time and finally go it to work
# I dont think I needed to concatenate the array into C but it is working now
# so I am going to leave it here


Black_Approved = 0 
Black_Not_Approved = 0
White_Approved = 0
White_Not_Approved = 0

for i in range(len(C)):
    X = A[i]
    Y = B[i]
    if X == 3 and Y == 1:
        Black_Approved += 1
    elif X == 3 and Y == 2:
        Black_Approved += 1
    elif X == 3 and Y ==  3:
        Black_Not_Approved += 1
    elif X == 5 and Y == 1:
        White_Approved += 1
    elif X == 5 and Y == 2:
        White_Approved += 1
    elif X == 5 and Y ==  3:
        White_Not_Approved += 1

Total_Black = Black_Approved + Black_Not_Approved
Total_White = White_Approved + White_Not_Approved

print("The total number of white applicants is",Total_White,". The total number of black applicants is",Total_Black)
print("Total approved white Applicants is",White_Approved,". Total Approved Black Applicants is",Black_Approved)


Cnames = ["Applicant Race", "Approved","Not Approved","Total"]
Approval_Values = np.array([["Black", 243, 96, 339], ["White", 1852, 189, 2041]])
Approval_Table = pd.DataFrame(Approval_Values, columns=Cnames)
print(Approval_Table)

###############################################################################
# Table does not fully match. Missing bottom row (Total) of table
###############################################################################

# 7. From the table you create in "6", calculate the following
# P(Approved/White)
# P(NotApproved/Black)

P_White_and_Approved = White_Approved/2380
print(round(P_White_and_Approved, 2))


# Probability of being white and approved is around 78%

P_Black_and_Not_Approved = Black_Not_Approved/2380
print(round(P_Black_and_Not_Approved, 2))

# Probability of being black and not approved is around 4%

###############################################################################
# What we were actually looking for is the probability that a person would be
# approved, given that we know they are white. So 1852/2041
###############################################################################

# Not sure if you actually wanted these values
P_AW = White_Approved/Total_Approved
print(P_AW)
# Here we see there is an 88% chance an approved applicant is white 

P_NAB = Black_Not_Approved/(Loans_Denied)
print(P_NAB)
# Here we see that there is a 33% chance not approved candidates will be black

