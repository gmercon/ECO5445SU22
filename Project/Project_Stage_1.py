# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:48:11 2022

@author: Guillermo
"""

#This project will follow a paper published in the American Economic Review. 
# The purpose of the paper was to test for the presence of racial 
# discrimination in the mortgage approval process. The dataset provided 
# contains records of the 2,380 applicants for mortgages in Boston.


# 2. Read the paper as it provides a detailed discussion of the data and 
# insight on the determinants of the probability of being approved. 


# 3. Bring in the dataset provided within my repository. The variables in the 
# dataset do not have intuitive names (e.g., the meaning of S3 is unclear). 
# Referencing the data description and the AER paper, identify the qualitative 
# dependent that you will be modeling and the set of co-variates that you 
# intend to include in your various models, and rename the variables so that 
# they have (somewhat) intuitive names. Be certain that the 
# debt-to-income ratio, race, self-employed, marital status, and 
# education indicator variables are included, among other variables.

# 4. Generate summary statistics on the set of variables selected, and explain 
# the composition of the sample and of the characteristics of an average 
# (representative) applicant. In the process, you should also generate
# histograms and frequency counts on particular variables of interest, which 
# can be referenced in your explanation of the composition of the sample 
# and of a representative applicant.

# 5. What is the baseline probability of an individual being approved 
# for a mortgage?

# 6. Based on the data you read in, create a table with the following 
# structure (values will not be the same as the example):
    
# 7. From the table you create in "6", calculate the following
# P(Approved/White)
# P(NotApproved/Black)