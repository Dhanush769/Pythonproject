import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("census.csv")

filtered = data[(data["Area Name"] == "India") & 
                (data["Total/Rural/Urban"] == "Total") & 
                (data["Religion"] == "All Religious Communities")]

plt.figure(figsize=(10, 6))
sns.barplot(data=filtered, x="Age-Group", y="Non-Workers - Persons", color="gray", label="Non-Workers")
sns.barplot(data=filtered, x="Age-Group", y="Main Activity - Students - Persons", color="green", label="Students")
plt.xticks(rotation=45)
plt.title("Non-Workers vs. Students by Age Group")
plt.legend()
plt.tight_layout()
plt.show()
