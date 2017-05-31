import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis_Project/rddata.xls")
df1 = df.ix[:,8:12]
df1 = df1[1:36]
#df1
df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']

print("\nThose were a lot of bar graphs, isn't it. Lets try something different.\n\nLet's go for pie charts\n\n")
time.sleep(2.0)
print("Choose the following options for the required functionality\n\n")
print("1 -> visualise the male and population data in a piechart.\n")
print("2 -> visualise the total population data in a piechart.\n")
print("3 -> skip to the next step of my demonstration.\n")
print("4 -> exit the program/demonstration.\n")

while True:
	user_response5 = input("\nPlease enter the relevant key:")
	
	if user_response5 == "1":
		fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(50,20))
		var = df1.groupby(['State']).sum().stack()
		temp = var.unstack()
		type(temp)
		x1_list = temp['Male_Popln']
		x2_list = temp['Fem_Popln']
		label_list = temp.index
		pie_1 = axes[0].pie(x1_list,labels = label_list,autopct = "%1.1f%%")
		axes[0].set_title("Male population Distribution")
		axes[0].axis('equal')
		pie_2 = axes[1].pie(x2_list,labels = label_list,autopct = "%1.1f%%")
		axes[1].set_title("Female population Distribution")
		axes[1].axis('equal')
		plt.subplots_adjust(wspace=1)
		plt.show()

	elif user_response5 == "2":
		fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(30,30))
		var = df1.groupby(['State']).sum().stack()
		temp = var.unstack()
		type(temp)
		x_list = temp['Tot_Popln']
		label_list = temp.index
		plt.axis("equal")
		plt.pie(x_list,labels = label_list,autopct = "%1.1f%%")
		plt.title("Total Population Distribution")
		plt.show()

	elif user_response5 == "3":
		break
	
	elif user_response5 == "4":
		print("\nOkay.Goodbye.")
		exit(1)

	else:
		print("Please enter a valid key.Try again.")