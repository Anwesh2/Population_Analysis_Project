import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis_Project/rddata.xls")
df1 = df.ix[:,8:12]
df1 = df1[1:36]
#df1
df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']
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
