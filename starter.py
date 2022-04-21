#!/usr/bin/env python
# coding: utf-8

# # Name of project
# 
# - Introduction to project
# - The purpose
# - The use
# - File(s) accessed: /datasets/vehicles_us.csv.
# - We will [Open the data file(s) and study the general information](#general_overview)
# - Summarize observations in [Introductory conclusion section](#general_overview_conclusion).
# 
# 
# *   **Project Plan**  
# 
#     1. **In the [Data preprocessing](#data_preprocessing) stage**:
#         * We will identify missing values and fill in as appropriate.
#         * We removed duplicates.
#         * We will study data types. Change data types where needed.
#         * We will summarize observations, actions taken, and rationales in [Data preprocessing conclusion section](#data_preprocessing_conclusion).             
#     2. **In the [Calculations](#calculations) stage**:
#         * We will add new columns as appropriate.
#         * We will summarize actions taken and rationales in [Calculations conclusion section].(#calculations_conclusion).       
#     3. **In the [Exploratory data analysis](#exploratory_data_analysis) stage**:
#         * We
#         * We
#         * We will summarize observations, actions taken, and rationales in [Exploratory data analysis conclusion section](#exploratory_data_analysis_conclusion).       
#     4. **In the [Overall conclusion](#conclusion)**:
#         * We will summarize the project's analysis. 
#         
#         
# *   **Table of Contents** <a class="anchor" id="table_of_contents"></a> 
# 
#     1. **[Data preprocessing](#data_preprocessing)**
#         * 1.1 [Data preprocessing conclusion section](#data_preprocessing_conclusion)
#     2. **[Calculations](#calculations)**
#         * 2.1 [Calculations conclusion section](#calculations_conclusion)
#     3. **[Carry out exploratory data analysis](#exploratory_data_analysis)**
#         * 3.1 [Exploratory data analysis conclusion section](#exploratory_data_analysis_conclusion)
#     4. **[Overall conclusion](#conclusion)**
#  

# In[ ]:





# <a class="anchor" id="general_overview"></a>
# **Open the data file and study the general information**

# In[ ]:


# import libraries
import pandas as pd
import numpy as np # for changing data types str to int
import matplotlib.pyplot as plt


# In[ ]:


# import sys and insert code to ignore warnings 
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


# In[ ]:


# load the data
try:
# TODO    df = pd.read_csv('  ')
except:
    print('ERROR: Unable to find or access file.')


# In[ ]:


# print the first 5 rows of the dataframe
# TODOprint('\nFirst 5 rows of  table')
# TODO.head()


# In[ ]:


# df general info
# TODO print('\nGeneral info for     table\n')
# TODO print(    .info())
# check df for duplicates 
# TODO print('\nNumber of duplicate rows:',    .duplicated().sum())
# check df for shape 
# TODO print('\nNumber rows and columns:',   .shape)


# In[ ]:


# check general statistics for dataframe
# TODO print('Statistics for      table')
# TODO     .describe()


# <a class="anchor" id="general_overview_conclusion"></a>
# **Introductory Conclusions**
# 
# - We note

# **[Return to table of contents](#table_of_contents)**

# <a class="anchor" id="data_preprocessing"></a>
# **1. Data preprocessing**
# 
# - First we will

# <a class="anchor" id="data_preprocessing_conclusion"></a>
# **1.1 Data preprocessing conclusion**
# 
# - hu
# - jio

# **[Return to table of contents](#table_of_contents)**

# <a class="anchor" id="calculations"></a>
# **2. Calculations**
# 
# - First we will

# <a class="anchor" id="calculations_conclusion"></a>
# **2.1 Calculations conclusion**
# 
# - hu
# - jio

# **[Return to table of contents](#table_of_contents)**

# <a class="anchor" id="exploratory_data_analysis"></a>
# **3. Exploratory data analysis**
# 
# - First we will

# <a class="anchor" id="exploratory_data_analysis_conclusion"></a>
# **3.1 Exploratory data analysis conclusion**
# 
# - hu
# - jio

# **[Return to table of contents](#table_of_contents)**

# <a class="anchor" id="conclusion"></a>
# *   **4. Overall conclusion**
#     1. **In the [Data preprocessing](#data_preprocessing) stage**:
#         * We 
#         * We 
#         * We             
#     2. **In the [Calculations](#calculations) stage**:
#         * We 
#         * We      
#     3. **In the [Exploratory data analysis](#exploratory_data_analysis) stage**:
#         * We
#         * We
#         * We    
#         
# summation paragraph(s)
# 
# Missing values happen for many reasons including human errors, no record of the information, misunderstanding of data types, problems joining files/databases, or problems transferring information.
# 

# **[Return to table of contents](#table_of_contents)**

# **References**
