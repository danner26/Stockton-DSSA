#!/usr/bin/python
# Name: Daniel W. Anner
# Date created: 11/04/2020
# Date last modified: 11/04/2020
# Reads in a csv of Abalone data, and makes scatter plots
# Useage: prompt$ ./plotter.py abalone.csv
# NOTE: Testing code is being kept in this file for the sole purpose of having it as a reference for the future. The color dictionary way of coloring worked and was successful, but unnecessary for this assignment
import matplotlib, csv, sys, time
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd

timestr = time.strftime("%H%M") #grab the current time to use in file names, for github image debugging

#Read the data from the CSV
df = pd.read_csv(sys.argv[1], delimiter=',', header=None, names=[ "sex", "length", "diameter", "height", "whole_weight", "shucked_weight", "viscera_weight", "shell_weight", "rings"])

#df1 = df[["length", "diameter"]]
#color_dict = {'length': '#50FFD7', 'diameter': '#FF7F50'}

#create the scatter plot
fig, ax = plt.subplots(1,1)
#set zorder to 2 so it is at the top of the final graph
ax.scatter(df["length"], df["diameter"], s=10, zorder=2, c='#FF7F50', label="Diameter (mm)") #[color_dict.get(x, '#333333') for x in df1.columns], label=[color_dict.get(x, "x") for x in df1.columns])
fig.suptitle("Abalone Physical Statistics")
plt.xlabel("Length (mm)");
plt.ylabel("Diameter (mm)");

plt.legend(title="Color Legend")
plt.savefig("png/abalone_data_2dimensions_" + timestr + ".png")

#df2 = df[["length", "diameter", "whole_weight", "shell_weight"]]
#color_dict = {'diameter': '#FF7F50', 'shell_weight': '#50FFD7', 'length': '#FFD750', 'whole_weight': '#50FF7F'}

#fig2, ax2 = plt.subplots(1,1)
#ax2.scatter(df[["diameter", "shell_weight"]], df[["length", "whole_weight"]], s=10, c=[color_dict.get(x, '#333333') for x in df2.columns], label=df2.)
#fig2.suptitle("Abalone Physical Statistics")
#ax.scatter(df["whole_weight"], df["shell_weight"], c=[color_dict.get(x, '#333333') for x in df.columns])
ax.scatter(df["length"], df["whole_weight"], s=10, c="#50FF7F", zorder=0, label="Whole Weight (grams)")
ax.scatter(df["length"], df["shell_weight"], s=10, c="#50FFD7", zorder=1, label="Shell Weight (grams)")
plt.ylabel("MM/Grams");
ax.legend()

plt.xlabel('Length (mm)')
caption=('''It is pretty clear that the longer the length,
the larger the diameter in millimeters.
You can also see the longer the Abalone,
the greater the weight in grams.
There is a slow positive growth of shell weight
xbut the whole weight grows more exponentially.''')
ax.text(1, 1, caption)

plt.savefig("png/abalone_data_4dimensions_" + timestr + ".png", bbox_inches = "tight")
