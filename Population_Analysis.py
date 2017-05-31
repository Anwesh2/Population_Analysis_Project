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
	df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis/rddata.xls")
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
""" I had to use the definitions of df1 here again as df1 was defined/created
inside an if statement when user chose "yes" as a response.df1 will be used a lot in the future."""

""" Some IMPROVEMENT that can be done is to ask whether the user wants to see the dataset,then pause the whole program and while the user 
had his fill of watching the dataset,then ask him to unpause the command.This will make the program truly interactive and user friendly.

Also,I have to find a way such that the user can check the previous graphs (if he/she want to) without running the whole program again"""

print("\nOkay, let me put my powers to use and help you visualise the datset.\n ")
time.sleep(2.0)
print("Choose the following options for the required functionality\n\n")
print("1 -> visualise the entire dataset in a bargraph.\n")
print("2 -> visualise the entire dataset in a stacked bar chart.\n")
print("3 -> skip to the next step of my demonstration.\n")
print("4 -> exit the program/demonstration.\n")

while True:
	user_response3 = input("Please enter any relevant key:")

	if user_response3 == "1":
		x = df1[['Tot_Popln','Male_Popln','Fem_Popln']].plot(df1['State'],kind ='bar',title ="Population Comparision",figsize=(30,10),legend = True,color =("blue","green","red"),fontsize=12)
		ax = plt.gca()
		ax.set_xlabel("States and categories",fontsize =20)
		ax.set_ylabel("Population Values in millions",fontsize = 20)
		#for p in ax.patches:
			#ax.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.legend(loc='upper left')
		plt.show(ax)
		#break
	elif user_response3 == "2":
		ax4 = plt.gca()
		ax4 = df1.plot(x = "State", y="Tot_Popln", kind="bar", figsize=(30,10))
		df1.plot(x="State", y ="Male_Popln", kind="bar", ax=ax4, color="C2")
		df1.plot(x="State", y ="Fem_Popln", kind="bar", ax=ax4, color="C3")
		#for p in ax4.patches:
			#ax4.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005)) # this is for annotating the top of the bar with values
		plt.legend(loc='upper left')
		plt.show()
		#break

	elif user_response3 == "3":
		break

	elif user_response3 == "4":
		print("\nOkay.Goodbye.")
		exit(1)

	else:
		print("Please enter a valid key.Try again.")
"""
The following is ALTERNATE code for creating stacked barchart for the same data
f, ax5 = plt.subplots(1, figsize=(70,10))
bar_width = 0.75

plt.legend(loc='upper left')

bar_l = [i+1 for i in range(len(df1['Fem_Popln']))]
tick_pos = [i+(bar_width/2) for i in bar_l]
ax5.bar(bar_l,
		# using the pre_score data
		df1['Fem_Popln'],
		# set the width
		width=bar_width,
		# with the label pre score
		label='Female Population',
		# with alpha 0.5
		alpha=0.5,
		# with color
		color='#F4561D')

ax5.bar(bar_l,
		# using the mid_score data
		df1['Male_Popln'],
		# set the width
		width=bar_width,
		# with pre_score on the bottom
		bottom=df1['Fem_Popln'],
		# with the label mid score
		label='Male Population',
		# with alpha 0.5
		alpha=0.5,
		# with color
		color='#F1911E')

ax5.bar(bar_l,
		# using the post_score data
		df1['Tot_Popln'],
		# set the width
		width=bar_width,
		# with pre_score and mid_score on the bottom
		bottom=[i+j for i,j in zip(df1['Fem_Popln'],df1['Male_Popln'])],
		# with the label post score
		label='Total_Popln',
		# with alpha 0.5
		alpha=0.5,
		# with color
		color='#F1BD1A')

plt.xticks(tick_pos, df1['State'])
ax1.set_ylabel("Population in millions")
ax1.set_xlabel("States and Categories")
plt.legend(loc='upper left')

#for p in ax5.patches:
 #   ax5.annotate(str(p.get_height()),(p.get_x()*1.005,p.get_height()*1.005))
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.show() 

"""

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


print("Okay then.I have showed you my data visualisation powers.\n")
print("Let me now perform some data analysis for you on the dataset.\nPlease hold on a moment for processing the data.....!! \n\n")
""" Lol ROFLLLL """
time.sleep(3.0)
print("Okay....I have processed the data. Choose the required options\n\n")
print("Choose the following options for the required functionality\n\n")
print(" 1 -> state with highest total population.\n")
print(" 2 -> state with highest male population.\n")
print(" 3 -> state with highest female population.\n")
print(" 4 -> skip to the next step of my demonstration\n")
print(" 5 -> exit the program/demonstration.\n")

while True:
	user_response6 = input("\nPlease enter the relevant key:\n\n")

	if user_response6== "1":
		print(df1.loc[df1['Tot_Popln'].idxmax()])

	elif user_response6== "2":
		print(df1.loc[df1['Male_Popln'].idxmax()])

	elif user_response6 =="3":
		print(df1.loc[df1['Fem_Popln'].idxmax()])

	elif user_response6== "4":
		break
	
	elif user_response6 == "5":
		print("\nOkay.Goodbye.")
		exit(1)

	else:
		print("Please enter a valid key.Try again.")



print(" \nWant some more analysis ? Okay then ...let's proceed.\n")
time.sleep(2.0)
print("Choose the following options for the required functionality\n\n")
print(" 1 -> states with male population geater than female population.\n")
print(" 2 -> states with female population geater than male population.\n")
print(" 3 -> states with population geater than 50 million.\n")
print(" 4 -> states with population lesser than 1 million.\n")
print(" 5 if you want to skip .")
# print(" Press 6 if you want to exit the program/demonstration.")

while True:
	user_response7 = input("Please enter the relevant key:\n\n")

	if user_response7== "1":
		x = (df1["Male_Popln"]) > (df1["Fem_Popln"])
		print(df1[x])
		
	elif user_response7== "2":
		y= (df1["Male_Popln"]) < (df1["Fem_Popln"])
		#df1.loc[(df1["Male_Popln"]) < (df1["Fem_Popln"]), "State"].values
		print(df1[y])

	elif user_response7 =="3":
		z = (df1["Tot_Popln"]) > 50.0
		print(len(df1[z].index))
		print(df1[z])

	elif user_response7 =="4":
		z = (df1["Tot_Popln"]) < 1.0
		print(len(df1[z].index))
		print(df1[z])

	elif user_response7== "5":
		break
	
	elif user_response7 == "6":
		print("\nOkay.Goodbye.")
		exit(1)

	else:
		print(" Please enter a valid key.Try again.")

print("\n\nSo that's it then. This is James...signing off. Have a good day. ")

""" 

Here I was trying to manage the outliers by taking log of the values.
But,then many of the resultant values startes getting negative.df1


df1['Tot_Popln'] = np.log(df1['Tot_Popln'])
df1['Male_Popln'] = np.log(df1['Male_Popln'])
df1['Fem_Popln'] = np.log(df1['Fem_Popln'])
df1

"""

 

