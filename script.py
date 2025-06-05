import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")
df.replace("Unknown", pd.NA, inplace=True)
df.dropna(inplace=True)

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

plt.figure(figsize=(6, 4))
sns.countplot(x="Accident_severity", data=df, palette="Set2", hue=None, legend=False)
plt.title("Accident Severity Distribution")
plt.xlabel("Accident Severity (1=Severe, 2=Slight)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(y="Road_surface_type", hue="Accident_severity", data=df, palette="Set3")
plt.title("Accidents by Road Surface Type")
plt.xlabel("Count")
plt.ylabel("Road Surface Type")
plt.tight_layout()
plt.savefig("road_surface_vs_severity.png")
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(y="Weather_conditions", hue="Accident_severity", data=df, palette="Set1")
plt.title("Accidents by Weather Conditions")
plt.xlabel("Count")
plt.ylabel("Weather Conditions")
plt.tight_layout()
plt.savefig("weather_vs_severity.png")
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(y="Light_conditions", hue="Accident_severity", data=df, palette="pastel")
plt.title("Accidents by Light Conditions")
plt.xlabel("Count")
plt.ylabel("Light Conditions")
plt.tight_layout()
plt.savefig("light_conditions_vs_severity.png")
plt.show()

plt.figure(figsize=(10, 6))
top_causes = df["Cause_of_accident"].value_counts().head(10).index
sns.countplot(y="Cause_of_accident", data=df[df["Cause_of_accident"].isin(top_causes)],
              palette="muted", order=top_causes, hue=None, legend=False)
plt.title("Top 10 Causes of Accidents")
plt.xlabel("Count")
plt.ylabel("Cause of Accident")
plt.tight_layout()
plt.savefig("top_causes.png")
plt.show()

print("All visualizations saved successfully.")
