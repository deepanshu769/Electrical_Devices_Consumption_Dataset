import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the data
data = pd.read_csv("C:/Git hub code/vs code/Kaggel project/Consumption.csv")
#  Consumption of #
fig, ax = plt.subplots(figsize=(12,6))
ax = sns. Consumptionplot(data=data, x="#", color="#00FFFF", order=data["#"].value_ Consumptions().index)
ax.set_title(" Consumption of #")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
#  Consumption of Class
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.countplot(data=data, x="Class", color="#1030C5", order=data["Class"].value_counts().index)
ax.set_title(" Consumption of Class")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
# Histogram of H00:00
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H00:00", color="#96EC2B", bins=30)
ax.set_title(" Consumption of H00:00")
plt.show()
#  Consumption of H00:15
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H00:15", color="#FF5733", bins=20)
ax.set_title(" Consumption of H00:15")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
# Consumption of H00:30
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H00:30", color="#c410c5", bins=20)
ax.set_title(" Consumption of H00:30")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
#  Consumption of H00:45
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H00:45", color="#8e10c5", bins=20)
ax.set_title(" Consumption of H00:45")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
#  Consumption of H01:00
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H01:00", color="#10c5b0", bins=20)
ax.set_title(" Consumption of H01:00")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
#  Consumption of H01:15
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H01:15", color="#b61ead", bins=20)
ax.set_title(" Consumption of H01:15")
ax.bar_label(ax.containers[0], fontsize=15)
plt.show()
#  Consumption of H01:30
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H01:30", color="#00864d", bins=20)
ax.set_title(" Consumption of H01:30")
ax.bar_label(ax.containers[0],fontsize=15)
plt.show()
#  Consumption of H01:45
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.histplot(data=data, x="H01:45", color="#10c578", bins=20)
ax.set_title(" Consumption of H01:45")
ax.bar_label(ax.containers[0],fontsize=15)
plt.show()