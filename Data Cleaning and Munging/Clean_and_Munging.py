import pandas as pd
import numpy as np
from pandas import read_csv
df = read_csv("D:\\R dir\\Cricket\\ODI_cric2.csv")
print df.head(10)

#Cleaning and Munging

df[df["Runs"] == "DNB"] = 0
df[df["Minutes"] == "-"] = 0
df[df["Balls Faced"] == "-"] = 0
df[df["Fours"] == "-"] = 0
df[df["Sixes"] == "-"] = 0
df[df["Strike Rate"] == "-"] = 0
#print df

# Data type-casting
#Runs = df["Runs"].astype(int)
Minutes = df["Minutes"].astype(int)
Balls_Faced = df["Balls Faced"].astype(int)
Fours = df["Fours"].astype(int)
Sixes = df["Sixes"].astype(int)
Strike_Rate = df["Strike Rate"].astype(float)


#Slicing the non-numeric data
Player = df["Player"]
Country = df["Country"]
Innings = df["Inns"]
Opposition = df["Opposition"]
