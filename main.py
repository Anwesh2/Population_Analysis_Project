import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
#% matplotlib inline
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')

print('\nNamaste. \nI am James and am your Data Analyst for today.')

user_response = input("\nShall I give you an example of my prowess ? Say yes OR no\n\n")
if user_response == "yes" :
	print("\nOkay then. Let me analyse a sample of India's population for you.\n\nLoading the dataset ....")
	#df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis_Project/rddata.xls")
	df = pd.read_excel("rddata.xls")
	
	time.sleep(3.0)
	print("\nDone.Dataset is loaded !")
else:
	print("\nOkay then.Have a good day !!")
	exit()

while True:
	user_response2 = input("Do you want to have a look at the dataset ? Say yes OR no\n\n")
	if user_response2 == "yes":
		df1 = df.ix[:,8:12]
		df1 = df1[1:36]
		#df1
		df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']
		print(df1)
		break
	elif user_response2 == "no":
		print("\nFine.As you wish.Let's continue forward.")
		break
	else:
		print("Please enter a valid answer.")

time.sleep(5.0)

df1 = df.ix[:,8:12]
df1 = df1[1:36]
#df1
df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']

import load.bargraphs
import load.sorted_bargraphs
import load.piecharts
import load.data_analysis_1
import load.data_analysis_2



