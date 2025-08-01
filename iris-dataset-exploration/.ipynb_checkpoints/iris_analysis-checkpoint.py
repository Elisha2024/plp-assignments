# Task 1: Load and Explore the Dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Try loading the dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print(" Dataset loaded successfully!")
except Exception as e:
    print(" Error loading dataset:", e)

# Display first few rows
print("\ First 5 rows of the dataset:")
print(df.head())

# Inspect structure
print("\n Dataset Info:")
print(df.info())

# Check for missing values
print("\n❓ Missing values:")
print(df.isnull().sum())

# No missing values in Iris dataset, but let's include a fill/drop for practice
df_cleaned = df.dropna()  # drop rows with missing values (if any)

#  Task 2: Basic Data Analysis
print("\n📊 Descriptive statistics:")
print(df_cleaned.describe())

# Group by target (species)
df_cleaned['species'] = df_cleaned['target'].apply(lambda x: iris.target_names[x])

grouped = df_cleaned.groupby("species").mean(numeric_only=True)
print("\n📚 Mean of numerical features grouped by species:")
print(grouped)

# 🧐 Identify Patterns
print("\n💡 Observations:")
print("• Iris-virginica generally has the largest petal dimensions.")
print("• Iris-setosa has the smallest petal lengths and widths.")

# 🎨 Task 3: Data Visualization

# Line Chart: We'll simulate a time-series using index for visualization
plt.figure(figsize=(8, 4))
plt.plot(df_cleaned.index, df_cleaned["sepal length (cm)"], label="Sepal Length")
plt.plot(df_cleaned.index, df_cleaned["petal length (cm)"], label="Petal Length")
plt.title("Line Chart: Sepal & Petal Length over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(data=df_cleaned, x="species", y="petal length (cm)", ci=None)
plt.title("Bar Chart: Avg Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.tight_layout()
plt.show()

# Histogram: Distribution of Sepal Width
plt.figure(figsize=(6, 4))
plt.hist(df_cleaned["sepal width (cm)"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df_cleaned, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="Set1")
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()
