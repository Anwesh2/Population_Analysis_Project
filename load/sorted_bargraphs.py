import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis_Project/rddata.xls")
df1 = df.ix[:,8:12]
df1 = df1[1:36]
#df1
df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']

print("\nLet me give you further evidence of my visualisation powers !\n ")

""" Some IMPROVEMENTS that can be done at this stage are:
	1. Check and store the attributes/columns of the datset.
	2. Check which of the above attributes contain integer values.Only those columns 
	containing integer values can be displayed using a bar graph. Also,these colums can be sorted
	in ascending/descending order and the result can again be plotted in a bar graph. """
time.sleep(2.0)	
print("Choose the following options for the required functionality\n\n")
print("1 -> visualise the male population data in a bargraph.\n")
print("2 -> sort and visualise the male population data in a bargraph.\n")
print("3 -> visualise the female population data in a bargraph.\n")
print("4 -> sort and visualise the female population data in a bargraph.\n")
print("5 -> visualise the total population data in a bargraph.\n")
print("6 -> sort and visualise the total population data in a bargraph.\n")
print("7 -> skip to the next step of my demonstration.\n")
print("8 -> exit the program/demonstration.\n")

while True:
	user_response4 = input("Please enter the relevant key:")

	if user_response4 == "1":
		ax21 = plt.gca()
		ax21 = df1[['Male_Popln']].plot(df1['State'],kind ='bar',title =" Male Population ",figsize=(100,50),legend = True,fontsize=12)
		ax21.set_xlabel("States",fontsize =20)
		ax21.set_ylabel("Population Values in millions",fontsize = 20)
		for p in ax21.patches:
			ax21.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.show(ax21)
	
	elif user_response4 == "2":
		df3 = df1.sort_values(['Male_Popln'], ascending = [False])
		df3 = df3.reset_index(drop=True)
		df3 = df3[['State','Male_Popln']]
		#df3
		ax22 = plt.gca()
		ax22 = df3[['Male_Popln']].plot(df1['State'],kind ='bar',title =" Male Population - Sorted",figsize=(100,50),legend = True,fontsize=12)
		ax22.set_xlabel("States",fontsize =20)
		ax22.set_ylabel("Population Values in millions",fontsize = 20)
		for p in ax22.patches:
			ax22.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.show(ax22)
		
	elif user_response4 == "3":
		ax31 = plt.gca()
		ax31 = df1[['Fem_Popln']].plot(df1['State'],kind ='bar',title ="Female Population ",figsize=(100,50),legend = True,fontsize=12)
		ax31.set_xlabel("States",fontsize =20)
		ax31.set_ylabel("Population Values in millions",fontsize = 20)
		for p in ax31.patches:
			ax31.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.show(ax31)
	
	elif user_response4 == "4":
		df3 = df1.sort_values(['Fem_Popln'], ascending = [False])
		df3 = df3.reset_index(drop=True)
		df3 = df3[['State','Fem_Popln']]
		#df3
		ax32 = plt.gca()
		ax32 = df3[['Fem_Popln']].plot(df1['State'],kind ='bar',title =" Female Population - Sorted",figsize=(100,50),legend = True,fontsize=12)
		ax32.set_xlabel("States",fontsize =20)
		ax32.set_ylabel("Population Values in millions",fontsize = 20)
		for p in ax32.patches:
			ax32.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.show(ax32)
		
	elif user_response4 == "5":
		ax41 = plt.gca()
		ax41 = df1[['Tot_Popln']].plot(df1['State'],kind ='bar',title =" Total Population ",figsize=(100,50),legend = True,fontsize=12)
		ax41.set_xlabel("States",fontsize =20)
		ax41.set_ylabel("Population Values in millions",fontsize = 20)
		for p in ax41.patches:
			ax41.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.show(ax41)
	elif user_response4 == "6":
		df3 = df1.sort_values(['Tot_Popln'], ascending = [False])
		df3 = df3.reset_index(drop=True)
		df3 = df3[['State','Tot_Popln']]
		#df3
		ax42 = plt.gca()
		ax42 = df3[['Tot_Popln']].plot(df1['State'],kind ='bar',title =" Total Population - Sorted",figsize=(100,50),legend = True,fontsize=12)
		ax42.set_xlabel("States",fontsize =20)
		ax42.set_ylabel("Population Values in millions",fontsize = 20)
		for p in ax42.patches:
			ax42.annotate(str(p.get_height()),(p.get_x()*1.e005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.show(ax42)
	
	elif user_response4 == "7":
		break
	
	elif user_response4 == "8":
		print("\nOkay.Goodbye.")
		exit(1)

	else:
		print("Please enter a valid key.Try again.")