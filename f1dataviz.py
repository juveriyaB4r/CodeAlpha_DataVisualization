import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the directory of the script itself
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build full path to CSV using that directory
csv_path = os.path.join(script_dir, "cleaned_f1_driver_standings_2024.csv")

# Load CSV from the relative path
df = pd.read_csv(csv_path)

# Plotting (unchanged)
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

top_10 = df.sort_values("Points", ascending=False).head(10)
sns.barplot(x="Points", y="Driver", data=top_10, palette="coolwarm")
plt.title("🏁 Top 10 F1 Drivers by Points (2024)")
plt.xlabel("Points")
plt.ylabel("Driver")
plt.tight_layout()

# Save the plot to the same folder
plot_path = os.path.join(script_dir, "top_10_drivers_points_2024.png")
plt.savefig(plot_path)
plt.show()

