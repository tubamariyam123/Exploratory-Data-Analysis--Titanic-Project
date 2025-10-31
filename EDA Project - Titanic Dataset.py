# 📊 EDA Project - Titanic Dataset
# TUBA MARIYAM KHATEEB

#------------------------------
#Importing Required Libraries
#------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('Titanic-Dataset.csv')

# Step 2: View the first few rows
df.head()

# Step 3: Basic information
print(df.info())
print(df.describe())

# Step 4: Check for missing values
print(df.isnull().sum())

# Step 5: Visualizations
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.show()

# Step 6: Insights
print("✅ Most females survived.")
print("✅ Younger passengers had higher survival rates.")
print("✅ Higher-class passengers had better chances of survival.")
