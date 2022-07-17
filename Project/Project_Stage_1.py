# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:48:11 2022

@author: Guillermo
"""

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

# this scatter plot shows the years of education group on race. The 
# lower alpha allows us to see when a majority of data spikes in one point
plt.scatter(Data_subset["School"],Data_subset["Race"], alpha = .20)
plt.axis([0, 30, 0, 6])
plt.xlabel("Years of Education")
plt.ylabel("Race (Black = 3, White = 5")
plt.title("Years of Education Grouped by Race")

# Similar to above, this scatter plot shows income in thousands grouped by race
# The darker points indicate a majority of people earning that income amount, 
# a lighter circle indicates little to no people earning that amount. 
plt.scatter(Data_subset["Income_Thousands"], Data_subset["Race"], alpha = .20)
plt.axis([0, 200, 0, 6])
plt.xlabel("Income in Thousands")
plt.ylabel("Race (Black=3, White =5)")
plt.title("Income in Thousands Grouped by Race")

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



# 6. Based on the data you read in, create a table with the following 
# structure (values will not be the same as the example):
    
# 7. From the table you create in "6", calculate the following
# P(Approved/White)
# P(NotApproved/Black)