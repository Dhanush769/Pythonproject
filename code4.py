import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("census.csv")

filtered = data[(data["Area Name"] == "India") & 
                (data["Total/Rural/Urban"] == "Total") & 
                (data["Religion"] == "All Religious Communities")]

activities = {
    "Students": filtered["Main Activity - Students - Persons"].sum(),
    "Household Duties": filtered["Main Activity - Household Duties - Persons"].sum(),
    "Dependents": filtered["Main Activity - Dependents - Persons"].sum(),
    "Pensioners": filtered["Main Activity - Pensioners - Persons"].sum(),
    "Rentiers": filtered["Main Activity - Rentiers - Persons"].sum(),
    "Beggars, Vagrants": filtered["Main Activity - Beggars, Vagrants etc. - Persons"].sum(),
    "Others": filtered["Main Activity - Others - Persons"].sum()
}

plt.figure(figsize=(8, 8))
plt.pie(activities.values(), labels=activities.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Main Activities - India Total")
plt.tight_layout()
plt.show()
