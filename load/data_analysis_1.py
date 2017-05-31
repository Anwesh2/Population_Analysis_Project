import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis_Project/rddata.xls")
df1 = df.ix[:,8:12]
df1 = df1[1:36]
#df1
df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']

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
