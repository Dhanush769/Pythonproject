import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("census.csv");

filtered = data[(data["Area Name"] == "India") & 
                (data["Total/Rural/Urban"] == "Total") & 
                (data["Religion"] == "All Religious Communities")]

plt.figure(figsize=(12, 6))
sns.barplot(data=filtered, x="Age-Group", y="Non-Workers - Persons")
plt.xticks(rotation=45)
plt.title("Non-Workers by Age Group in India")
plt.ylabel("Number of Non-Workers")
plt.xlabel("Age Group")
plt.tight_layout()
plt.show()

