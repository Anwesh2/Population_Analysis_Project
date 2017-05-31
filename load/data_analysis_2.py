import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

time.sleep(2.0)

df = pd.read_excel("/home/anwesh/Desktop/Data_Analyses/Population_Analysis_Project/rddata.xls")
df1 = df.ix[:,8:12]
df1 = df1[1:36]
#df1
df1.columns = ['State','Male_Popln','Fem_Popln','Tot_Popln']

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

print("So that's it then. This is James...signing off. Have a good day. ")