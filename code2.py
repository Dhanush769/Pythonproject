import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("census.csv")

filtered = data[(data["Area Name"] == "India") & 
                (data["Total/Rural/Urban"] == "Total") & 
                (data["Religion"] == "All Religious Communities")]

plt.figure(figsize=(12, 6))
sns.barplot(data=filtered, x="Age-Group", y="Main Activity - Students - Persons", color="lightblue", label="Total")
sns.barplot(data=filtered, x="Age-Group", y="Main Activity - Students - Males", color="blue", label="Males")
sns.barplot(data=filtered, x="Age-Group", y="Main Activity - Students - Females", color="pink", label="Females", alpha=0.6)
plt.xticks(rotation=45)
plt.title("Students by Age Group and Gender")
plt.legend()
plt.tight_layout()
plt.show()
